import subprocess
from netmiko import Netmiko

src = input("Enter source ip: ")
dst = input("Enter dst ip: :")

#result = subprocess.call(['traceroute',src]).split('\n')

r2 = Netmiko(ip=src,username="admin",password="noc",secret='noc',device_type="cisco_ios",)

#r2.enable();
print(r2.find_prompt())
trace = r2.send_command('traceroute '+dst)
path = trace.split('\n')[4:]
path = [i.split()[1] for i in path]
print("Hops: ",path)

devices = []
for ip in path:
    devices.append(Netmiko(ip=ip,username="admin",password="noc",device_type="cisco_ios",))

       
for device in devices:
    print(device.find_prompt())
    print(device.send_command('show ip int br | include up'))

r2.disconnect()
for r in devices:
    r.disconnect()
print("Disconnected from all devices")
