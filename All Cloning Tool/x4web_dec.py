from os import system as oss
import sys
import time
def logo():
	oss('toilet -f mono12 -F gay "X4WEB"')
logo()
head = """Author : Rakib Hossain

Github : https://www.github.com/teamx4ck

Facebook : X4ck cyber army

Fb page : Team X4CK
"""
print(head)
time.sleep(0.5)
def opt():
	print('[1] Whois Scan')
	print('[2] NSLookup')
	print('[3] Nmap')
	print('[4] Page link dump')
	print('[5] Join Facebook')
	print('[6] More Tools')
	print('[0] Exit')
opt()
print()
opt = int(input('Enter your option : '))
if opt==1:
	oss('clear')
	logo()
	whurl = str(input('Enter domain name : '))
	print('Please wait.....')
	time.sleep(0.5)
	oss('whois '+whurl)
	input('Press enter.....')
	oss('python x4web.py')
elif opt==2:
	oss('clear')
	logo()
	nsurl = str(input('Enter domain name : '))
	oss('nslookup '+nsurl)
	input('Press Enter.....')
	oss('python x4web.py')
elif opt==3:
	oss('clear')
	logo()
	nm = input('Enter ip : ')
	oss('nmap '+ip)
	input('Press enter......')
	oss('python x4web.py')
elif opt==4:
	oss('clear')
	logo()
	pgurl = str(input('Enter url : '))
	oss('lynx -listonly -nonumbers -dump '+pgurl)
	input('Press enter......')
	oss('python x4web.py')
elif opt==5:
	oss('xdg-open https://www.facebook.com/groups/x4ckcyberarmy/?ref=share')
	oss('python x4web.py')
elif opt==6:
	oss('xdg-open https://www.github.com/teamx4ck')
	oss('python x4web.py')
elif opt==0:
	print('Good day..')
	sys.exit()
else:
	print('option not found...!')
	time.sleep(2)
	oss('python x4web.py')
