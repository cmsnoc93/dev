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
temp_vals = ret.split(' ')
vals = []
for string in temp_vals:
    if len(string.strip())>0:
        vals.append(string.strip("\n"))
        
memory.update({'processor':{'total':mb(vals[3]),'used':mb(vals[5]),'free':mb(vals[7]),'percent':percent(vals[5],vals[3])},'io':{'total':mb(vals[11]),'used':mb(vals[13]),'free':mb(vals[15]),'percent':percent(vals[13],vals[11])}})
print(memory)







