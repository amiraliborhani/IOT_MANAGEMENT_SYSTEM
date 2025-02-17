'''

APM: ahsant besiar awli
tahe codeton yek example usage bezarid yani benevisid k chijori msieh estefade kard az class ha
'''
#salam aghaye pilevar add kardam
#=============================DEVCIE============================
import numpy as np
class Device:
    def __init__(self,topic,pin=None):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.status='off'
        self.pin=pin
    def turn_on(self):
        self.status='on'
        #print('now it is turned on')
    def turn_off(self):
        self.status='off'
        #print('now it is turned off')
    def get_status(self):
        return self.status



#=============================sensor============================

class Sensor:
    def __init__(self,name,group_name,unit,pin=None):
        self.name=name
        self.group_name=group_name
        self.pin=pin
        self.unit=unit
        self.current_value=None
    def read_sensor(self):
        return np.random.uniform(20,25)




#=============================ADMIN PANEL============================


class admin_panel:
    def __init__(self):
        self.groups={}
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
        else:
            print('your name is dublicated')
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device} added in group {group_name}')
        else:
            print('f group {group_name} does not exsist')
    def create_device(self,group_name,device_type,name):
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {device_type} craeted in group {group_name}')
        else:
            print('your group does not exist')
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        if group_name in self.groups:
            for i in range(1,number_of_devcies+1):
                device_name=f'{device_type}{i}'
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'{number_of_devcies} device {device_type} added to group {group_name}')
        else:
            print(f'group {group_name} does not exist')
    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name]
            print(f'all devises in {group_name} ')
        else:
            print(f'group {group_name} does not exist')
    def turn_on_all_in_groups(self,group_name):
        devices=self.get_devices_in_groups(group_name) 
        for device in devices:
            device.turn_on()
        print(f'all devices in group {group_name} are now turned on')
    def turn_off_all_in_groups(self,group_name):
        devises=self.get_devices_in_groups(group_name)
        for devise in devises:
            devise.turn_off()
        print(f'all devices in group {group_name} are now turned off')
    def turn_on_all_devices(self):
       for devices in self.groups.values():
          all_device=[]
          all_device.extend(devices)
       for i in all_device:
           i.turn_on()
       print('all devices are turned on now')
    def turn_off_all_devices(self):
        for devices in self.groups.values():
            all_device=[]
            all_device.extend(devices)
        for i in all_device:
            i.turn_off()
        print('all devices are turned off now')
    def get_status_in_group(self,gorup_name):
        if gorup_name in self.groups:
            all_device=self.get_devices_in_groups(gorup_name)
            for i in all_device:
                if i.status=='on':
                    print(f'device {i.name} is on')
                elif i.status=='off':
                    print(f'device {i.name} is off')
        else:
            print(f'group {gorup_name} does not exsist')
    def get_status_in_device_type(self,device_type):
        all_device=[]
        for i in self.groups.values():
            all_device.extend(i)
        for device in all_device:
          if device.device_type==device_type:
               if device.status=='on':
                 print(f'{device.name} in {device.group} is on')
               elif device.status=='off':
                 print(f'{device.name} in {device.group} is off')
          else:
            print(f'{device_type} not found')
            break
    def add_sensor_in_group(self,group_name,sensor):
        if group_name in self.groups:
            self.groups[group_name].append(sensor)
            print(f'sensor {sensor} added in group {group_name}')
        else:
            print('f group {group_name} does not exsist')
    def create_sensor(self,name,group_name,unit):
         if group_name in self.groups:
            topic=f'{name}/{group_name}/{unit}'
            new_sensor=Sensor(topic)
            self.add_sensor_in_group(group_name, new_sensor)
            print(f'sensor {name} craeted in group {group_name}')
         else:
           print('your group does not exist') 
    def get_data_from_sensor_in_group(self,group_name):
        if group_name in self.groups:
             for i in self.groups.values():
               if isinstance(i, Sensor):
                 print(f'sensor {i.name} data: {i.read_sensor()} {i.unit}')
        else:
            print(f'group {group_name} does not exsist')
    def delete_all_devives_in_group(self,group_name):
      new_group = []
        if group_name in self.groups:
           for i in self.groups[group_name]:
               if not isinstance(i, Device):  
                   new_group.extend(i)
           self.groups[group_name] = new_group  
           print(f'all sensors in group {group_name} deleted')
        else:
           print(f'group {group_name} does not exist')
    def delete_all_sensors_in_group(self, group_name):
      new_group = []
      if group_name in self.groups:
        for i in self.groups[group_name]:
            if not isinstance(i, Sensor):  
                new_group.extend(i)
        self.groups[group_name] = new_group  
        print(f'all sensors in group {group_name} deleted')
      else:
        print(f'group {group_name} does not exist')
    def rename_groupname(self,group_name,new_group_name):
        if group_name in self.groups:
             if new_group_name not in self.groups:
                 self.groups[new_group_name]=self.groups[group_name]
                 del self.groups[group_name]
                 print(f'name group {group_name} renamed to {new_group_name} ')
             else:
                 print(f'group {new_group_name} is duplicate')
        else:
            print(f'group {group_name} does not exsist')
    def status_one_device_in_group(self,device_type,name):
        all_device=[]
        for i in self.groups.values():
            all_device.extend(i)
        for i in all_device:
         if isinstance(i, Device):
              if i.name==name and i.device_type==device_type:
               print(f'status {name} : {i.get_status()}')
               break
        else:
             print('the device_type or name is incorrect')


a1=Device('home/kitchen/lamp/lamp0')
a=Sensor('kontorol', 'living_room', 'c')
b=admin_panel()
b.create_sensor('kontorol', 'living_room', 'c')
b.add_sensor_in_group('living_room', a)
b.create_group('wc')
b.create_group('living_room')
b.create_group('kitchen')
b.create_device('living_room', 'lamp', 'lamp1')
b.create_device('wc', 'fan', 'fan1')
b.create_device('wc', 'water_pump', 'pump1')
b.add_device_to_group('kitchen', a1)
b.add_device_to_group('living_room', 'lamp')
b.add_device_to_group('wc', 'fan')
b.add_device_to_group('wc', 'water')
b.create_multiple_devices('kitchen', 'door', 3)
b.create_multiple_devices('living_room','lamp',7)
b.create_multiple_devices('wc', 'fan', 2)
b.create_multiple_devices('wc', 'water', 2)
b.turn_on_all_in_groups('wc')
b.turn_off_all_in_groups('kitchen')
b.get_status_in_group('kitchen')
b.get_devices_in_groups('living_room')
b.turn_on_all_devices()
b.get_data_from_sensor_in_group('living_room')
b.delete_all_devives_in_group('wc')
b.delete_all_sensors_in_group('living_room')
b.rename_groupname('wc', 'bathroom')
b.status_one_device_in_group('lamp', 'lamp1')
