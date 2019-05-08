from netmiko import ConnectHandler
import textfsm
import time
ssh= ConnectHandler(device_type="cisco_ios",host="10.7.14.14",username="rit",password="CMSnoc$1234")

# SHOW IP EIGRP NEIGHBORS (3)
gennodedict=dict()
gennodedict['eigrp_neigh']=dict()
for iter in range(3):
	boo=True
	while boo:
		try:
			ans=ssh.send_command("show ip eigrp neighbors")
			boo=False
		except:
			print("9-3 Exception handled. Error in sh ip eigrp neigh. Trying again ")
			boo=True
         
		print(" Return from sh ip eigrp neighbors ")
		print(ans)
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
		print("\n TEXTFSM LIST:\n")	
		print(ans_final)
		hello={}
		j=0
		for i in range(0,len(ans_final)):
			hello={}
			neigh = hello['neighbor']=ans_final[i][1]
			hello['uptime'] = list()
			hello['uptime'].append(ans_final[i][4])
			hello['hold'] = list()
			hello['hold'].append(ans_final[i][3])
			hello['srtt'] = list()
			hello['srtt'].append(ans_final[i][5])
			hello['rto'] = list()

			hello['rto'].append(ans_final[i][6])
			hello['iteration'] = list()
			hello['iteration'].append(iter)
			if neigh in gennodedict['eigrp_neigh']:
				gennodedict['eigrp_neigh'][neigh]['iteration'].append(iter)
				gennodedict['eigrp_neigh'][neigh]['hold'].append(ans_final[i][3])
				gennodedict['eigrp_neigh'][neigh]['uptime'].append(ans_final[i][4])
				gennodedict['eigrp_neigh'][neigh]['srtt'].append(ans_final[i][5])
				gennodedict['eigrp_neigh'][neigh]['rto'].append(ans_final[i][6])
				gennodedict['eigrp_neigh'][neigh]['uptime']=hello['uptime']
				
			else:
				gennodedict['eigrp_neigh'][neigh]=dict()
				gennodedict['eigrp_neigh'][neigh]=hello
	time.sleep(1)
print("\nFINAL DICT:\n")	
print(gennodedict)
