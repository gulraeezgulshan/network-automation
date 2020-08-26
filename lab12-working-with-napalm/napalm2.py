from napalm import get_network_driver
import json

host = '192.168.0.51'
user_name = 'admin'
password = 'cisco'

driver = get_network_driver('ios')

device = driver(host, user_name, password)
device.open()
device.load_merge_candidate(config='interface GigabitEthernet0/1\n ip address 192.168.0.52 255.255.255.0\n no shutdown\n end\n')
print(device.compare_config())
device.load_merge_candidate(config='interface GigabitEthernet0/2\n ip address 192.168.0.53 255.255.255.0\n no shutdown\n end\n')
print(device.compare_config())
device.commit_config()

print(json.dumps(device.get_interfaces_ip(), sort_keys=True, indent=2))

device.close()
