from netmiko import ConnectHandler
import yaml


with open('input.yml') as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)

base_data = data['base']
devices = data['devices']
print(devices)

for device, host in devices.items():
    # print(host)
    base_data.update(host)
    # print(base_data)
    device_ssh = ConnectHandler(**base_data)

    device_name = device_ssh.find_prompt().split('>')[0]

    device_ssh.enable()
    device_ssh.send_command('terminal length 0')
    device_ssh_rc = device_ssh.send_command('show run')
    with open(f'{device_name}_running_config.txt', 'w') as rc:
        rc.write(device_ssh_rc)

    device_ssh.disconnect()
