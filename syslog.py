import re
from netmiko import Netmiko

src_ip = '10.1.7.1'

src = Netmiko(ip=src_ip,username="rit",password="pan",device_type="cisco_ios",)

print("Connected")
time = src.send_command("show clock").split(" ")[3:5]
time = time[0]+" "+time[1]
print(time)
#ret = src.send_command("show log | i down|Down|up|Up|err|fail|Fail|drop|crash|MALLOCFAIL|duplex",time[0]+" "+str((int(time[1])-1)))
ret = src.send_command("show log | i "+time)
arr = ret.split('\n')

count=0
syslog = dict()
for line in arr:
    if line.find('%')!=-1 and (line.find("NBRCHANGE")!=-1 or line.find("ADJCHANGE")!=-1 or line.find("UPDOWN")!=-1 or line.find("duplex")!=-1):
        syslog.update({count:line})
        count+=1

print(syslog)
	
        










