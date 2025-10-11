#=============================DEVICE============================
import numpy as np

class Device:
    def __init__(self, topic, pin=None):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.status = 'off'
        self.pin = pin

    def turn_on(self):
        self.status = 'on'

    def turn_off(self):
        self.status = 'off'

    def get_status(self):
        return self.status

#=============================SENSOR============================

class Sensor:
    def __init__(self, name, group_name, unit, pin=None):
        self.name = name
        self.group_name = group_name
        self.pin = pin
        self.unit = unit
        self.current_value = None

    def read_sensor(self):
        return np.random.uniform(20, 25)

#=============================ADMIN PANEL============================

class admin_panel:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'group {group_name} is created')
        else:
            print('your name is duplicated')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            if isinstance(device, Device):
                self.groups[group_name].append(device)
                print(f'device {device.name} added in group {group_name}')
            else:
                print('You must add a Device object')
        else:
            print(f'group {group_name} does not exist')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {device_type} created in group {group_name}')
        else:
            print('your group does not exist')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f'{device_type}{i}'
                topic = f'home/{group_name}/{device_type}/{device_name}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'{number_of_devices} device(s) {device_type} added to group {group_name}')
        else:
            print(f'group {group_name} does not exist')

    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            print(f'all devices in {group_name}:')
            return self.groups[group_name]
        else:
            print(f'group {group_name} does not exist')
            return []

    def turn_on_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            if isinstance(device, Device):
                device.turn_on()
        print(f'all devices in group {group_name} are now turned on')

    def turn_off_all_in_groups(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            if isinstance(device, Device):
                device.turn_off()
        print(f'all devices in group {group_name} are now turned off')

    def turn_on_all_devices(self):
        all_device = []
        for devices in self.groups.values():
            all_device.extend([d for d in devices if isinstance(d, Device)])
        for i in all_device:
            i.turn_on()
        print('all devices are turned on now')

    def turn_off_all_devices(self):
        all_device = []
        for devices in self.groups.values():
            all_device.extend([d for d in devices if isinstance(d, Device)])
        for i in all_device:
            i.turn_off()
        print('all devices are turned off now')

    def get_status_in_group(self, group_name):
        if group_name in self.groups:
            all_device = self.get_devices_in_groups(group_name)
            for i in all_device:
                if isinstance(i, Device):
                    print(f'device {i.name} is {i.status}')
        else:
            print(f'group {group_name} does not exist')

    def get_status_in_device_type(self, device_type):
        found = False
        for devices in self.groups.values():
            for device in devices:
                if isinstance(device, Device) and device.device_type == device_type:
                    print(f'{device.name} in {device.group} is {device.status}')
                    found = True
        if not found:
            print(f'{device_type} not found')

    def add_sensor_in_group(self, group_name, sensor):
        if group_name in self.groups:
            if isinstance(sensor, Sensor):
                self.groups[group_name].append(sensor)
                print(f'sensor {sensor.name} added in group {group_name}')
            else:
                print('You must add a Sensor object')
        else:
            print(f'group {group_name} does not exist')

    def create_sensor(self, name, group_name, unit):
        if group_name in self.groups:
            new_sensor = Sensor(name, group_name, unit)
            self.add_sensor_in_group(group_name, new_sensor)
            print(f'sensor {name} created in group {group_name}')
        else:
            print('your group does not exist')

    def get_data_from_sensor_in_group(self, group_name):
        if group_name in self.groups:
            for i in self.groups[group_name]:
                if isinstance(i, Sensor):
                    print(f'sensor {i.name} data: {i.read_sensor()} {i.unit}')
        else:
            print(f'group {group_name} does not exist')

    def delete_all_devives_in_group(self, group_name):
        if group_name in self.groups:
            new_group = [i for i in self.groups[group_name] if not isinstance(i, Device)]
            self.groups[group_name] = new_group
            print(f'all devices in group {group_name} deleted')
        else:
            print(f'group {group_name} does not exist')

    def delete_all_sensors_in_group(self, group_name):
        if group_name in self.groups:
            new_group = [i for i in self.groups[group_name] if not isinstance(i, Sensor)]
            self.groups[group_name] = new_group
            print(f'all sensors in group {group_name} deleted')
        else:
            print(f'group {group_name} does not exist')

    def rename_groupname(self, group_name, new_group_name):
        if group_name in self.groups:
            if new_group_name not in self.groups:
                self.groups[new_group_name] = self.groups[group_name]
                del self.groups[group_name]
                print(f'group {group_name} renamed to {new_group_name}')
            else:
                print(f'group {new_group_name} is duplicate')
        else:
            print(f'group {group_name} does not exist')

    def status_one_device_in_group(self, device_type, name):
        found = False
        for devices in self.groups.values():
            for i in devices:
                if isinstance(i, Device) and i.name == name and i.device_type == device_type:
                    print(f'status {name} : {i.get_status()}')
                    found = True
                    break
            if found:
                break
        if not found:
            print('the device_type or name is incorrect')

# ============================= USAGE EXAMPLES =============================

a1 = Device('home/kitchen/lamp/lamp0')
a = Sensor('kontorol', 'living_room', 'c')
b = admin_panel()
b.create_group('wc')
b.create_group('living_room')
b.create_group('kitchen')
b.create_sensor('kontorol', 'living_room', 'c')
b.add_sensor_in_group('living_room', a)
b.create_device('living_room', 'lamp', 'lamp1')
b.create_device('wc', 'fan', 'fan1')
b.create_device('wc', 'water', 'pump1')
b.add_device_to_group('kitchen', a1)
b.create_multiple_devices('kitchen', 'door', 3)
b.create_multiple_devices('living_room', 'lamp', 7)
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
