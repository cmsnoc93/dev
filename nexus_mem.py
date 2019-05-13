from netmiko import ConnectHandler
import textfsm
import time
ssh= ConnectHandler(device_type="cisco_ios",host="10.9.10.10",username="rit",password="CMSnoc$1234")

def mb(str):
        return round(int(str)/1024/1024,2)
	        

def percent(a,b):
        return round((int(a)/int(b)) * 100,2)

boo=True
while boo:
	    try:
	        ret = ssh.send_command("show proc mem shared | include totals")
	        boo=False
	    except:
	        print(" 9-4 Exception handled in sh proc mem | inc Pool Total. Trying Again")
	        boo=True
	    print("Return from show proc mem ")
	    #print(ret)
	    if not ret:
	        print(" 9-4 Returned value is null. Trying again ")
	        boo=True
	    elif not(isinstance(ret,str)):
	        boo=True
	        print("9-4 Returned value is not string, trying again ")
	    else:
	        boo=False
	        


	        
	    memory = dict()
	    ret = ret.split('\n')
	    for line in ret:
	        temp_vals = line.split(' ')
	        vals = []
	        for string in temp_vals:
	            if len(string.strip())>0:
	                vals.append(string)
	        print(vals)  
	        memory.update({"Total":{'total':int(vals[5]),'used':int(vals[8]),'free':int(vals[11]),'percent':percent(vals[8],vals[5])}})
	        print(memory)
	        break;


	    
