import subprocess
from netmiko import Netmiko

src_ip = input("Enter source ip: ")
dst_ip = input("Enter dst ip: ")

#If tracerouting from jumphost to src
#result = subprocess.call(['traceroute',src_ip]).split('\n')

src = Netmiko(ip=src_ip,username="admin",password="noc",secret='noc',device_type="cisco_ios",)

print(src.find_prompt())
trace = src.send_command('traceroute '+dst_ip)
path = trace.split('\n')[4:]
path = [i.split()[1] for i in path]
print("Hops: ",path)

devices = []
for ip in path:
    devices.append(Netmiko(ip=ip,username="admin",password="noc",device_type="cisco_ios",))

       
for device in devices:
    print(device.find_prompt())
    print(device.send_command('show ip int br | include up'))

src.disconnect()
for r in devices:
    r.disconnect()
print("Disconnected from all devices")
