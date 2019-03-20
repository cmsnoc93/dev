src='10.3.9.9'
dst='10.12.18.18'

Entry interfaces 
{'MUM--RC06': {'FastEthernet2/0 10.5.6.6'}, 'MUM--SA18': {'12.18.18 10.11.18.18', 'FastEthernet2/1 directly'}, 'MUM--RC05': {'FastEthernet1/0 10.4.5.5'}, 'CHN--RC04': {'FastEthernet0/0 10.4.10.4'}, 'MUM--SC11': {'FastEthernet0/0 10.5.11.11'}, 'CHN--SC10': {'10.4.10.10 10.9.10.10'}, 'MUM--SC12': {'FastEthernet2/2 10.11.12.12', 'FastEthernet0/0 10.6.12.12'}}

 Exit  interfaces 
{'CHN--SC09': {'FastEthernet2/2 10.9.10.10'}, 'MUM--RC06': {'FastEthernet0/0 10.6.12.12'}, 'MUM--SA18': {'FastEthernet2/1 directly'}, 'MUM--RC05': {'FastEthernet2/0 10.5.6.6', 'FastEthernet0/0 10.5.11.11'}, 'CHN--RC04': {'FastEthernet1/0 10.4.5.5'}, 'MUM--SC11': {'FastEthernet2/2 10.11.12.12', 'FastEthernet2/0 10.11.18.18'}, 'CHN--SC10': {'FastEthernet0/0 10.4.10.4'}, 'MUM--SC12': {'FastEthernet2/1 directly'}}

 Entry Reverse 
{'10.5.6.6': {'MUM--RC06 FastEthernet2/0'}, '10.4.5.5': {'MUM--RC05 FastEthernet1/0'}, '10.9.10.10': {'CHN--SC10 10.4.10.10'}, '10.11.18.18': {'MUM--SA18 12.18.18'}, '10.11.12.12': {'MUM--SC12 FastEthernet2/2'}, '10.4.10.4': {'CHN--RC04 FastEthernet0/0'}, '10.5.11.11': {'MUM--SC11 FastEthernet0/0'}, 'directly': {'MUM--SA18 FastEthernet2/1'}, '10.6.12.12': {'MUM--SC12 FastEthernet0/0'}}
 Name CHN--SC09
 Entry interfaces 
set()
 Exit interfaces 
{'FastEthernet2/2 10.9.10.10'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.9.10.9'}}
------------------------------
 Name CHN--SC10
 Entry interfaces 
{'10.4.10.10 10.9.10.10'}
 Exit interfaces 
{'FastEthernet0/0 10.4.10.4'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': 'YES'}, '10.4.10.10': {'ip': '10.9.10.10'}}
------------------------------
 Name CHN--RC04
 Entry interfaces 
{'FastEthernet0/0 10.4.10.4'}
 Exit interfaces 
{'FastEthernet1/0 10.4.5.5'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.4.10.4'}, 'FastEthernet1/0': {'ip': '10.4.5.4'}}
------------------------------
 Name MUM--RC05
 Entry interfaces 
{'FastEthernet1/0 10.4.5.5'}
 Exit interfaces 
{'FastEthernet2/0 10.5.6.6', 'FastEthernet0/0 10.5.11.11'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.5.11.5'}, 'FastEthernet1/0': {'ip': '10.4.5.5'}, 'FastEthernet2/0': {'ip': '10.5.6.5'}}
------------------------------
 Name MUM--SC11
 Entry interfaces 
{'FastEthernet0/0 10.5.11.11'}
 Exit interfaces 
{'FastEthernet2/2 10.11.12.12', 'FastEthernet2/0 10.11.18.18'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.11.12.11'}, 'FastEthernet0/0': {'ip': '10.5.11.11'}, 'FastEthernet2/0': {'ip': '10.11.18.11'}}
------------------------------
 Name MUM--RC06
 Entry interfaces 
{'FastEthernet2/0 10.5.6.6'}
 Exit interfaces 
{'FastEthernet0/0 10.6.12.12'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.6.12.6'}, 'FastEthernet2/0': {'ip': '10.5.6.6'}}
------------------------------
 Name MUM--SA18
 Entry interfaces 
{'12.18.18 10.11.18.18', 'FastEthernet2/1 directly'}
 Exit interfaces 
{'FastEthernet2/1 directly'}
 Interface Dictionary 
{'FastEthernet2/1': {'ip': '10.12.18.18'}, '12.18.18': {'ip': '10.11.18.18'}}
------------------------------
 Name MUM--SC12
 Entry interfaces 
{'FastEthernet2/2 10.11.12.12', 'FastEthernet0/0 10.6.12.12'}
 Exit interfaces 
{'FastEthernet2/1 directly'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.11.12.12'}, 'FastEthernet2/1': {'ip': '10.12.18.12'}, 'FastEthernet0/0': {'ip': '10.6.12.12'}}
------------------------------




































src='10.2.8.8'
dst='10.12.18.18'

Entry interfaces 
{'MUM--RC06': {'FastEthernet1/0 10.1.6.6'}, 'BGL--RC01': {'FastEthernet0/0 10.1.7.1'}, 'MUM--SA18': {'FastEthernet2/1 directly'}, 'MUM--SC12': {'FastEthernet0/0 10.6.12.12'}, 'BGL--SC07': {'FastEthernet2/2 10.7.8.7'}}

 Exit  interfaces 
{'BGL--RC01': {'FastEthernet1/0 10.1.6.6'}, 'MUM--RC06': {'FastEthernet0/0 10.6.12.12'}, 'BGL--SC08': {'FastEthernet2/2 10.7.8.7'}, 'MUM--SC12': {'FastEthernet2/1 directly'}, 'BGL--SC07': {'FastEthernet0/0 10.1.7.1'}}

 Entry Reverse 
{'10.1.6.6': {'MUM--RC06 FastEthernet1/0'}, '10.1.7.1': {'BGL--RC01 FastEthernet0/0'}, '10.7.8.7': {'BGL--SC07 FastEthernet2/2'}, '10.6.12.12': {'MUM--SC12 FastEthernet0/0'}, 'directly': {'MUM--SA18 FastEthernet2/1'}}
 Name BGL--SC08
 Entry interfaces 
set()
 Exit interfaces 
{'FastEthernet2/2 10.7.8.7'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.7.8.8'}}
------------------------------
 Name BGL--SC07
 Entry interfaces 
{'FastEthernet2/2 10.7.8.7'}
 Exit interfaces 
{'FastEthernet0/0 10.1.7.1'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.1.7.7'}, 'FastEthernet2/2': {'ip': '10.7.8.7'}}
------------------------------
 Name BGL--RC01
 Entry interfaces 
{'FastEthernet0/0 10.1.7.1'}
 Exit interfaces 
{'FastEthernet1/0 10.1.6.6'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.1.7.1'}, 'FastEthernet1/0': {'ip': '10.1.6.1'}}
------------------------------
 Name MUM--RC06
 Entry interfaces 
{'FastEthernet1/0 10.1.6.6'}
 Exit interfaces 
{'FastEthernet0/0 10.6.12.12'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.6.12.6'}, 'FastEthernet1/0': {'ip': '10.1.6.6'}}
------------------------------
 Name MUM--SC12
 Entry interfaces 
{'FastEthernet0/0 10.6.12.12'}
 Exit interfaces 
{'FastEthernet2/1 directly'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.6.12.12'}, 'FastEthernet2/1': {'ip': '10.12.18.12'}}
------------------------------
 Name MUM--SA18
 Entry interfaces 
{'FastEthernet2/1 directly'}
 Exit interfaces 
set()
 Interface Dictionary 
{'FastEthernet2/1': {'ip': '10.12.18.18'}}








src='10.10.16.16'
dst='10.12.18.18'
    
Entry interfaces 
{'MUM--SC12': {'FastEthernet2/2 10.11.12.12', 'FastEthernet0/0 10.6.12.12'}, 'MUM--SA18': {'FastEthernet2/1 directly'}, 'CHN--SC10': {'0 10.10.16.10'}, 'MUM--RC05': {'FastEthernet1/0 10.4.5.5'}, 'CHN--RC04': {'FastEthernet0/0 10.4.10.4'}, 'MUM--SC11': {'FastEthernet0/0 10.5.11.11'}, 'MUM--RC06': {'FastEthernet2/0 10.5.6.6'}}

 Exit  interfaces 
{'MUM--SC12': {'FastEthernet2/1 directly'}, 'CHN--SA16': {'FastEthernet2/1 10.10.16.10'}, 'CHN--SC10': {'FastEthernet0/0 10.4.10.4'}, 'MUM--RC05': {'FastEthernet2/0 10.5.6.6', 'FastEthernet0/0 10.5.11.11'}, 'CHN--RC04': {'FastEthernet1/0 10.4.5.5'}, 'MUM--SC11': {'FastEthernet2/2 10.11.12.12'}, 'MUM--RC06': {'FastEthernet0/0 10.6.12.12'}}

 Entry Reverse 
{'10.4.5.5': {'MUM--RC05 FastEthernet1/0'}, '10.11.12.12': {'MUM--SC12 FastEthernet2/2'}, '10.10.16.10': {'CHN--SC10 0'}, 'directly': {'MUM--SA18 FastEthernet2/1'}, '10.5.11.11': {'MUM--SC11 FastEthernet0/0'}, '10.5.6.6': {'MUM--RC06 FastEthernet2/0'}, '10.6.12.12': {'MUM--SC12 FastEthernet0/0'}, '10.4.10.4': {'CHN--RC04 FastEthernet0/0'}}
 Name CHN--SA16
 Entry interfaces 
set()
 Exit interfaces 
{'FastEthernet2/1 10.10.16.10'}
 Interface Dictionary 
{'FastEthernet2/1': {'ip': 'YES'}}
------------------------------
 Name CHN--SC10
 Entry interfaces 
{'0 10.10.16.10'}
 Exit interfaces 
{'FastEthernet0/0 10.4.10.4'}
 Interface Dictionary 
{'FastEthernet0/0': {'ip': '10.4.10.10'}, '0': {'ip': '10.10.16.10'}}
------------------------------
 Name CHN--RC04
 Entry interfaces 
{'FastEthernet0/0 10.4.10.4'}
 Exit interfaces 
{'FastEthernet1/0 10.4.5.5'}
 Interface Dictionary 
{'FastEthernet1/0': {'ip': '10.4.5.4'}, 'FastEthernet0/0': {'ip': '10.4.10.4'}}
------------------------------
 Name MUM--RC05
 Entry interfaces 
{'FastEthernet1/0 10.4.5.5'}
 Exit interfaces 
{'FastEthernet2/0 10.5.6.6', 'FastEthernet0/0 10.5.11.11'}
 Interface Dictionary 
{'FastEthernet2/0': {'ip': '10.5.6.5'}, 'FastEthernet1/0': {'ip': '10.4.5.5'}, 'FastEthernet0/0': {'ip': '10.5.11.5'}}
------------------------------
 Name MUM--SC11
 Entry interfaces 
{'FastEthernet0/0 10.5.11.11'}
 Exit interfaces 
{'FastEthernet2/2 10.11.12.12'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.11.12.11'}, 'FastEthernet0/0': {'ip': '10.5.11.11'}}
------------------------------
 Name MUM--RC06
 Entry interfaces 
{'FastEthernet2/0 10.5.6.6'}
 Exit interfaces 
{'FastEthernet0/0 10.6.12.12'}
 Interface Dictionary 
{'FastEthernet2/0': {'ip': '10.5.6.6'}, 'FastEthernet0/0': {'ip': '10.6.12.6'}}
------------------------------
 Name MUM--SC12
 Entry interfaces 
{'FastEthernet2/2 10.11.12.12', 'FastEthernet0/0 10.6.12.12'}
 Exit interfaces 
{'FastEthernet2/1 directly'}
 Interface Dictionary 
{'FastEthernet2/2': {'ip': '10.11.12.12'}, 'FastEthernet0/0': {'ip': '10.6.12.12'}, 'FastEthernet2/1': {'ip': '10.12.18.12'}}
------------------------------
 Name MUM--SA18
 Entry interfaces 
{'FastEthernet2/1 directly'}
 Exit interfaces 
set()
 Interface Dictionary 
{'FastEthernet2/1': {'ip': '10.12.18.18'}}






import re
from netmiko import ConnectHandler

#src=input(" Enter Source ")
#dst=input(" Enter destination ")
src='10.10.16.16'
dst='10.12.18.18'

class router(object):
    def __init__(self,name):
        self.name=name
        self.entry=set()
        self.exit=set()
        self.dictint=dict()

    def addentry(self,ent):
        self.entry.add(ent)

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
        print("------------------------------")
        
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
while(len(s)>0):
    now=ls[0]
    boo=True
    while boo:
        try:
            ssh=ConnectHandler(device_type="cisco_ios",host=now,username="rit",password="pan")
            boo=False
        except:
            boo=True
            print(" Connection error, trying again ")


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
        count+=1
        
    
    print(name)
    honame.add(name)
    print("dict of names ")
    print(dictofnames)
    boo=True
    while boo:
        try:
            ret=ssh.send_command("sh ip route "+dst+" | include Known via")
            boo=False
        except Exception as e:
            boo=True
            print(" Exception Handled- Trying again")
        print(" return from sh ip route | inc known via ")
        print(ret)
        if not ret:
            print("Trying again")
            boo=True
        elif len(ret.split())>=3:
            boo=False
        else:
            print("Trying Again sh ip route")
            boo=True
    print(" Name "+name+" show ip route | i known via")
    print(ret)
    ret=ret.split()
    prot=ret[2][1:]
    print("PROT- "+prot)
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
                    print(" Exception Handled- Trying again")

                if not ret:
                    boo=True
                    print("Trying again")
                elif len(ret.split("\n"))>1:
                    boo=False
                else:
                    boo=True
                    print("Trying again")
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
                print(" Exception Handled- Trying again")
                boo=True
            if not ret:
                boo=True
            elif len(ret.split())<3:
                boo=True
                
        ip=ret.split()[1]



        ctobj=dictofnames[name]
        arr[ctobj].addexit(p)
        dictofobj[name].adddictip(hop,ip)
        



        p=''
            
    elif prot=='connected",':
        boo=True
        while boo:
            try:
                ret=ssh.send_command("sh ip route "+dst+" | include directly")
                boo=False
            except:
                boo=True
                print(" Exception Handled- Trying again")

            if not ret:
                boo=True
                print("Trying again")
            elif len(ret.split())>3:
                boo=False
            else:
                print("Trying again")
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
                print(" Exception Handled- Trying again")
                boo=True
            if not ret:
                boo=True
            elif len(ret.split())<3:
                boo=True
                
        ip=ret.split()[1]

        dictofobj[name].adddictip(hop,ip)

        p=''

    else:
        boo=True
        while boo:
            try:
                ret=ssh.send_command("sh ip route "+dst+" | include via")
                boo=False
            except:
                boo=True
                print(" Exception Handled- Trying again")

            if not ret:
                boo=True
                print("Trying again")
            elif len(ret.split('\n'))>1:
                boo=False
            else:
                print("Trying again")
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
                            print(" Exception Handled- Trying again")
                            boo=True
                        print(" Return ")
                        print(ret1)
                        if not ret1:
                            boo=True
                        elif len(ret1.split())<3:
                            boo=True
                
                    ip=ret1.split()[1]
                    dictofobj[name].adddictip(hop,ip)

                    p=''
                    break
    extract.clear()
    s.remove(now)
    ls.remove(now)
 
    if now!=src:
        boo=True
        while boo:
            try:    
                ret=ssh.send_command("sh ip int brief | include "+now)
                boo=False
            except:
                print(" Exception Handled- Trying again")
                boo=True
            print(" return from sh ip int brief | inc dest at dest ")
            print(ret)
            if len(ret.split())>2:
                boo=False
            else:
                print("Trying Again")
                boo=True
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
     
boo=True
while boo:
        try:
            ssh=ConnectHandler(device_type="cisco_ios",host=dst,username="rit",password="pan")
            boo=False
        except:
            boo=True
            print(" Connection error, trying again ")



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
    count+=1


boo=True
while boo:
    try:
        ret=ssh.send_command("sh ip int brief | include "+dst)
        boo=False
    except:
        print(" Exception Handled- Trying again")
        boo=True
    print(" return from sh ip int brief | inc dest ")
    print(ret)
    if not ret:
        boo=True
    elif len(ret.split())>2:
        boo=False
    else:
        print("Trying Again")
        boo=True

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


for i in arr:
    i.objprint()








