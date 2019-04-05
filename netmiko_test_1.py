from netmiko import ConnectHandler
import yaml
from copy import deepcopy

# TODO:
# -add the command to be sent _DONE
# -type of the device _DONE
# -password independent connection _DONE
# -add a site name
# -WHAT IF THERE IS NO ENABLE PASSWORD
# -style the output with the device name and the command _DONE 50%
# -Use asyncio for multitasking.

with open('input.yml') as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)

# print(f'this is the input data \n{data}')
# GRABBING BASE DATA
base_data = data['base']

# GRABBING DEVICE DATA
devices = data['devices']
# print(f'this is the devices data \n{devices}')

for device, host in devices.items():
    # print(f'this is the host data \n{host}')
    # A COPY OF THE DATA THAT WOULD BE MANIPULATED MORE THAN ONCE
    new_base_data = deepcopy(base_data)

    # INIT THE DEVICE OUTPUT
    device_ssh_data = ''

    if 'username' in host and not host['username']: host.pop('username')
    if 'password' in host and not host['password']: host.pop('password')
    if 'secret' in host and not host['secret']: host.pop('secret')
    if 'device_type' in host and not host['device_type']: host.pop('device_type')
    if 'commands' in host and not host['commands']: host.pop('commands')
    # print(host)
    new_base_data.update(host)

    # COMMANDS TO BE PASSED FOR DEVICES
    commands = new_base_data.pop('commands').split(',')
    new_commands = deepcopy(commands)
    # print(f'this is the commands data \n{commands}')
    # print(f'this is the new_base_data data \n{new_base_data}')
    device_ssh = ConnectHandler(**new_base_data)

    device_name = device_ssh.find_prompt().split('>')[0]

    device_ssh.enable()

    device_ssh.send_command('terminal length 0')
    for command in new_commands:
        device_ssh_data += '\n {0} {1} {0} \n {2} {3}'.format('*'*20, command, device_ssh.send_command(command), '\n'*5)
    with open(f'{device_name}_data', 'w') as rc:
        rc.write(device_ssh_data)

    device_ssh.disconnect()

