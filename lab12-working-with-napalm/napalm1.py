from napalm import get_network_driver
import json

host = '192.168.0.51'
user_name = 'admin'
password = 'cisco'

driver = get_network_driver('ios')

device = driver(host, user_name, password)
device.open()
# for d in dir(device):
#     print(d)

#print(device.get_facts())
#print(json.dumps(device.get_facts(), indent=2))

#print(json.dumps(device.get_interfaces(), indent=2))

#print(json.dumps(device.get_interfaces_ip(), indent=2))

#print(json.dumps(device.get_arp_table(), indent=2))

#print(json.dumps(device.get_config(), indent=2))

#print(json.dumps(device.get_config()['startup'], indent=2))
#print(device.get_config()['startup'])
#print(json.dumps(device.get_config()['running'], indent=2))
#print(device.get_config()['running'])

#print(json.dumps(device.get_users(), indent=2))
#print(json.dumps(device.get_vlans(), indent=2))
device.close()