import paramiko
import time
from netmiko import ConnectHandler, SSHDetect
from subprocess import Popen, PIPE
import re
ip = '10.9.10.9'
username = 'rit'
password = 'CMSnoc$1234'
rem = paramiko.SSHClient()
rem.set_missing_host_key_policy(paramiko.AutoAddPolicy())
boo=True
while boo:
    try:
        rem.connect(ip,port=22, username=username, password=password)
        boo=False
        print ("SSH connection established for getting the version - ",ip)
        stdin,stdout,stderr=rem.exec_command("show version")
    except Exception as e:
        print("Error in ssh connection, Trying again. Error - ",e) 
        boo=True
  
    

output=stdout.readlines()
#print(output)
output='\n'.join(output)
k=output.replace('\n',' ')
#print("\n\n\n\n")
#print(k)
k=k.split()
#print("\n\n\n\n")
#print(k)
a=k.index('Cisco')
#print(a)
#print(k[a+1])
ios_ver=''
verdict={}
if (k[a+1]=='IOS'):
    if (k[a+2]=='XE'):
        ios_ver='cisco_xe'
    else:
        ios_ver='cisco_ios'
else:
    ios_ver='cisco_nxos'

print(ios_ver)


verdict['soft_ver']=ios_ver

if ios_ver=='cisco_nxos':
    var=k.index('BIOS:')
    var3=k.index('kickstart:')
    verdict['version']="BIOS: "+k[var+2]+" Kickstart: "+k[var3+2]
    var=k.index('uptime')
    var2=k.index('second(s)')
    verdict['uptime']=' '.join(k[var+2:var2+1])
    var=k.index('Hardware')
    verdict['hardware']=' '.join(k[var+1:var+3])
    var=k.index('Reason:')
    verdict['reload_reason']=k[var+1]

elif ios_ver=='cisco_xe':
    var=k.index('weeks,')
    var2=k.index('minutes')
    verdict['uptime']=' '.join(k[var-1:var2+1])

    var=k.index('Last')
    var2=k.index('This')
    verdict['reload_reason']=' '.join(k[var+3:var2])
 
    var=k.index('Version')

    verdict['version']=k[var+1]
    
    var=k.index('Release')
    verdict['hardware']=k[var+4]  

     

else:
    
    var=k.index('Version')
    verdict['version']=' '.join(k[var+1][:-1])
    var=k.index('Software,')
    verdict['hardware']=k[var+1]  
    var=k.index('uptime')
    var2=k.index('minutes')
    verdict['uptime']=' '.join(k[var+2:var2+1])
    var=k.index('reason:')
    var2=k.index('This')
    verdict['reload_reason']=' '.join(k[var+1:var2])

#print(verdict)
#dictofobj[nme].gennodedict['version']=verdict 

rem.close()
#needs nexus as cisco_nxos

now=ip

ssh= ConnectHandler(device_type=ios_ver,host=now,username="rit",password="CMSnoc$1234")

dst='10.1.2.1'

'''
if ios_ver=='cisco_nxos':
    ret=ssh.send_command("sh ip route "+dst)
    print(" return from sh ip route | inc known via ")
    ret=ret.split('\n')[6:]
    print(ret)


    if 'attached' in ret[0]:
        print('connected",')
        prot='connected",'
    else:
        t3=0
        for line in ret:
            line=line.split()    
            for word in line:
                #print(word)
                if re.match('^eigrp*',word):
                    print("eigrp")
                    prot='eigrp'
                    t3=1
                    break
            if t3==1:
                break
#bgp condition not included


    if prot=='connected",':
        ret=ssh.send_command("sh ip route "+dst)
        print(" return from sh ip route | inc known via ")
        ret=ret.split('\n')[6:]
        print(ret)
        ret=ret[1].split()
        print(ret)
        posn=ret.index('*via')
        print(posn)
        exit_int=ret[posn+2][:-1]
        print(exit_int)
        ret=ssh.send_command("sh ip int brief | include "+exit_int)
        ret=ret.split()
        print(ret)
        exit_int_ip=ret[1]
        print(exit_int_ip)
    else:
        ret=ssh.send_command("sh ip route "+dst+" | include via")
        #ret=ret.split('\n')[6:]
        print(ret)
        #posn=ret.index('*via')
        #next_hop_ip=
        ret=ret.split('\n')
        for line in ret:
            line=line.split()
            print(line)
            if '*via' in line:
                via_pos=line.index('*via')
                next_hop_ip=line[via_pos+1][:-1]
                exit_int=line[via_pos+2][:-1]
                ret2=ssh.send_command("sh ip int brief | include "+exit_int)
                ret2=ret2.split()
                print(ret2)
                exit_int_ip=ret2[1]
                print(next_hop_ip+"   "+exit_int+"  "+exit_int_ip)
        

    ret=ssh.send_command('sh ip int brief | include '+now)
    ret=ret.split()
    entry_int=ret[0]
    print("entry interface "+entry_int)


#only to be run on destination


#REMOVE THE LINE BELOW
    dst=now 
    ret=ssh.send_command('sh ip int brief | include '+dst)
    ret=ret.split()
    print(ret)
    entry_int_dst=ret[0]
    print("entry on dest "+entry_int_dst)



#ret=ssh.send_command('ping 10.9.16.16')
#ret=ret.split()
#print(ret)
src='10.1.2.1'
dst='10.9.16.16'
ping_stat=dict()
cmd="ping -c 4 "+src
p=Popen(cmd,shell=True, stdout=PIPE, stderr=PIPE)
out,err=p.communicate()
print(out)
out=out.split()
print('\n')
print(out)
rec_index='received,'.encode('ascii')
num_stat=int(out[out.index(rec_index)-1].decode('ascii'))
print(num_stat)
if num_stat==4:
    ping_stat['source']='Ping successful. source reachable'
    ping_stat['def_gate']='Ping successful. DG reachable'
    print('Ping successful. source reachable')
elif num_stat>0:
    ping_stat['source']='Ping not completely successful'
    
    ping_stat['def_gate']='Ping not completely successful. DG reachable'
    print('Not completely successful. Check connectivity')
else:
    print('Source not reachable')
    
    
ret=ssh.send_command("ping "+dst)
ret=ret.split()
print(ret)

'''


if ios_ver=='cisco_nxos':
    ret=ssh.send_command('show proc cpu | ex 0.0',use_textfsm=True)
    #ret=ret.split()
    print(ret)



  





















    




















