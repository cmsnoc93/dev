import re
from netmiko import Netmiko

src_ip = '10.1.7.1'

src = Netmiko(ip=src_ip,username="rit",password="pan",device_type="cisco_ios",)

print("Connected")

ret = src.send_command("show log | i down|Down|up|Up|err|fail|Fail|drop|crash|MALLOCFAIL|duplex")
arr = ret.split('\n')

count=0
syslog = dict()
for line in arr:
    if line.find('%')!=-1:
        syslog.update({count:line})
        count+=1

print(syslog)
	
        










