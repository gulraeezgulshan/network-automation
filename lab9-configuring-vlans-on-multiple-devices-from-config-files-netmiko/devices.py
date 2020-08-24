devices = [
    {
        "host": "SW1",
        "domain": "axiom.com.pk",
        "username": "admin",
        "password": "cisco",
        "ip": "192.168.0.51",
        "mask": "255.255.255.0",
        "interface" : "vlan 1"
    },
    {
        "host": "SW2",
        "domain": "axiom.com.pk",
        "username": "admin",
        "password": "cisco",
        "ip": "192.168.0.52",
        "mask": "255.255.255.0",
        "interface" : "vlan 1"
    },
    {
        "host": "SW3",
        "domain": "axiom.com.pk",
        "username": "admin",
        "password": "cisco",
        "ip": "192.168.0.53",
        "mask": "255.255.255.0",
        "interface" : "vlan 1"
    }
]

interfaces= [
    {
        "name": "gi0/1",
        "description": "pc1 vlan 10",
        "vlan": 10,
        "uplink": False
    },
    {
        "name": "gi0/2",
        "description": "pc2 vlan 11",
        "vlan": 11,
        "uplink": False
    },
    {
        "name": "gi0/3",
        "description": "pc1 vlan 12",
        "vlan": 12,
        "uplink": False
    },
    {
        "name": "gi0/0",
        "description": "switch trunk port",
        "vlan": None,
        "uplink": True
    }
]