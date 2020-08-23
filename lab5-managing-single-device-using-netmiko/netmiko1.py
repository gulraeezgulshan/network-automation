from netmiko import ConnectHandler

cisco_ios1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.116',
    'username': 'admin',
    'password': 'cisco'
}

net_connect = ConnectHandler(**cisco_ios1)

config_commands = [ 'int g0/2',
                    'ip addr 192.168.0.100 255.255.255.0',
                    'no shut' ]

output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command('show ip int brief')
print(output)