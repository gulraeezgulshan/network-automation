from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from devices import interfaces

sw1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.51',
    'username': 'admin',
    'password': 'cisco'
}

sw2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.52',
    'username': 'admin',
    'password': 'cisco'
}

sw3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.53',
    'username': 'admin',
    'password': 'cisco'
}

devices = [sw1, sw2, sw3]

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("interface_template.j2")
commands = template.render(interfaces=interfaces)
print("Loading configuring from file...")
print(commands)
print("---------------------------------")
print("\n")

with open('sw.conf', 'w') as config_file:
     config_file.writelines(commands)


for device in devices:
    print("Configuring ", device['host'], "...\n")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file('sw.conf')
    verification = net_connect.send_command('show vlan br')
    print(verification)
    net_connect.disconnect()