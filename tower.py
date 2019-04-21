from netmiko import ConnectHandler
from helper import connection_data, parsed_yaml


def device_connection(new_base_data, new_commands):
    device_ssh_data = ''
    device_ssh = ConnectHandler(**new_base_data)

    device_ssh.enable()
    device_name = device_ssh.find_prompt().split('#')[0]
    device_ssh.send_command('terminal length 0')

    for command in new_commands:
        device_ssh_data += '\n {0} {1} {0} \n {2} {3}'.format('*' * 20, command, device_ssh.send_command(command),
                                                              '\n' * 5)

    return device_name, device_ssh_data


def main():
    inventory = 'inventory.yml'
    data = parsed_yaml(inventory)
    base_data = data['base']
    devices = data['devices']

    all_data = connection_data(base_data, devices)

    for data_ in all_data:
        device_name, device_ssh_data = device_connection(*data_)
        with open(f'{device_name}_data.txt', 'w') as captured_data:
            captured_data.write(device_ssh_data)


if __name__ == '__main__':
    main()
