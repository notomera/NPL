from netmiko import ConnectHandler

cisco = {
    'device_type': 'cisco_ios',
    'host': '10.100.0.100',
    'username': 'npl',
    'password': 'npl',
    }

R1 = ConnectHandler(**cisco)
print(R1.find_prompt())         # Verify that you've an established SSH connection

R1_output = R1.send_command("show ip int brief")
print(R1_output)
#play with the enable password see if netmiko will use the default credintial
# R1 = ConnectHandler(device_type='cisco_ios', host='10.100.0.100', username='npl', password='npl')