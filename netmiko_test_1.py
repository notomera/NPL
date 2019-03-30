from netmiko import ConnectHandler
import yaml

# cisco = {
#     'device_type': 'cisco_ios',
#     'host': '10.100.0.100',
#     'username': 'npl',
#     'password': 'npl',
#     'secret': 'npl'
#     }
#
# R1 = ConnectHandler(**cisco)
#
# #Enter enable mode
# R1.enable()
#
# #copy the running config to a file
#
# R1.send_command('terminal length 0')
# R1_rc = R1.send_command('show run')
# with open('R1_running_config.txt', 'w') as rc:
#     rc.write(R1_rc)
#
#
# R1.disconnect()

with open('input.yml') as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)
print(data)
device1_data = data['devices']['device_1']
print(device1_data)

R1 = ConnectHandler(**device1_data)

#Enter enable mode
R1.enable()

#copy the running config to a file

R1.send_command('terminal length 0')
R1_rc = R1.send_command('show run')
with open('R1_int.txt', 'w') as rc:
    rc.write(R1_rc)


R1.disconnect()