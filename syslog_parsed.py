import re
from netmiko import Netmiko

src_ip = '10.1.7.1'

src = Netmiko(ip=src_ip,username="rit",password="pan",device_type="cisco_ios",)

print("Connected")

ret = src.send_command("show log | i down|Down|up|Up|err|fail|Fail|drop|crash|MALLOCFAIL|duplex")
arr = ret.split('\n')

for line in arr:
    if line.find('%')!=-1:
        #print(line)
        if line.find('NBRCHANGE')!=-1:
            print("EIGRP Flap :",'Up' if line.find('down') == -1 else 'Down', re.findall(r'[0-9]+(?:\.[0-9]){3}',line),line[line.rfind("(")+1:line.rfind(")")])
        elif line.find('ADJCHANGE')!=-1:
             print("BGP Flap :",'Up' if line.find('Down') == -1 else 'Down',re.findall(r'[0-9]+(?:\.[0-9]){3}',line))
        elif line.find('UPDOWN')!=-1 or line.find('LINK')!=-1:
             print("Interface Flap :",'Link' if line.find('Line') == -1 else 'Line Protocol','Up' if line.find('down') == -1 else 'Down',line[line.find("Interface")+9:line.find(",")])
        elif line.find('duplex'):
             print("Duplex Mismatch :",line[line.find('on')+2:line.find("(")])










