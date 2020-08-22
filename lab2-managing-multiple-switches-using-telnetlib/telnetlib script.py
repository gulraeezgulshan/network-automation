import telnetlib
from devices import switches

for switch in switches:
    HOST = switch['ip']
    user = switch['username'].strip()
    password = switch['password'].strip()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\r\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\r\n")

    print("Configuring " + switch['host'] + "...")
    tn.write(b"enable\n")
    tn.write(b"conf t\n")
    tn.write(b"int loop 0\n")
    tn.write(b"ip addr 1.1.1.1 255.255.255.255\n")
    tn.write(b"exit\n")
    tn.write(b"int loop 1\n")
    tn.write(b"ip addr 2.2.2.3 255.255.255.255\n")
    tn.write(b"exit\n")
    tn.write(b"int loop 2\n")
    tn.write(b"ip addr 3.3.3.3 255.255.255.255\n")
    tn.write(b"exit\n")
    tn.write(b"end\n")
    print(tn.read_all().decode('ascii'))
