import json
import time
import paramiko
import textfsm
import re
from collections import defaultdict
from netmiko import ConnectHandler, SSHDetect
ssh= ConnectHandler(device_type='cisco_nxos',host="10.4.10.10",username="rit",password="CMSnoc$1234")
print(ssh.find_prompt())
ret = ssh.send_command("sh proc cpu" ,use_textfsm=True)
#ret1 = ssh .send_command("sh interface counters errors | ex 0")
print(ret)
print(type(ret))
print('\n\n\n\n\n')
#print(ret1.split("\n"))
#print(type(ret1))
