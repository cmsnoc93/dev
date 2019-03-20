from flask import Flask, redirect, url_for, request, render_template
import json

app = Flask(__name__)
if __name__ == '__main__' :
	app.run()


src=""
dst=""
	

#Entry interfaces 
entry = {'CHN--RC03': {'FastEthernet1/0 10.2.3.3'}, 
         'BGL--SC08': {'FastEthernet2/0 10.8.13.8'}, 
         'CHN--SC09': {'FastEthernet0/0 10.3.9.9'}, 
         'CHN--SA16': {'FastEthernet2/0 10.9.16.16'}, 
         'BGL--RC02': {'FastEthernet0/0 10.2.8.2'}, 
         'CHN--SC10': {'FastEthernet2/2 10.9.10.10', 'FastEthernet2/1 directly', 'FastEthernet0/0 10.4.10.10'}, 
         'CHN--RC04': {'FastEthernet2/0 10.3.4.4'}}

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
		   '10.2.8.2': {'BGL--RC02 FastEthernet0/0'}}

# AJAX RESPONSE FORMAT
""" {[ {"this":"CHN--RC03", "exit":"fa2/0", "next":"CHN--RC04", entry:"fa2/0"},
	   {"this":"CHN--RC03", "exit":"fa0/0", "next":"CHN-SC09", entry:"fa0/0"},
    ]} """



@app.route('/Topology',methods=['GET','POST'])
def topology():
	if request.method == 'GET':
		src = request.args.get('src')
		dst = request.args.get('dst')

		# call ritesh function
		print("src:",src)
		print("dst:",dst)

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

		print(temp)
		return render_template('topology.html',response=json.dumps(temp))




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






	
