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

"""
for key,value in exit.items():
	print(key)
	print(list(value))

"""
temp = []
for key,value in exit.items():
	value = list(value)
	if len(value)>0 :
		for i in value:
			t = {}
			t["this"] = key
			foo = i.split()
			t["exit"] = foo[0]
			foo2 = list(reverse[foo[1]])
			t["next"] = foo2[0].split()[0]
			t["entry"] = foo2[0].split()[1]
			temp.append(t)
	else:
			t = {}
			t["this"] = key
			foo = value[0].split()
			t["exit"] = foo[0]
			foo2 = list(reverse[foo[1]])
			t["next"] = foo2[0].split()[0]
			t["entry"] = foo2[0].split()[1]
			temp.append(t) 

print(temp)