from flask import Flask, redirect, url_for, request, render_template
import json

app = Flask(__name__)
if __name__ == '__main__' :
	app.run()

src=""
dst=""
"""	
#Exit  interfaces 
exit = {'CHN--RC03': {'FastEthernet2/0 10.3.4.4', 'FastEthernet0/0 10.3.9.9'}, 
		'CHN--SC10': {'FastEthernet2/1 directly'}, 
		'CHN--SC09': {'FastEthernet2/2 10.9.10.10', 'FastEthernet2/0 10.9.16.16'}, 
		'CHN--SA16': {'FastEthernet2/1 directly'}, 
		'BGL--RC02': {'FastEthernet1/0 10.2.3.3'},
	    'BGL--SA13': {'FastEthernet2/0 10.8.13.8'},
	    'BGL--SC08': {'FastEthernet0/0 10.2.8.2'}, 
	    'CHN--RC04': {'FastEthernet0/0 10.4.10.10'}}

#Entry Reverse 
reverse = {'10.2.3.3': {'CHN--RC03 FastEthernet1/0'}, 
		   'directly': {'CHN--SC10 FastEthernet2/1'}, 
		   '10.9.10.10': {'CHN--SC10 FastEthernet2/2'},
		   '10.9.16.16': {'CHN--SA16 FastEthernet2/0'},
		   '10.3.9.9': {'CHN--SC09 FastEthernet0/0'},
		   '10.8.13.8': {'BGL--SC08 FastEthernet2/0'},
		   '10.4.10.10': {'CHN--SC10 FastEthernet0/0'},
		   '10.3.4.4': {'CHN--RC04 FastEthernet2/0'},
		   '10.2.8.2': {'BGL--RC02 FastEthernet0/0'}}"""
 

exit={'BGL--SA14': {'FastEthernet2/0 10.7.14.7'}, 'BGL--SC07': {'FastEthernet0/0 directly'}}
reverse={'directly': {'BGL--RC01 FastEthernet0/0'}, '10.7.14.7': {'BGL--SC07 FastEthernet2/0'}}


# AJAX RESPONSE FORMAT
""" {[ {"this":"CHN--RC03", "exit":"fa2/0", "next":"CHN--RC04", entry:"fa2/0"},
	   {"this":"CHN--RC03", "exit":"fa0/0", "next":"CHN-SC09", entry:"fa0/0"},
    ]} """

# AJAX OBJECT RESPONSE FORMAT 
objs = {"CHN--RC03":{'interfaces':{'FastEthernet0/0':{ 'ip' : '10.1.2.1','counters':'ok','duplex':'full'},
							  'FastEthernet0/1':{ 'ip' : '10.1.3.1','errors':'','duplex':''},
							  'FastEthernet0/3':{ 'ip' : '10.1.6.1','errors':'','duplex':''}},
				'device'  :{'cpu':'','ram':''},
				'protocol'	:{'k':'v'},
				'qos'		:{'k':'v'}
			 },
 "CHN-RC04": {},
 "BGL--RC02":{}} 

kpijson = [{'General Node': {'100': {'proc_5_sec': '0.24', 'proc_5_min': '0.28', 'proc_1_min': '0.28', 'process': 'Spanning Tree    '}, 'cpu': {'cpu_5_sec': '1', 'cpu_5_min': '2', 'cpu_1_min': '3'}, '87': {'proc_5_sec': '0.16', 'proc_5_min': '0.18', 'proc_1_min': '0.20', 'process': 'IP ARP Retry Age '}, 'ip_route_00': {1: 'D       1.1.1.1 [90/412160] via 10.7.14.7, 00:57:32, FastEthernet2/0', 2: 'D       2.2.2.2 [90/412160] via 10.8.14.8, 00:57:24, FastEthernet2/1', 3: 'D EX    33.33.33.33 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 4: 'D EX    3.3.3.3 [170/286720] via 10.8.14.8, 00:57:24, FastEthernet2/1', 5: 'D EX    4.4.4.4 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 6: '                [170/25628416] via 10.7.14.7, 00:57:24, FastEthernet2/0', 7: 'D EX    55.55.55.55 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 8: 'D EX    5.5.5.5 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 9: '                [170/25628416] via 10.7.14.7, 00:57:24, FastEthernet2/0', 10: 'D EX    6.6.6.6 [170/286720] via 10.7.14.7, 00:57:32, FastEthernet2/0', 11: 'D EX    22.22.22.22 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 12: 'D       10.7.13.0 [90/30720] via 10.7.14.7, 00:57:32, FastEthernet2/0', 13: 'D EX    10.6.12.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 14: 'D EX    10.3.9.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 15: 'D       10.2.8.0 [90/284160] via 10.8.14.8, 00:57:32, FastEthernet2/1', 16: 'D EX    10.5.11.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 17: 'D EX    10.4.10.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 18: 'D       10.7.8.0 [90/30720] via 10.8.14.8, 00:57:32, FastEthernet2/1', 19: '                 [90/30720] via 10.7.14.7, 00:57:32, FastEthernet2/0', 20: 'D EX    10.9.10.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 21: 'D EX    10.5.6.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 22: 'D       10.1.2.0 [90/286720] via 10.8.14.8, 00:57:24, FastEthernet2/1', 23: '                 [90/286720] via 10.7.14.7, 00:57:24, FastEthernet2/0', 24: 'D EX    10.4.5.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 25: 'D EX    10.2.3.0 [170/25628416] via 10.8.14.8, 00:50:12, FastEthernet2/1', 26: 'D EX    10.9.15.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 27: 'D       10.1.7.0 [90/284160] via 10.7.14.7, 00:57:32, FastEthernet2/0', 28: 'D EX    10.11.12.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 29: 'D EX    10.3.4.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 30: 'D EX    10.1.6.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 31: 'D EX    10.10.15.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 32: 'D       10.8.13.0 [90/30720] via 10.8.14.8, 00:57:32, FastEthernet2/1', 33: 'D EX    10.11.17.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 34: 'D EX    10.10.16.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 35: 'D EX    10.11.18.0 [170/25628416] via 10.7.14.7, 00:57:32, FastEthernet2/0', 36: 'D EX    10.9.16.0 [170/25628416] via 10.8.14.8, 00:57:24, FastEthernet2/1', 37: 'D       10.13.19.0 [90/33280] via 10.8.14.8, 00:57:32, FastEthernet2/1', 38: '                   [90/33280] via 10.7.14.7, 00:57:32, FastEthernet2/0', 39: 'D EX    10.12.18.0 [170/25628416] via 10.7.14.7, 00:57:31, FastEthernet2/0', 40: 'D EX    10.12.17.0 [170/25628416] via 10.7.14.7, 00:57:31, FastEthernet2/0'}, '47': {'proc_5_sec': '0.24', 'proc_5_min': '0.21', 'proc_1_min': '0.19', 'process': 'Compute load avg '}}, 'Interface Dictionary': {'FastEthernet2/0': {'rxload': '1/255', 'output_drops': '89', 'duplex': '', 'late_collision': '0', 'collisions': '0', 'speed': '', 'reliability': '255/255', 'bandwidth': '100000 Kbit', 'input_errors': '0', 'txload': '1/255', 'output_errors': '0', 'ignored': '0', 'interf_reset': '4', 'frame': '0', 'crc': '0', 'ip': '10.7.14.14', 'overrun': '0'}}, 'Name': {'0': 'BGL--SA14'}}, {'General Node': {'cpu': {'cpu_5_sec': '0', 'cpu_5_min': '2', 'cpu_1_min': '4'}, '87': {'proc_5_sec': '0.16', 'proc_5_min': '0.18', 'proc_1_min': '0.20', 'process': 'IP ARP Retry Age '}, '83': {'proc_5_sec': '0.16', 'proc_5_min': '0.22', 'proc_1_min': '0.22', 'process': 'ACCT Periodic Pr '}, 'ip_route_00': {1: 'D EX    10.2.3.0 [170/25628416] via 10.7.8.8, 00:56:01, FastEthernet2/2'}}, 'Interface Dictionary': {'FastEthernet0/0': {'rxload': '1/255', 'output_drops': '0', 'duplex': 'Half-duplex', 'late_collision': '0', 'collisions': '0', 'speed': '10Mb/s', 'reliability': '255/255', 'bandwidth': '10000 Kbit', 'input_errors': '0', 'txload': '1/255', 'output_errors': '0', 'ignored': '0', 'interf_reset': '6', 'frame': '0', 'crc': '0', 'ip': '10.1.7.7', 'overrun': '0'}, 'FastEthernet2/0': {'rxload': '1/255', 'output_drops': '0', 'duplex': '', 'late_collision': '0', 'collisions': '0', 'speed': '', 'reliability': '255/255', 'bandwidth': '100000 Kbit', 'input_errors': '0', 'txload': '1/255', 'output_errors': '0', 'ignored': '0', 'interf_reset': '4', 'frame': '0', 'crc': '0', 'ip': '10.7.14.7', 'overrun': '0'}}, 'Name': {'0': 'BGL--SC07'}}, {'General Node': {'139': {'proc_5_sec': '0.95', 'proc_5_min': '0.94', 'proc_1_min': '0.94', 'process': 'HQF Shaper Backg '}, 'cpu': {'cpu_5_sec': '1', 'cpu_5_min': '2', 'cpu_1_min': '2'}, '41': {'proc_5_sec': '0.31', 'proc_5_min': '0.39', 'proc_1_min': '0.37', 'process': 'Per-Second Jobs  '}, 'ip_route_00': {}}, 'Interface Dictionary': {'FastEthernet0/0': {'rxload': '1/255', 'output_drops': '0', 'duplex': 'Half-duplex', 'late_collision': '0', 'collisions': '0', 'speed': '100Mb/s', 'reliability': '255/255', 'bandwidth': '100000 Kbit', 'input_errors': '0', 'txload': '1/255', 'output_errors': '0', 'ignored': '0', 'interf_reset': '0', 'frame': '0', 'crc': '0', 'ip': '10.1.7.1', 'overrun': '0'}}, 'Name': {'0': 'BGL--RC01'}}] 



class Response():
	
    def __init__(self,responseList):
	    self.jsons = list()
	    for json in responseList:
	        self.jsons.append(json)
	
	

@app.route('/Topology',methods=['GET','POST'])
def topology():
	if request.method == 'GET':
		src = request.args.get('src')
		dst = request.args.get('dst')

		# call ritesh function
		print("src:",src)
		print("dst:",dst)

		#entry,exit,objs = rit(src,dst);

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
		responseList.append(json.dumps(kpijson))


		return render_template('topology.html',response=json.dumps(Response(responseList).__dict__))

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






	
