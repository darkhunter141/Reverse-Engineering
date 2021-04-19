# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
logo = '\n\x1b[1;96m ------------------------\n \x1b[1;32m < OFFICIAL CODER MEHEDI >\n \x1b[1;96m ------------------------\n\n\x1b[1;91m ____   ____ _______ ____  _        ____          ____          \n\x1b[1;92m|  _ \\ / __ \\__   __/ __ \\| |      |  _ \\   /\\   |  _ \\   /\\    \n\x1b[1;91m| |_) | |  | | | | | |  | | |      | |_) | /  \\  | |_) | /  \\   \n\x1b[1;92m|  _ <| |  | | | | | |  | | |      |  _ < / /\\ \\ |  _ < / /\\ \\  \n\x1b[1;91m| |_) | |__| | | | | |__| | |____  | |_) / ____ \\| |_) / ____ \\ \n\x1b[1;92m|____/ \\____/  |_|  \\____/|______| |____/_/    \\_\\____/_/    \\_\n\x1b[1;95m\n--------------------------------------------------\n\x1b[1;96m             AUTHOR  : MEHEDI HASAN ARIYAN \n             YOUTUBE : MASTER TRICK \n             GITHUB  : BOTOL MEHEDI \n\x1b[1;92m--------------------------------------------------\n                                               '
CorrectUsername = 'botol'
CorrectPassword = 'botol'
loop = 'true'
while loop == 'true':
    print logo
    username = raw_input(' TOOL USERNAME: ')
    if username == CorrectUsername:
        password = raw_input(' TOOL PASSWORD: ')
        if password == CorrectPassword:
            print ' Logged in successfully as ' + username
            time.sleep(1)
            loop = 'false'
        else:
            print ' Wrong Password !'
            os.system('xdg-open https://youtube.com/MasterTrick1')
            os.system('clear')
    else:
        print ' Wrong Username !'
        os.system('xdg-open https://facebook.com/TheMehtan')
        os.system('clear')

def tik():
    titik = [
     '.', '..', '...', '.', '..', '...']
    for o in titik:
        print '\r[+] Loging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


def login():
    os.system('clear')
    try:
        toket = open('....', 'r')
        os.system('python2 .README.md')
    except (KeyError, IOError):
        os.system('rm -rf ....')
        os.system('clear')
        print logo
        print '[1] Login With Email/Number and Password'
        print '[2] Login With Access Token'
        print 50 * '-'
        login_choice()


def login_choice():
    bch = raw_input('\n ====>  ')
    if bch == '':
        print '[!] Fill in correctly'
        login()
    elif bch == '2':
        os.system('clear')
        print logo
        fac = raw_input(' Paste Access Token Here: ')
        tik()
        fout = open('....', 'w')
        fout.write(fac)
        fout.close()
        print '[+]\x1b[1;92m Login successfull \x1b[1;97m'
        time.sleep(1)
        os.system('xdg-open http://mastertrick.design')
        os.system('python2 .README.md')
    elif bch == '1':
        login1()


def login1():
    os.system('clear')
    try:
        tb = open('....', 'r')
        os.system('python2 .README.md')
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '           LOGIN WITH FACEBOOK '
        print
        iid = raw_input('[+] Number/Email: ')
        id = iid.replace(' ', '')
        pwd = getpass.getpass('[+] Password : ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('....', 'w')
            st.write(z['access_token'])
            st.close()
            print '[+]\x1b[1;92m Login successfull \x1b[1;97m'
            time.sleep(1)
            os.system('xdg-open https://www.facebook.com/groups/231747098048450')
            os.system('clear')
            os.system('python2 .README.md')
        elif 'www.facebook.com' in z['error_msg']:
            print 'Account has a checkpoint !'
            time.sleep(1)
            login1()
        else:
            print 'number/user id/ password is wrong !'
            time.sleep(1)
            login1()


if __name__ == '__main__':
    login()