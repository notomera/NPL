import yaml
from copy import deepcopy


def parsed_yaml(inventory):
    with open(f'{inventory}') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)


def connection_data(base_data, devices):
    for device, host in devices.items():
        # print(f'this is the host data \n{host}')
        # A COPY OF THE DATA THAT WOULD BE MANIPULATED MORE THAN ONCE
        new_base_data = deepcopy(base_data)
        # INIT THE DEVICE OUTPUT

        if 'username' in host and not host['username']:
            host.pop('username')
        if 'password' in host and not host['password']:
            host.pop('password')
        if 'secret' in host and not host['secret']:
            host.pop('secret')
        if 'device_type' in host and not host['device_type']:
            host.pop('device_type')
        if 'commands' in host and not host['commands']:
            host.pop('commands')
        # print(host)
        new_base_data.update(host)

        # COMMANDS TO BE PASSED FOR DEVICES
        commands = new_base_data.pop('commands').split(',')
        new_commands = deepcopy(commands)

        yield new_base_data, new_commands
