from netmiko import ConnectHandler
import textfsm
import time
ssh= ConnectHandler(device_type="cisco_ios",host="10.9.10.9",username="rit",password="CMSnoc$1234")

def mb(str):
        return round(int(str)/1024/1024,2)
	        

def percent(a,b):
        return round((int(a)/int(b)) * 100,2)

gennodedict = dict()

boo=True
while boo:
	    try:
	            
	        ret = ssh.send_command("show logging | i err|drop|fail|Fail|crash|MALLOCFAIL|down")
	        boo=False
	    except:
	        print("9-5 exception handled in show log. Trying again ")
	        boo=True
	    if not(isinstance(ret,str)):
	        print("9-5  Return from show log in not string. Trying again")
	        boo=True
	    else:
	        boo=False
	            
	    print(ret)
	    array = ret.split('\n')

	    count=0
	    syslog = dict()
	    for line in array:
	        if line.find('%')!=-1:
	            syslog.update({count:line})
	            count+=1
	    gennodedict['log']=syslog
	    print(gennodedict)

	    
