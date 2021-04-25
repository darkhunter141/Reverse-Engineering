import os
import sys
import time
import base64
import marshal
import zlib

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
P = '\033[1;35m'
W = '\033[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 100)

logo = """
\033[1;36m____  _            _    __  __        __ _
\033[1;36m| __ )| | __ _  ___| | _|  \/  | __ _ / _(_) __ _
\033[1;36m|  _ \| |/ _` |/ __| |/ / |\/| |/ _` | |_| |/ _` |
\033[1;36m| |_) | | (_| | (__|   <| |  | | (_| |  _| | (_| |
\033[1;36m|____/|_|\__,_|\___|_|\_\_|  |_|\__,_|_| |_|\__,_|
\033[1;36m ______        \033[1;36m  _______                  _ _        
\033[1;36m(_____ \       \033[1;36m (_______)                (_) |       
\033[1;36m _____) )   _  \033[1;36m  _       ___  ____  ____  _| | _____ 
\033[1;36m|  ____/ | | | \033[1;36m | |     / _ \|    \|  _ \| | || ___ |
\033[1;36m| |    | |_| | \033[1;36m | |____| |_| | | | | |_| | | || ____|
\033[1;36m|_|     \__  | \033[1;36m  \______)___/|_|_|_|  __/|_|\_)_____)
\033[1;36m       (____/  \033[1;36m                    |_|               
\033[1;36m
\033[1;36m               WhatsApp Num     03094161457
"""

banner = """
 \033[1;31m[\033[1;37m01\033[1;31m]\033[1;35m Encrypt Marshal
 \033[1;31m[\033[1;37m02\033[1;31m]\033[1;35m Encrypt Base64
 \033[1;31m[\033[1;37m03\033[1;31m]\033[1;35m Encrypt Marshal\033[1;37m,\033[1;36mBase32
 \033[1;31m[\033[1;37m04\033[1;31m]\033[1;35m Encrypt Zlib\033[1;37m,\033[1;36mBase64
 \033[1;31m[\033[1;37m05\033[1;31m]\033[1;35m Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;36mBase64
 \033[1;31m[\033[1;37m06\033[1;31m]\033[1;35m Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;36mBase32
 \033[1;31m[\033[1;37m07\033[1;31m]\033[1;35m Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;36mBase16
 \033[1;31m[\033[1;37m00\033[1;31m]\033[1;35m Exit
"""

os.system("clear")
print logo
slowprint (banner)

mainmenu = raw_input(R + " Select an option" + C + " > " + Y)

if mainmenu == "1" or mainmenu == "01":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(Y + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (G + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    a = compile(fileopen, 'dg', 'exec')
    m = marshal.dumps(a)
    s = repr(m)
    b = '# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport marshal\nexec(marshal.loads(' + s + '))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "2" or mainmenu == "02":
    print ("")
    slowprint(P + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (P + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    a = base64.b64encode(fileopen)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "3" or mainmenu == "03":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (P + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = base64.b32encode(sb)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "4" or mainmenu == "04":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (P + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    sa = zlib.compress(fileopen)
    sb = base64.b64encode(sa)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "5" or mainmenu == "05":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (G + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b64encode(sc)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print P + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "6" or mainmenu == "06":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(G + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (G + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b32encode(sc)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "7" or mainmenu == "07":
    print ("")
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ("")
    file = raw_input(G + " Name of the File to Encrypt" + C + " > " + Y)
    print ("")
    c = raw_input(P + " Output File Name" + C + " > " + Y)
    print ("")
    slowprint (G + " Encrypting...")
    print ("")
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b16encode(sc)
    b = "# Obfuscated by Py Compile\n# Created by BlackMafia (https://github.com/lovehacker404)\n# WhatsApp : 03094161457\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + " Encryption Completed...")
    time.sleep(3)
    print ("")
    print G + ' Output File Name : ' + Y, c
    print ("")
    print (W)
elif mainmenu == "0" or mainmenu == "00":
    print ("")
    print ("")
    slowprint(Y + "  Thanks for using this tool")
    time.sleep(1)
    print ("")
    print (W)
    sys.exit
else:
   print (W + "")
   print (C + "[" + R + " !" + C + "]" + Y + " Invalid input " + C + "[" + R + "!" + C + "]")
   print (W)

