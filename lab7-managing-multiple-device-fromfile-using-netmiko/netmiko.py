from netmiko import ConnectHandler

sw1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.50',
    'username': 'admin',
    'password': 'cisco'
}

sw2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.51',
    'username': 'admin',
    'password': 'cisco'
}

sw3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.52',
    'username': 'admin',
    'password': 'cisco'
}

sw4 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.53',
    'username': 'admin',
    'password': 'cisco'
}

sw5 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.54',
    'username': 'admin',
    'password': 'cisco'
}

devices = [sw1,sw2,sw3,sw4,sw5]

for device in devices:
    net_connect = ConnectHandler(**device)
    print("Configuring ", device['host'])
    for n in range(2,11):
        print('Configuring VLAN ' + str (n))
        config_commands = ['vlan ' + str(n),
                           'name AXIOM_' + str(n)]
        output = net_connect.send_config_set(config_commands)
    net_connect.send_command('write memory')
    output = net_connect.send_command('show vlan br')
    print(output)

