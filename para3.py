import paramiko
import time
from netmiko import ConnectHandler, SSHDetect
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
#rint("\n\n\n\n")
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
'''
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

#elif ios_ver=='cisco_xe':
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

     

#else:
    
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

print(verdict)
#dictofobj[nme].gennodedict['version']=verdict 
'''
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





'''




#KPIs on nexus
    #ret=ssh.send_command("sh proc cpu | ex 0.0",use_textfsm=True)
    #print(ret)
    




'''
    ret=ssh.send_command("sh ip route",use_textfsm=True)
    #print(ret)
    for l in ret:
        print(l)
        print('\n')
'''

#sh feature | i eigrp
#sh feature | i eigrp

    #ans=ssh.send_command("show ip protocols | include bgp")
    #ans1=ssh.send_command("show ip protocols | include eigrp")


    #ans=ssh.send_command("show ip eigrp neighbors",use_textfsm=True)
    #print(ans)
    #template=open('cisco_ios_show_ip_eigrp_neighbors.template')
    #res_template=textfsm.TextFSM(template)
    #ans_final=res_template.ParseText(ans)

    #ans=ssh.send_command("show ip bgp summary")
    #print(ans)
    #template=open('cisco_ios_show_ip_bgp_summary.template')
    #res_template=textfsm.TextFSM(template)
    #ans_final=res_template.ParseText(ans)
    #print(ans_final)



#ret=ssh.send_command("sh ip bgp summary")
#print(ret)
'''
three=[]
neigh_wise=dict()
all_bgp_neigh=set()
for rot in range(3):
    ret=ssh.send_command("sh ip bgp summary",use_textfsm=True)
    #print(ret)
    three.append(ret)
    for move in range(0,len(ret)):
        if ret[move]['bgp_neigh'] not in all_bgp_neigh:
            all_bgp_neigh.add(ret[move]['bgp_neigh'])
            neigh_wise[ret[move]['bgp_neigh']]=list()
        neigh_wise[ret[move]['bgp_neigh']].append(ret[move])
    time.sleep(1)

#if len(three[0])!=len(three[1]) and len(three[1])!=len(three(2)):
    #number of neighbors not constant
    
for i in neigh_wise.keys():
    print(neigh_wise[i])
    print("\n")

for neigh in all_bgp_neigh:
    len_list=len(neigh_wise[neigh])
    a=neigh_wise[neigh][0]
    b=neigh_wise[neigh][1]
    c=neigh_wise[neigh][2]
    c['condition']=''
    c['condition']='perfect'
    concheck=1
    if a['state_pfxrcd']!=b['state_pfxrcd'] and b['state_pfxrcd']!=c['state_pfxrcd']:
        if concheck==1:
            concheck=0
            c['condition']=''
        c['condition']+='Number of routes exchanged is changing. '  
        
    if a['state_pfxrcd']=='Idle (Admin)' or b['state_pfxrcd']=='Idle (Admin)' or c['state_pfxrcd']=='Idle (Admin)':
        if concheck==1:
            concheck=0
            c['condition']=''
        c['condition']+='Neighbor in Idle (Admin) state. Check if it is shutdown. '

    if a['state_pfxrcd'].isdigit()==False or b['state_pfxrcd'].isdigit()==False or c['state_pfxrcd'].isdigit()==False :
        if concheck==1:
            concheck=0
            c['condition']=''
        c['condition']+='Routes not being exchanged. '

    if a['updown']=='never' or b['updown']=='never' or c['updown']=='never':
        c['condition']+='. Neighborship not established properly. '
    if re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',a['updown']):
        if not(re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',b['updown'])) or not(re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',c['updown'])):
            if concheck==1:
                concheck=0
                c['condition']=''
            c['condition']+='Neighborship flapping. '

        else:
            at1=int(a['updown'][:2])*60*60+int(a['updown'][3:5])*60+int(a['updown'][6:])
            bt1=int(b['updown'][:2])*60*60+int(b['updown'][3:5])*60+int(b['updown'][6:])
            ct1=int(c['updown'][:2])*60*60+int(c['updown'][3:5])*60+int(c['updown'][6:])
            if not(at1<bt1) or not(bt1<ct1):
                if concheck==1:
                    concheck=0
                    c['condition']=''
                c['condition']+='Neighborship Flapping. '
                
    if re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',c['updown']):
        ct1=int(a['updown'][:2])*60*60+int(a['updown'][3:5])*60+int(a['updown'][6:])
        if ct1<3600:
            if concheck==1:
                concheck=0
                c['condition']=''
            c['condition']+='Neighbor uptime less than an hour. '
    print("\n\n")    
    print(c)
    #dictofobj[nme].gennodedict['bgp_neigh'][c['bgp_neigh']]=dict()
    #dictofobj[nme].gennodedict['bgp_neigh'][c['bgp_neigh']]=c


ret=ssh.send_command("sh feature | i eigrp",use_textfsm=True)
print(ret)
eigrp_flag=0
for moo in ret:
    if moo['state']=='enabled':
        eigrp_flag=1
        break

#bgp not checked    

    
ret=ssh.send_command("sh feature | i bgp",use_textfsm=True)
print(ret)
for l in ret:
    print(l)
    print('\n')
            


ret=ssh.send_command("sh ip route | inc 00:",use_textfsm=True)
print(ret)
for l in ret:
    print(l)
    print('\n')
   
neigh_wise_eig=dict()
all_eig_neigh=set()


if ios_ver=='cisco_nxos':
    e_size=list()
    for iterate in range(0,3):
        ret=ssh.send_command("sh ip eigrp neighbor")
        #print(ret)
        ret=ret.split('\n')[3:]
        print(ret)
        e_size.append(len(ret))
        for retslip in ret:
            #print(retslip.split())
            retslip=retslip.split()
            print('\n')
            if retslip[1] not in all_eig_neigh:
                all_eig_neigh.add(retslip[1])
                neigh_wise_eig[retslip[1]]=list()
            interim_dict=dict()
            interim_dict={'e_neigh':retslip[1],'e_interf':retslip[2],'e_hold':retslip[3],'e_uptime':retslip[4],'e_srtt':retslip[5],'e_rto':retslip[6]}
            neigh_wise_eig[interim_dict['e_neigh']].append(interim_dict)
        time.sleep(1)

   
    for e_neigh in all_eig_neigh:
        e_fl1=0
        e_fl2=0
        e_fl3=0
        e_fl4=0
        e_fl5=0
        lneigh=len(neigh_wise_eig[e_neigh])
        last_iter=neigh_wise_eig[e_neigh][lneigh-1]
        last_iter['condition']=''
        for iterate in range (0,lneigh):
            if iterate>0 and e_fl1==0 and neigh_wise_eig[e_neigh][iterate]['e_srtt']!=neigh_wise_eig[e_neigh][iterate-1]['e_srtt']:
                e_fl1=1
                last_iter['condition']+=' srtt value fluctuating. '
            if iterate>0 and e_fl2==0 and neigh_wise_eig[e_neigh][iterate]['e_rto']!=neigh_wise_eig[e_neigh][iterate-1]['e_rto']:
                e_fl2=1
                last_iter['condition']+=' rto value fluctuating. '
            if e_fl4==0 and int(neigh_wise_eig[e_neigh][iterate]['e_srtt'])>1500:
                last_iter['condition']+=' srtt value very high. '
                e_fl4=1
            if e_fl5==0 and int(neigh_wise_eig[e_neigh][iterate]['e_rto'])>4500:
                last_iter['condition']+=' rto value very high. '
                e_fl5=1
            if e_fl3==0 and re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',neigh_wise_eig[e_neigh][iterate]['e_uptime']):
                et1=int(neigh_wise_eig[e_neigh][iterate]['e_uptime'][:2])*60*60+int(neigh_wise_eig[e_neigh][iterate]['e_uptime'][3:5])*60+int(neigh_wise_eig[e_neigh][iterate]['e_uptime'][6:])
                if et1<86400:
                    e_fl3=1
                    last_iter['condition']+=' uptime less than an hour. '
        if last_iter['condition']=='':
            last_iter['condition']='perfect.'
        #dictofobj[nme].gennodedict['eigrp_neigh'][e_neigh]=dict()
        #dictofobj[nme].gennodedict['eigrp_neigh'][e_neigh]=last_iter
    #if e_size[0]>0 and (e_size[0]!=e_size[1] or e_size[1]!=e_size[2]):
        #dictofobj[nme].gennodedict['eigrp_neigh']['Number_of_neigh']='Number of neighbors not constant'
        print(last_iter) 


        '''
ret=ssh.send_command("sh ip route | inc 00:",use_textfsm=True)
nxos_ip_route=dict()
ip_rou_ct=1
#print(ret)
for inter_rou in ret:
    print(inter_rou)
    print('\n')
    nxos_ip_route[ip_rou_ct]=inter_rou
    ip_rou_ct+=1

#dictofobj[nme].gennodedict['ip_route_00']=dict()
#dictofobj[nme].gennodedict['ip_route_00']=ip_rou_ct


















    




















