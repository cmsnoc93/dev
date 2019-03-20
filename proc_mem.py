import subprocess
from netmiko import Netmiko

src_ip = '10.7.14.7'

src = Netmiko(ip=src_ip,username="rit",password="pan",device_type="cisco_ios",)

print("Connected")

ret = src.send_command("show proc mem | include Pool Total")

def mb(str):
    return round(int(str)/1024/1024,2)

def percent(a,b):
    return round((int(a)/int(b)) * 100,2)

memory = dict()
vals = ret.split(' ')
memory.update({'processor':{'total':mb(vals[4]),'used':mb(vals[8]),'free':mb(vals[11][0:-2]),'percent':percent(vals[8],vals[4])},'io':{'total':mb(vals[22]),'used':mb(vals[27]),'free':mb(vals[32]),'percent':percent(vals[27],vals[22])}})
print(memory)







