from netmiko import ConnectHandler

c1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.51',
    'username': 'admin',
    'password': 'cisco'
}

c2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.52',
    'username': 'admin',
    'password': 'cisco'
}

a1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.53',
    'username': 'admin',
    'password': 'cisco'
}

a2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.54',
    'username': 'admin',
    'password': 'cisco'
}

a3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.55',
    'username': 'admin',
    'password': 'cisco'
}

core_sw = [c1,c2]
access_sw = [a1,a2,a3]

with open("core_switches_conf") as f:
    core_sw_commands = f.read().splitlines()
print(core_sw_commands)

with open("access_switches_conf") as f:
    access_sw_commands = f.read().splitlines()
print(access_sw_commands)


for c in core_sw:
    net_connect = ConnectHandler(**c)
    print("Configuring Core Switch: ", c['host'], "...")
    output = net_connect.send_config_set(core_sw_commands)
    net_connect.send_command('write memory')
    net_connect.disconnect()
    print(output)


for a in access_sw:
    net_connect = ConnectHandler(**a)
    print("Configuring Access Switch: ", a['host'], "...")
    output = net_connect.send_config_set(access_sw_commands)
    net_connect.send_command('write memory')
    print(output)
    net_connect.disconnect()
