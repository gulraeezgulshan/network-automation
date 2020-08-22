import telnetlib

HOST = "192.168.0.116"

user = "admin"
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip addr 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip addr 2.2.2.3 255.255.255.255\n")
tn.write(b"int loop 2\n")
tn.write(b"ip addr 3.3.3.3 255.255.255.255\n")
tn.write(b"end\n")

tn.write(b"sh ip int br\n")

print(tn.read_all().decode('ascii'))