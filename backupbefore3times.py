from flask import Flask, redirect, url_for, request, render_template
import json
import time
import paramiko
import textfsm
import re
from netmiko import ConnectHandler, SSHDetect


app = Flask(__name__)
jinja_options = app.jinja_options.copy()

jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>'
))
app.jinja_options = jinja_options

if __name__ == '__main__' :
	app.run()

class router(object):
	    def __init__(self,name):
	        self.name=name
	        self.entry=set()
	        self.exit=set()
	        self.dictint=dict()
	        self.gennodedict=dict()
	        self.sship=''

	    def addentry(self,ent):
	        self.entry.add(ent)

	    def addconnect(self,conn):
	        self.handle=conn

	    def addsship(self,ipadd):
	        self.sship=ipadd

	    def addexit(self,ext):
	        self.exit.add(ext)

	    def adddictip(self,interf,ip):
	        if interf not in self.dictint.keys():
	            self.dictint[interf]=dict()
	        self.dictint[interf]['ip']=ip

	    def objprint(self):
	        print(" Name "+self.name)
	        print(" Entry interfaces ")
	        print(self.entry)
	        print(" Exit interfaces ")
	        print(self.exit)
	        print(" Interface Dictionary ")
	        print(self.dictint)
	        print()
	        print(" General Node Information ")
	        print(self.gennodedict)
	        
	        print("------------------------------")

def backend(src,dst):
	src=src
	dst=dst	
	        
	arr=[]
	count=0

	setofnames=set()
	dictofnames={}
	dictofobj={}

	name=''
	s={src}
	now=src
	honame=set()
	exit=dict()
	entry=dict()
	entryrev=dict()
	ls=[]
	ls.append(now)
	extract=set()
	p=''
	boo=True
	intojson=[]

	while(len(s)>0):
	    now=ls[0]
	    rem=paramiko.SSHClient()
	    rem.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    boo=True
	    while boo:
	        try:
	            rem.connect(now,port=22, username='rit',password='CMSnoc$1234')
	            boo=False
	            print ("SSH connection established for getting the version - ",now)
	            stdin,stdout,stderr=rem.exec_command("show version")
	        except Exception as e:
	            print("Error in ssh connection, Trying again. Error - ",e) 
	            boo=True
 
   
	    output=stdout.readlines()
	    print(output)
	    output='\n'.join(output)
	    k9=output.replace('\n',' ')
	    print("\n\n\n\n")
	    print(k9)
	    k9=k9.split()
	    print("\n\n\n\n")
	    print(k9)
	    a=k9.index('Cisco')
	    #print(a)
	    #print(k9[a+1])
	    ios_ver=''
	    verdict={}
	    if (k9[a+1]=='IOS'):
	        if (k9[a+2]=='XE'):
	            ios_ver='cisco_xe'
	        else:
	            ios_ver='cisco_ios'
	    else:
	        ios_ver='cisco_nxos'
           
	    print(ios_ver)


	    verdict['soft_ver']=ios_ver

	    if ios_ver=='cisco_nxos':
	        var=k9.index('BIOS:')
	        var3=k9.index('kickstart:')
	        verdict['version']="BIOS: "+k9[var+2]+" Kickstart: "+k9[var3+2]
	        var=k9.index('uptime')
	        var2=k9.index('second(s)')
	        verdict['uptime']=' '.join(k9[var+2:var2+1])
	        var=k9.index('Hardware')
	        verdict['hardware']=' '.join(k9[var+1:var+3])
	        var=k9.index('Reason:')
	        verdict['reload_reason']=k9[var+1]
           
	    elif ios_ver=='cisco_xe':
	        var=k9.index('weeks,')
	        var2=k9.index('minutes')
	        verdict['uptime']=' '.join(k9[var-1:var2+1])
	        var=k9.index('Last')
	        var2=k9.index('This')
	        verdict['reload_reason']=' '.join(k9[var+3:var2])
            
	        var=k9.index('Version')
           
	        verdict['version']=k9[var+1]
         
	        #var=k9.index('Release')
	        #verdict['hardware']=k9[var+4]  
          
               
        
	    else:
        
	        var=k9.index('Version')
	        verdict['version']=' '.join(k9[var+1][:-1])
	        var=k9.index('Software,')
	        verdict['hardware']=k9[var+1]  
	        var=k9.index('uptime')
	        var2=k9.index('minutes')
	        verdict['uptime']=' '.join(k9[var+2:var2+1])            
	        #var=k9.index('reason:')
	        #var2=k9.index('This')
	        #verdict['reload_reason']=' '.join(k9[var+1:var2])

	    print(verdict)
	    rem.close()

	    boo=True
	    while boo:
	        try:
	            #device = {"device_type": "autodetect","host":now,"username": "rit","password":"CMSnoc$1234"}
	            #guesser = SSHDetect(**device)
	            #best_match = guesser.autodetect()
	            #print(best_match,guesser.potential_matches)
    
	            ssh= ConnectHandler(device_type=ios_ver,host=now,username="rit",password="CMSnoc$1234")
	            boo=False
	        except Exception as e:
	            boo=True
	            print(" Connection error, trying again ",e)


	    #ret=ssh.send_command("en")
	    boo=True
	    while boo:
	        try: 
	            name=ssh.find_prompt()
	            boo=False
	        except Exception as e:
	            print(str(e))
	            print("Trying again")
	            boo=True
	        if not(re.match("^[A-Z]{3}-{2}[A-Z]{2}[0-9]{2}#{1}$",name)):
	            boo=True
	            print(" Name Received Incorrect- Trying again "+name)
	    
	    name=name[:-1]


	    if name not in setofnames:
	        setofnames.add(name)
	        dictofnames[name]=count
	        k=router(name)
	        arr.append(k)
	        dictofobj[name]=k
	        dictofobj[name].addconnect(ssh)
	        dictofobj[name].addsship(now)
	        count+=1
	        
	    dictofobj[name].gennodedict['version']=verdict
	    print(name)
	    honame.add(name)
	    print("dict of names ")
	    print(dictofnames)
	    t3=0
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

	    
	    else:
	        
	    
	        boo2=True
	        while boo2:
	    
	            boo=True
	            while boo:
	                try:
	                    ret=ssh.send_command("sh ip route "+dst+" | include Known via")
	                    boo=False
	                except Exception as e:
	                    boo=True
	                    print("1 Exception Handled- Trying again")
	                print(" return from sh ip route | inc known via ")
	                print(ret)
	                if not ret:
	                    print("1 Trying again")
	                    boo=True
	                elif isinstance(ret,list):
	                    print("1 Return from sh ip route is a list, trying again")
	                    boo=True
	                elif len(ret.split())>=3:
	                    boo=False
	                else:
	                    print("1 Trying Again sh ip route")
	                    boo=True
	            print(" Name "+name+" show ip route | i known via")
	            print(ret)
	            ret=ret.split()
	            prot=ret[2][1:]
	            print("PROT- "+prot)
	            if prot!='bgp' and prot !='connected",' and prot!='eigrp':
	                boo2=True
	                print(" Protocol received isn't correct. Trying Again ")
	            else:
	                boo2=False
	            
	    
	    
	    if prot=='bgp':
	        dst1=dst
	        fl=0
	        print("Prot BGP")
	        while fl!=2:
	            boo=True
	            while boo:
	                try:
	                    ret=ssh.send_command("sh ip route "+dst1)
	                    boo=False
	                except:
	                    boo=True
	                    print("2 Exception Handled- Trying again")

	                if not ret:
	                    boo=True
	                    print("2 Trying again")
	                elif isinstance(ret,list):
	                    print("2 Return from sh ip route is a list, trying again")
	                    boo=True
	                elif len(ret.split())>3:
	                    boo=False
	                else:
	                    boo=True
	                    print("2 Trying again")
	            print("\tBGP- sh ip route for dst "+dst1)
	            print(ret)
	            ret=ret.split("\n")
	            fl=0
	            for i in ret:
	                i=i.split()
	                print("splitting ret")
	                print(i)
	                if i[0]=='*':
	                    nxt=i[1]
	                    if nxt=='directly':
	                        x=i.index('via')
	                        hop=i[x+1]
	                        fl=2
	                        break
	                    elif re.match('^(?:[0-9]{1,3}\.){3}([0-9]{1,3})',nxt):
	                        dst1=nxt
	                        if nxt[-1]==',':
	                            dst1=nxt[:-1]

	                        fl=1
	                        break
	        print("Name "+name+" BGP: next hop "+dst1+" exit interface "+hop)
	        extract.add(dst1)
	        s.add(dst1)
	        ls.append(dst1)
	        p=''
	        p=hop+' '+dst1
	        if name not in exit.keys():
	            exit[name]=set()
	        exit[name].add(p)
	        boo=True
	        while boo:
	            try:    
	                ret=ssh.send_command("sh ip int brief | include "+hop)
	                boo=False
	            except:
	                print("3 Exception Handled- Trying again")
	                boo=True
	            if not ret:
	                boo=True
	            elif isinstance(ret,list):
	                print("3 Return from sh ip int brief is a list, trying again")
	                boo=True
	            elif len(ret.split())<6:
	                boo=True
	            else:
	                boo=False
	                
	        ip=ret.split()[1]



	        ctobj=dictofnames[name]
	        arr[ctobj].addexit(p)
	        dictofobj[name].adddictip(hop,ip)
	        



	        p=''
	            
	    elif prot=='connected",':
	        if ios_ver=='cisco_nxos':
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
	            p=''
	            p=exit_int+' directly'
	            if name not in exit.keys():
	                exit[name]=set()
	            exit[name].add(p)
	            print(" Name "+name+" is connected to dst via "+p)

	            ctobj=dictofnames[name]
	            arr[ctobj].addexit(p)
	            dictofobj[name].adddictip(exit_int,exit_int_ip)

	            p=''

	        else:


	            boo=True
	            while boo:
	                try:
	                    ret=ssh.send_command("sh ip route "+dst+" | include directly")
	                    boo=False
	                except:
	                    boo=True
	                    print("4 Exception Handled- Trying again")
	                print(" Return from sh ip route dst i directly")
	                print(ret)
	                if not ret:
	                    boo=True
	                    print("4 Return from show ip route dst is null, Trying again")
	            
	                elif isinstance(ret,list):
	                    print("4 Return from sh ip route directly is a list, trying again")
	                    boo=True
	                elif len(ret.split())>3:
	                    boo=False
	                else:
	                    print("4 Trying again")
	                    boo=True
	        
	            print("Connected route- show ip route| i directly ")
	            print(ret)
	            ret=ret.split()
	            p=''
	            x=ret.index('via')
	            p=ret[x+1]
	            hop=ret[x+1]
	            p=p+' directly'
	            if name not in exit.keys():
	                exit[name]=set()
	            exit[name].add(p)
	            print(" Name "+name+" is connected to dst via "+p)

	            ctobj=dictofnames[name]
	            arr[ctobj].addexit(p)
	            boo=True
	            while boo:
	                try:    
	                    ret=ssh.send_command("sh ip int brief | include "+hop)
	                    boo=False
	                except:
	                    print("5 Exception Handled- Trying again")
	                    boo=True
	                if not ret:
	                    boo=True
	                elif isinstance(ret,list):
	                    print("5 Return from sh ip int brief is a list, trying again")
	                    boo=True
	                elif len(ret.split())<6:
	                    boo=True
	                else:
	                    boo=False
	            
	                
	            ip=ret.split()[1]

	            dictofobj[name].adddictip(hop,ip)

	            p=''
    
	    else:
	        if ios_ver=='cisco_nxos':

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
	                    if next_hop_ip not in extract:
	                        extract.add(next_hop_ip)
	                        s.add(next_hop_ip)
	                        ls.append(next_hop_ip)
	                        p=''  
	                           
	                        p=exit_int+' '+next_hop_ip
	                        if name not in exit.keys():
	                            exit[name]=set()
	              
	                        exit[name].add(p)

	                        ctobj=dictofnames[name]
	                        #print("ctobj "+ctobj)
	                        arr[ctobj].addexit(p)
	                        dictofobj[name].adddictip(exit_int,exit_int_ip)

	                        p=''	                        

	        else:


	            boo=True
	            while boo:
	                try:
	                    ret=ssh.send_command("sh ip route "+dst+" | include via")
	                    boo=False
	                except:
	                    boo=True
	                    print("6 Exception Handled- Trying again")
	                print(" Return from sh ip route")
	                print(ret)
	                if not ret:
	                    boo=True
	                    print("6 Trying again")
	            
	                elif isinstance(ret,list):
	                    print("6 Return from sh ip route is a list, trying again")
	                    boo=True
	                elif len(ret.split())>3:
	                    boo=False
	                else:
	                    print("6 Trying again")
	                    boo=True
	            print("output from sh ip route | inc via ")
	            print(ret)
	            print("Splitting")
	            ret=ret.split('\n')
	            for i in ret:
	                i=i.split()
	                print(i)
	                t=0
	                for j in i:
	                #print(j)
	                    if re.match('^(?:[0-9]{1,3}\.){3}([0-9]{1,3})',j):
	                        print("extract- "+j[:-1])
	                        j=j[:-1]
	                        if j not in extract:
	                            extract.add(j)
	                            s.add(j)
	                            ls.append(j)     
	                        t=1
	               
	                    if t==1:
	                        num=i.index('via')
	                        p=i[num+1]
	                        hop=i[num+1]
	                        p=p+' '+j
	                        if name not in exit.keys():
	                            exit[name]=set()
	              
	                        exit[name].add(p)

	                        ctobj=dictofnames[name]
	                        #print("ctobj "+ctobj)
	                        arr[ctobj].addexit(p)
	                        print("hop ",hop)
	                        boo=True
	                        ret1=""
	                        while boo:
	                            try:    
	                                ret1=ssh.send_command("sh ip int brief | include "+hop)
	                                boo=False
	                            except:
	                                print("6-2 Exception Handled- Trying again")
	                                boo=True
	                            print(" Return ")
	                            print(ret1)
	                            print(len(ret1.split()))
	                            #print(ret1.split()[0])
	                            if not ret1:
	                                boo=True
	                            elif isinstance(ret1,list):
	                                print("6-2 Return from sh ip int brief is a list, trying again")
	                                boo=True
	                            elif len(ret1.split())<5:
	                                boo=True
	                            else:
	                                boo=False
	                    
	                        ip=ret1.split()[1]
	                        dictofobj[name].adddictip(hop,ip)

	                        p=''
	                        break
	    extract.clear()
	    s.remove(now)
	    ls.remove(now)
	 
	    if now!=src:
	        if ios_ver=='cisco_nxos':
    
	            ret=ssh.send_command('sh ip int brief | include '+now)
	            ret=ret.split()
	            entry_int=ret[0]
	            print("entry interface "+entry_int)

	 
	            if name not in entry.keys():
	                entry[name]=set()
	            p=''
	            
	            p=entry_int+' '+now
	            entry[name].add(p)

	            ctobj=dictofnames[name]
	            arr[ctobj].addentry(p)
	            dictofobj[name].adddictip(entry_int,now)
	        

	            entryrev[now]=set()
	            p=''
	            p=name+' '+entry_int
	            entryrev[now].add(p)
	     






	        else:

	            boo=True
	            while boo:
	                try:    
	                    ret=ssh.send_command("sh ip int brief | include "+now)
	                    boo=False
	                except:
	                    print("7  Exception Handled- Trying again")
	                    boo=True
	                print(" return from sh ip int brief | inc dest at dest ")
	                print(ret)
	                print(len(ret.split()))
	                if not ret:
	                    print("7 null")
	                    boo=True
	                elif isinstance(ret,list):
	                    print("7 Return from sh ip route is a list, trying again")
	                    boo=True
	                elif len(ret.split())<6:
	                    boo=True
	                    print("7 Trying Again")
	                else:
	                    boo=False
	            print(" Name "+name+" sh ip int brief | include "+now)
	            print(ret)
	            ret=ret.split()
	 
	            if name not in entry.keys():
	                entry[name]=set()
	            p=''
	            p=ret[0]
	            hop=ret[0]
	            ip=now
	            p=p+' '+now
	            entry[name].add(p)

	            ctobj=dictofnames[name]
	            arr[ctobj].addentry(p)
	            dictofobj[name].adddictip(hop,ip)
	        

	            entryrev[now]=set()
	            p=''
	            p=name+' '+ret[0]
	            entryrev[now].add(p)
	     



	rem=paramiko.SSHClient()
	rem.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	boo=True
	while boo:
	    try:
	        rem.connect(dst,port=22, username='rit',password='CMSnoc$1234')
	        boo=False
	        print ("SSH connection established for getting the version - ",now)
	        stdin,stdout,stderr=rem.exec_command("show version")
	    except Exception as e:
	        print("Error in ssh connection, Trying again. Error - ",e) 
	        boo=True
 
   
	output=stdout.readlines()
	print(output)
	output='\n'.join(output)
	k9=output.replace('\n',' ')
	print("\n\n\n\n")
	print(k9)
	k9=k9.split()
	print("\n\n\n\n")
	print(k9)
	a=k9.index('Cisco')
	#print(a)
	#print(k9[a+1])
	ios_ver=''
	verdict={}
	if (k9[a+1]=='IOS'):
	    if (k9[a+2]=='XE'):
	        ios_ver='cisco_xe'
	    else:
	        ios_ver='cisco_ios'
	else:
	    ios_ver='cisco_nxos'
           
	print(ios_ver)


	verdict['soft_ver']=ios_ver

	if ios_ver=='cisco_nxos':
	    var=k9.index('BIOS:')
	    var3=k9.index('kickstart:')
	    verdict['version']="BIOS: "+k9[var+2]+" Kickstart: "+k9[var3+2]
	    var=k9.index('uptime')
	    var2=k9.index('second(s)')
	    verdict['uptime']=' '.join(k9[var+2:var2+1])
	    var=k9.index('Hardware')
	    verdict['hardware']=' '.join(k9[var+1:var+3])
	    var=k9.index('Reason:')
	    verdict['reload_reason']=k9[var+1]
           
	elif ios_ver=='cisco_xe':
	    var=k9.index('weeks,')
	    var2=k9.index('minutes')
	    verdict['uptime']=' '.join(k9[var-1:var2+1])
	    var=k9.index('Last')
	    var2=k9.index('This')
	    verdict['reload_reason']=' '.join(k9[var+3:var2])
            
	    var=k9.index('Version')
           
	    verdict['version']=k9[var+1]
         
	    #var=k9.index('Release')
	    #verdict['hardware']=k9[var+4]  
          
               
        
	else:
        
	    var=k9.index('Version')
	    verdict['version']=' '.join(k9[var+1][:-1])
	    var=k9.index('Software,')
	    verdict['hardware']=k9[var+1]  
	    var=k9.index('uptime')
	    var2=k9.index('minutes')
	    verdict['uptime']=' '.join(k9[var+2:var2+1])            
	    #var=k9.index('reason:')
	    #var2=k9.index('This')
	    #verdict['reload_reason']=' '.join(k9[var+1:var2])

	    print(verdict)





	
	boo=True
	while boo:
	        try:
	            
	            ssh=ConnectHandler(device_type=ios_ver,host=dst,username="rit",password="CMSnoc$1234")
	            boo=False
	        except Exception as e:
	            boo=True
	            print(" Connection error, trying again ",e,dst)


	boo=True
	while boo:
	    try:
	        name=ssh.find_prompt()
	        boo=False
	    except Exception as e:
	        print(str(e))
	        print("Find Prompt errTrying Again")
	        boo=True
	        
	name=name[:-1]
	honame.add(name)

	if name not in setofnames:
	    setofnames.add(name)
	    dictofnames[name]=count
	    k1=router(name)
	    arr.append(k1)
	    dictofobj[name]=k1
	    dictofobj[name].addconnect(ssh)
	    count+=1

	dictofobj[name].gennodedict['version']=verdict
	
	if ios_ver=='cisco_nxos':
    	
	    ret=ssh.send_command('sh ip int brief | include '+dst)
	    ret=ret.split()
	    print(ret)
	    entry_int_dst=ret[0]
	    print("entry on dest "+entry_int_dst)
	    if name not in entry.keys():
	        entry[name]=set()
	    p=''
	    
	    p=entry_int+' '+'directly'
	    entry[name].add(p)

	    
	    

	    ctobj=dictofnames[name]
	    arr[ctobj].addentry(p)
	    dictofobj[name].adddictip(entry_int,dst)

	    p=''
	    entryrev['directly']=set()
	    p=name+' '+entry_int
	    entryrev['directly'].add(p)

	else:
												
	    boo=True
	    while boo:
	        try:
	            ret=ssh.send_command("sh ip int brief | include "+dst)
	            boo=False
	        except:
	            print("8 Exception Handled- Trying again")
	            boo=True
	        print(" return from sh ip int brief | inc dest ")
	        print(ret)
	        if not ret:
	            boo=True
	        elif isinstance(ret,list):
	            print("8 Return from sh ip int brief is a list, trying again")
	            boo=True
	        elif len(ret.split())<6:
	            boo=True
	            print("8 Trying Again")
	        else:
	            boo=False

	    ret=ret.split()
	    #print(ret)
	    if name not in entry.keys():
	        entry[name]=set()
	    p=''
	    p=ret[0]
	    p=p+' '+'directly'
	    entry[name].add(p)

	    hop=ret[0]
	    ip=dst

	    ctobj=dictofnames[name]
	    arr[ctobj].addentry(p)
	    dictofobj[name].adddictip(hop,ip)

	    p=''
	    entryrev['directly']=set()
	    p=name+' '+ret[0]
	    entryrev['directly'].add(p)

	print("Entry interfaces ")
	print(entry)
	print()
	print(" Exit  interfaces ")
	print(exit)

	print()
	print(" Entry Reverse ")
	print(entryrev)

	ff=0

	#KPIs
	for nme in setofnames:
	    ssh=dictofobj[nme].handle

	    # SHOW PROC CPU	    
	    boo=True
	    while boo:
	        try:
	            ret=ssh.send_command("sh proc cpu | ex 0.0",use_textfsm=True)
	            print(ret)
	            boo=False
	        except:
	            print("9 Exception Raised , Trying again")
	            boo=True
	        if not(isinstance(ret,list)):
	            boo=True
	            print("9 return from sh proc cpu not proper, trying again",nme,ssh.device_type)
	        else:
	            boo=False	            
	    
	    ct1=0
	    for line in ret:
	        if ct1==0:
	            cpu={}
	            cpu['cpu_5_sec']=line['cpu_5_sec']
	            cpu['cpu_1_min']=line['cpu_1_min']
	            cpu['cpu_5_min']=line['cpu_5_min']
	            dictofobj[nme].gennodedict['CPU']=cpu                
	            
	        combine={}
	        combine['process']=line['process']
	        combine['proc_5_sec']=line['proc_5_sec']
	        combine['proc_1_min']=line['proc_1_min']
	        combine['proc_5_min']=line['proc_5_min']
	        dictofobj[nme].gennodedict[line['pid']]=combine      
	        ct1+=1

	    # SHOW IP ROUTE
	    boo=True
	    while boo:
	        try:
	            ret=ssh.send_command("sh ip route")
	            boo=False
	        except:
	            print("10 Exception Raised , Trying again")
	            boo=True
	        print(ret)
	        if not ret:
	            boo=True
	        elif isinstance(ret,list):
	            print("10 Return from sh ip route is a list, trying again")
	            boo=True
	        else:
	            boo=False

	    ret=ret.split('\n')
	    gen={}
	    ct1=0
	    print("RETURN: " ,ret)
	    for line in ret:
	        print("LINE: ",line)
	        line2=line.split()
	        print("Splitted LINE: ",line2)
	        if not(not(line2)) and line2[0]!='S' and line2[0]!='C' and line2[0]!='S*' and 'via' in line2 and line2[0]=='D' and line2[0]=='B':
	            pos=line2.index('via')
	            if line2[pos+2][0:2]=='00':
	                ct1+=1
	                gen[ct1]=line
	                print(line)        
	    dictofobj[nme].gennodedict['ip_route_00']=gen
	                
	    	    
	#-----------------------------------------Harshad------------------------------------------------------------------------------------------
	    
	    # SHOW IP PROTOCOLS
	    boo=True
	    while boo:
	        ans=ans1=0
	        try:
	            ans=ssh.send_command("show ip protocols | include bgp")
	            ans1=ssh.send_command("show ip protocols | include eigrp")
	            boo=False
	        except:
	            print("9-2 Exception raised in sh ip protocols, trying again ")
	            boo=True
	        print(" sh ip protocols | i bgp ")
	        print(ans)
	        print(" sh ip protocols | i eigrp")
	        print(ans1)
	        if not(isinstance(ans,str)) or not(isinstance(ans1,str)):
	            boo=True
	            print("9-2 Return from sh ip protocols not proper. Trying again")
	        elif not ans and not ans1:
	            print("9-2  Return null from both protocols, trying again ")
	            boo=True
	        elif (not(ans1) and len(ans.split())<5) or (not(ans) and len(ans1.split())<5):
	            print(" 9-2-1 Return from sh ip protocols not proper. Trying again")
	            boo=True
	        elif not(not(ans)) and len(ans.split())<5 and not(not(ans1)) and len(ans1.split())<5:
	            print(" 9-2-3 Return from sh ip protocols not proper. Trying again")
	            boo=True
	        else:
	            boo=False
	            
	    
	    bgp=ans.split("\n")
	    eigrp=ans1.split("\n")
	    bgp_sub='"bgp'
	    eigrp_sub='"eigrp'
	    flag1=0
	    flag2=0
	    for text in bgp:
	        if bgp_sub in text:
	            flag1=1
	            break
	    for text in eigrp:
	        if eigrp_sub in text:
	            flag2=1
	            break
	    
	    if flag2==1:
	        print("eigrp there")
	        # SHOW IP EIGRP NEIGHBORS (3)
	        boo=True
	        while boo:
	            try:
	                ans=ssh.send_command("show ip eigrp neighbors")
	                boo=False
	            except:
	                print("9-3 Exception handled. Error in sh ip eigrp neigh. Trying again ")
	                boo=True
	            
	            print(" Return from sh ip eigrp neighbors ")
	            #print(ans)
	            if not ans:
	                print('Null returned from show ip eigrp neighbors')
	                boo=True
	            elif not(isinstance(ans,str)):
	                print('not a string, returned from show ip eigrp neighbors')
	                boo=True
	            elif len(ans.split())<3:
	                print('size less, returned from show ip eigrp neighbors')
	                boo=True
	            else:
	                boo=False
	        boo=True
	        while boo: 
	            try:
	                template=open('cisco_ios_show_ip_eigrp_neighbors.template')
	                res_template=textfsm.TextFSM(template)
	                ans_final=res_template.ParseText(ans)
	                boo=False
	            except Exception as e:
	                print(e)
	                print("9-4 Exception in Textfsm, Trying again")
	                boo=True
	        print(ans_final)
	        hello={}
	        j=0
	        dictofobj[nme].gennodedict['eigrp_neigh']=dict()
	        for i in range(0,len(ans_final)):
	            hello={}
	            hello['neighbor']=ans_final[i][1]
	            hello['uptime']=ans_final[i][4]
	            hello['srtt']=ans_final[i][5]
	            hello['rto']=ans_final[i][6]
	            #dictofobj[nme].gennodedict['eigrp_neigh']
	            dictofobj[nme].gennodedict['eigrp_neigh'][ans_final[i][1]]=dict()
	            dictofobj[nme].gennodedict['eigrp_neigh'][ans_final[i][1]]=hello
	  

	  
	    if flag1==1:
	        print("bgp there")
	        ans=ssh.send_command("show ip bgp summary")
	        print(ans)
	        template=open('cisco_ios_show_ip_bgp_summary.template')
	        res_template=textfsm.TextFSM(template)
	        ans_final=res_template.ParseText(ans)
	        print(ans_final)
	        hello={}
	        j=0
	        dictofobj[nme].gennodedict['bgp_neigh']=dict()
	        for i in range(0,len(ans_final)):
	            hello={}
	            hello['neighbor']=ans_final[i][2]
	            hello['AS']=ans_final[i][3]
	            hello['up/down']=ans_final[i][5]

	            dictofobj[nme].gennodedict['bgp_neigh'][ans_final[i][2]]=dict()
	            dictofobj[nme].gennodedict['bgp_neigh'][ans_final[i][2]]=hello
	            
	            
	        


	#----------------------------------------------------------------------------------------------------------------------------------------------


	#------------------------------------------Neeraj-----------------------------------------------------------------------------------------------



	    boo=True
	    while boo:

	        try:
	            ret = ssh.send_command("show proc mem | include Total")
	            boo=False
	        except:
	            print(" 9-4 Exception handled in sh proc mem | inc Pool Total. Trying Again")
	            boo=True
	        print("Return from show proc mem ")
	        print(ret)
	        if not ret:
	            print(" 9-4 Returned value is null. Trying again ")
	            boo=True
	        elif not(isinstance(ret,str)):
	            boo=True
	            print("9-4 Returned value is not string, trying again ")
	        elif ret.split()[0]!='Processor':
	            print("9-4 Returned value on show proc mem is not proper, trying again")
	        elif len(ret.split())<6:
	            print("9-4 Returned value on show proc mem is not proper, trying again")
	            boo=True
	        else:
	            boo=False
	        

	    def mb(str):
	        return round(int(str)/1024/1024,2)
	        #return 1
	        

	    def percent(a,b):
	        return round((int(a)/int(b)) * 100,2)
	        
	    memory = dict()
	    ret = ret.split('\n')
	    count=0
	    for line in ret:
	        count=count+1
	        if(count>2):
	            break;
	        temp_vals = line.split(' ')
	        vals = []
	        for string in temp_vals:
	            if len(string.strip())>0:
	                vals.append(string)
	        print(vals)
	        memory.update({vals[0]:{'total':mb(vals[3]),'used':mb(vals[5]),'free':mb(vals[7]),'percent':percent(vals[5],vals[3])}})   

	    dictofobj[nme].gennodedict['Process_Memory']=dict()
	    dictofobj[nme].gennodedict['Process_Memory']=memory
	    print(memory)




	    boo=True
	    while boo:
	        
	        try:
	            time1 = ssh.send_command("show clock")
	            boo=False
	        except:
	            print("9-4 Exception handled. sh clock. Trying again")
	            boo=True
	        print("Time ")
	        print(time1)
	        if not time1:
	            boo=True
	            print("9-4 Return from show clock not proper. Trying again ")
	        elif not(isinstance(time1,str)):
	            print("9-4  Return from show clock in not string. Trying again")
	            boo=True
	        elif len(time1.split())<5:
	            print("Time received not proper. Trying again ")
	            boo=True
	        else:
	            boo=False
	    
	    
	    time1=time1.split(" ")[3:5]
	    time1 = time1[0]+" "+time1[1]
	    print(time1)
	    #ret = src.send_command("show log | i down|Down|up|Up|err|fail|Fail|drop|crash|MALLOCFAIL|duplex",time[0]+" "+str((int(time[1])-1)))

	    boo=True
	    while boo:
	        try:
	            
	            ret = ssh.send_command("show log | i down|Down|err|fail|Fail|drop|crash|MALLOCFAIL|")
	            boo=False
	        except:
	            print("9-5 exception handled in show log. Trying again ")
	            boo=True
	        if not(isinstance(ret,str)):
	            print("9-5  Return from show log in not string. Trying again")
	            boo=True
	        else:
	            boo=False
	            
	    array = ret.split('\n')

	    count=0
	    syslog = dict()
	    for line in array:
	        if line.find('%')!=-1 and (line.find("NBRCHANGE")!=-1 or line.find("ADJCHANGE")!=-1 or line.find("UPDOWN")!=-1 or line.find("duplex")!=-1):
	            syslog.update({count:line})
	            count+=1
	    dictofobj[nme].gennodedict['log']=syslog


	#---------------------------------------------------------------------------------------------------------------------------------------
	#---------------------------------------------------ARAVIND-----------------------------------------------------------------------------


	    map_return = {}
	    print("For Spanning Tree KPI")
	    #print(dictofobj[nme].gennodedict['version']['hardware'])
	    output_span=''
	    #if dictofobj[nme].gennodedict['version']['hardware']=='3725':
	    if True:        
	        boo=True
	        while boo:
	            try:
	                output_span= ssh.send_command("sh spanning-tree active")
	                boo=False
	            except:
	                boo=True
	                print("9-6 Exception Raised in show spanning tree")
	            if not output_span:
	                print(" 9-6 Return from show spanning tree is null. Trying again ")
	                boo=True
	            elif not(isinstance(output_span,str)):
	                boo=True
	                print(" 9-6 Return from show spanning tree is not a string. Trying again ")
	                
	            elif len(output_span.split())<4:
	                boo=True
	                print(" 9-6 Return from show spanning tree is not proper. Trying again")
	            else:
	                boo=False
	        
	        l=output_span.split('\n')
	        print("Spanning LIST")
	        print(l)
	        flag = 0
	        p = 12
	        m1={}
	        for k in range(len(l)-6):
	            if (k == p):
	                print(" k ")
	                print(k)
	                print(" p ")
	                print(p)
	                print(l[k])
	                print(l[k + 6])
	                m1[l[k]] = l[k + 6]
	                p += 9
	        p = 12
	        time.sleep(20)
	        for lo in range(0, 2):
	            for k in range(len(l)-6):
	                if (k == p):
	                    print(" k ")
	                    print(k)
	                    print(" p ")
	                    print(p)
	                    # print(l[k])
	                    # print(l[k+6])
	                    if (m1[l[k]] != l[k + 6]):
	                        map_return[l[k]] = l[k + 6]
	                        print(l[k] + "\n" + l[k + 6])
	                        flag = 1
	                    else:
	                        print("No change Observed")
	                        flag = 0
	                    p += 9
	            p = 12
	            time.sleep(20)
	        if (flag == 0):
	            print("No Changes in the Past 1 minute")
	        flag = 0
	        print('\n\n\n')
	    dictofobj[nme].gennodedict['spanning_tree']=map_return








	    print("For show interface counters")
	    #print(dictofobj[nme].gennodedict['version']['hardware'])
	    Int_count={}
	    print(nme," ",dictofobj[nme].gennodedict['version']['soft_ver'])
	    if dictofobj[nme].gennodedict['version']['soft_ver']=='cisco_ios':
	    #if ios_ver=='cisco_ios':	     
	        boo=True
	        while boo:
	            try:
	                command = ssh.send_command("sh int counters error | ex 0")
	                boo=False
	            except:
	                boo=True
	                print("9-7 Exception handled - sh int counters error, Trying again")
	            print("Return from show int counters error")
	            print(command)
	    
	            
	        if not(command):
	            print("Sorry empty")
	        else:           
	            output = command.split('\n')
	            output.pop(0)
	            if (output[1]):
	                for i in output:
	                    print(i + '\n')
	                    Int_count = {i: 5 for i in output}
	            else:
	                print("Sorry Empty")
	        
	    dictofobj[nme].gennodedict['interface_counters_errors']=Int_count
















	#---------------------------------------------------------------------------------------------------------------------------------------------------



	    #interface_level_details
	    for interf in dictofobj[nme].dictint.keys():
	        print(interf+" in loop ")
	        boo=True
	        while boo:
	            try:
	                ret=ssh.send_command("sh interfaces "+interf,use_textfsm=True)
	                boo=False
	            except:
	                print("11 Exception Raised , Trying again")
	                boo=True
	                continue
	            print(ret)
	            if not ret:
	                boo=True
	            elif isinstance(ret,str):
	                print("11 output not in proper form, trying again ")
	                boo=True
	            else:
	                boo=False
	        
	        print(ret)
		#dictofobj[nme].dictint[interf]['crc']=list
	        line={}
	        for line in ret:
	            x=line.keys()
	            if 'crc' in x:
	                dictofobj[nme].dictint[interf]['crc']=line['crc']
	            if 'duplex' in x:
	                dictofobj[nme].dictint[interf]['duplex']=line['duplex']
	            if 'reliability' in x:
	                dictofobj[nme].dictint[interf]['reliability']=line['reliability']
	            if 'txload' in x:
	                dictofobj[nme].dictint[interf]['txload']=line['txload']
	            if 'rxload' in x:
	                dictofobj[nme].dictint[interf]['rxload']=line['rxload']
	            if 'speed' in x:
	                dictofobj[nme].dictint[interf]['speed']=line['speed']
	            if 'collisions' in x:
	                dictofobj[nme].dictint[interf]['collisions']=line['collisions']
	            if 'late_collision' in x:
	                dictofobj[nme].dictint[interf]['late_collision']=line['late_collision']
	            if 'overrun' in x:
	                dictofobj[nme].dictint[interf]['overrun']=line['overrun']
	            if 'interf_reset' in x:
	                dictofobj[nme].dictint[interf]['interf_reset']=line['interf_reset']
	            if 'input_errors' in x:
	                dictofobj[nme].dictint[interf]['input_errors']=line['input_errors']
	            if 'output_errors' in x:
	                dictofobj[nme].dictint[interf]['output_errors']=line['output_errors']
	            if 'frame' in x:
	                dictofobj[nme].dictint[interf]['frame']=line['frame']
	            if 'ignored' in x:
	                dictofobj[nme].dictint[interf]['ignored']=line['ignored']
	            if 'bandwidth' in x:
	                dictofobj[nme].dictint[interf]['bandwidth']=line['bandwidth']
	            if 'ignored' in x:
	                dictofobj[nme].dictint[interf]['output_drops']=line['output_drops']

	    forjson={}
	    forjson['Name']=dict()
	    forjson['Name']['0']=nme
	    forjson['Interface Dictionary']=dict()

	    forjson['Interface Dictionary']=dictofobj[nme].dictint
	    forjson['General Node']=dict()
	    forjson['General Node']=dictofobj[nme].gennodedict
	    intojson.append(forjson)
	    


	    ssh.disconnect()
	        

	#for r in arr:
	#    r.objprint()



	print( "FINAL OUTPUT ")
	print(exit)
	print(entryrev)
	print(intojson)
	return exit,entryrev,intojson



class Response():
	
    def __init__(self,responseList):
	    self.jsons = list()
	    for json in responseList:
	        self.jsons.append(json)
	
	

@app.route('/Topology',methods=['GET','POST'])
def topology():
	if request.method == 'GET':
		return render_template('topology.html')
	elif request.method == 'POST':
		req = request.get_json();
		print(req)
		src = req['src']
		dst = req['dst']

		# call ritesh function
		print("src:",src)
		print("dst:",dst)

		exit,reverse,kpi_json = backend(src,dst);

		temp = []
		for key,value in exit.items():
			value = list(value)
			if len(value)>0 :
				for i in value:
					t = {}
					t["now"] = key
					foo = i.split()
					t["exit"] = foo[0]
					foo2 = list(reverse[foo[1]])
					t["next"] = foo2[0].split()[0]
					t["entry"] = foo2[0].split()[1]
					temp.append(t)
			else:
					t = {}
					t["now"] = key
					foo = value[0].split()
					t["exit"] = foo[0]
					foo2 = list(reverse[foo[1]])
					t["next"] = foo2[0].split()[0]
					t["entry"] = foo2[0].split()[1]
					temp.append(t) 
		responseList = list()
		responseList.append(json.dumps(temp))
		device_json = []
		for device in kpi_json:
			processes = {}
			protocols = {}
			device_health= []
			device["device"] = dict()
			device["device"]["memory"]  =dict()
			device["device"]["log"] = dict()
			device["device"]["version"] = dict()
			device["device"]["interface_counters_errors"] = dict();
			device["CPU"] = dict()
			device["CPU"]["pid"] = dict()
			for key in device["General Node"].keys():
				if (key == "interface_counters_errors"):
					device["device"][key] = device["General Node"][key]
				if (key == "Process_Memory"):
					device["device"]["memory"] = device["General Node"][key]
				if(key == "log"):
					device["device"]["log"] = device["General Node"][key]
				if(key == "version"):
					device["device"]["version"] = device["General Node"][key]
				if (key == "CPU"):
					device["CPU"]["cpu_util"] = device["General Node"][key]
				if key.isdigit():
					processes[key] = device["General Node"][key]
					device["CPU"]["pid"] = processes
				if (key == "eigrp_neigh"):
					protocols["eigrp"] = device["General Node"][key]
				if (key == "bgp_neigh"):
					protocols["bgp"] = device["General Node"][key]
				if (key == "ip_route_00"):
					protocols["ip_route"] = device["General Node"][key]
				if (key == "spanning_tree"):
					protocols["spanning_tree"] = device["General Node"][key]
				device["Protocols"] = protocols
			del device["General Node"]
			device_json.append(device)
		response_list = list()
		response_list.append(temp)
		response_list.append(device_json)
		return json.dumps(response_list)		
		#return json.dumps(Response(responseList).__dict__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.args.get('username')
		password = request.args.get('password')
		# if validated,
		return render_template('topology.html')
	print("Failure")
	return render_template('login.html')






	
