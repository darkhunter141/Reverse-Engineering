# Decompiled By DarkXploit
# Author Team Dark Hunter 141
# Github : https://github.com/darkhunter141
# If If you see this and you copy it, give me credit# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = '\n\n\x1b[1;92m\t\t    _   _______ _____  __\n\x1b[1;93m\t\t   / | / / ___//  _/ |/ /\n\x1b[1;92m\t\t  /  |/ /\\__ \\ / / |   /\n\x1b[1;93m\t\t / /|  /___/ // / /   |\n\x1b[1;92m\t\t/_/ |_//____/___//_/|_|\n\n\x1b[1;91m           OFFICIAL CODER B14CK-KN1GH7 (NAFIS FUAD)\n\n\x1b[1;93m        AUTOMATIC ACCOUNT CRACKER BY \x1b[1;96mNAFIS FUAD\n\n\x1b[1;97m--------------------------------------------------\n\n\x1b[1;95m\n ADMIN      : NAFIS FUAD\n FACEBOOK   : FACEBOOK.COM/NAFIS.FUAD.904\n YOUTUBE    : NFS TECH BD\n GITHUB     : GITHUB.COM/NFS-TECH-BD\n\x1b[1;32m\n\n--------------------------------------------------\n\n                                '
cusr = 'nfs-tech-bd'
cpwd = 'nsix'

def u():
    os.system('clear')
    print logo
    usr = raw_input(' ENTER USERNAME : ')
    if usr == cusr:
        p()
    else:
        os.system('clear')
        print logo
        print ' ENTER USERNAME : ' + usr + ' (wrong)'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/nafis.fuad.904')
        u()


def p():
    os.system('clear')
    print logo
    print ' ENTER USERNAME : nfs-tech-bd (correct)'
    pwd = raw_input(' ENTER PASSWORD : ')
    if pwd == cpwd:
        z()
    else:
        os.system('clear')
        print logo
        print ' ENTER USERNAME : nfs-tech-bd (correct)'
        print ' ENTER PASSWORD : ' + pwd + ' (wrong)'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/nafis.fuad.904')
        p()


def z():
    os.system('clear')
    print logo
    print ' ENTER USERNAME : nfs-tech-bd (correct)'
    print ' ENTER PASSWORD : nsix (correct)'
    print ' \x1b[1;92mLogin Successfull\x1b[0m'
    jalan('\x1b[1;93mPlease Wait 2 Minutes, All Packages Are Chacking.....')
    time.sleep(1)
    os.system('python2 .README.md')


if __name__ == '__main__':
    u()