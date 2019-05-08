import re
a='10:00:00'
if re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$',a):
    print('abc')
    hh=int(a[:2])
    mm=int(a[3:5])
    ss=int(a[6:])
    print(hh*60*60+mm*60+ss)
else:
    print('bca')
