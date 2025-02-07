

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
        print('now it is turned on')
    def turn_off(self):
        self.status='off'
        print('now it is turned off')
    def get_status(self):
        return self.status




import numpy as np

class Sensor:
    def __init__(self,name,group,unit,pin):
        self.name=name
        self.group=group
        self.pin=pin
        self.unit=unit
        self.current_value=None
    def read_sensor(self):
        return np.random.uniform(20,25)





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
        
        pass
    #Sensor --> a1=Sensor(...)
    #def create_device
    
    def create_sensor(self):
        pass
    
    def add_sensor_in_group(self,group_name):
        #yek group name bede va to sensor ro tooye oon list ezaf koni
        
        #add_devcie_in_group
        
        pass
    
    
    def get_data_from_sensor_in_group(self,group_name):
        
        '''
        
        lkiving__room --> tamame sensor haro mire behet 
        datasho pas mide
        '''
        pass
