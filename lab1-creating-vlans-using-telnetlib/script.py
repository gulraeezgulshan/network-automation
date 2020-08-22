import telnetlib

HOST = "192.168.0.50"

user = "admin"
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"terminal lenght 0\n")
tn.write(b"conf t\n")

for n in range(2,21):
    print("creating vlan " + str(n) + "...")
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name AXIOM_" + str(n).encode('ascii') + b"\n")

tn.write(b"do sh vlan br\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))