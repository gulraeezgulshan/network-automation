from netmiko import ConnectHandler

cisco_ios1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.116',
    'username': 'admin',
    'password': 'cisco'
}

net_connect = ConnectHandler(**cisco_ios1)

with open('command') as f:
    config_commands = f.read().splitlines()

print(config_commands)

output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command('show ip int brief')
print(output)