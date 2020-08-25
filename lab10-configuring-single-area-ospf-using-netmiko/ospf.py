from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

#Number of routers participating in OSPF
hosts = ["R1","R2","R3","R4","R5","R6"]

#SSH Username and Password of each router
username = 'admin'
password = 'cisco'

#Management Interface
ssh_interface = 'GigabitEthernet0/0'

host_starting_ip = 51


#Collection of devices for initial configuration like SSH and Management IP
devices = []

for r in hosts:
    devices.append({"host": r,
                    "domain": "axiom.com.pk",
                    "username": username,
                    "password": password,
                    "ip": "192.168.0."+str(hosts.index(r)+host_starting_ip),
                    "mask": "255.255.255.0",
                    "interface": ssh_interface})

#Jinja template being used of Initial Configuration
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")
output = template.render(devices=devices)

#Initial configuration being saved to text file;
# Now need to first apply this configuration to each router separately
with open("initial_configuration.txt", 'w') as f:
    f.writelines(output)

routers = []

for r in hosts:
    routers.append({"device_type": "cisco_ios",
                    "host": "192.168.0."+str(hosts.index(r)+host_starting_ip),
                    "username": username,
                    "password": password})

for device in routers:
    try:
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_command('show run | sec ospf')
            ospf_commands = ['router ospf 1', 'net 0.0.0.0 255.255.255.255 area 0']
            if('router ospf' not in output):
                print('OSPF is not enabled on device: ' + device['host'])
                answer = input('Would you like you enable default OSPF settings on: ' + device['host'] + ' <y/n> ')
                if answer == 'y':
                    output = net_connect.send_config_set(ospf_commands)
                    output += net_connect.save_config()
                    print(output)

                    print('OSPF is now configured!')
                else:
                    print('No OSPF configurations have been made!')
            else:
                print("OSPF is already configured on device: " + device['host'])
    except:
        print("Something went wrong... ! Please sure you have enabled ssh and made initial configurations.")




