import os,sys
os.system("clear")
import smtplib
import time


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
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b                                                      
""")

      
 #HEADER                
text=cyan+"\t\tDeveloped By : Sanaur Asif"+green+"\n\n\t\t★★ ROC-X MetaSploit★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
	

header()
print(cyan+"\n\t\t[•] Checking The Requirements")
time.sleep(0.7)
try:
	import time
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
	os.system("pip install ")


os.system('clear')
header()
print(red+"\n\n  [!] "+red+"NOTE : "+cyan+" You Have To Install Kali NetHunter in order to Run This Service\n  "+red+"[!] "+cyan+"Otherwise, you will get an error while start it.\n\n")
lastly=str(input(blue+"  [>] Have You Installed Kali NetHunter ? [y/n] : "+yellow ))
if lastly=="Y" or lastly=="y" or lastly=="yes" or lastly=="YES":
	os.system("python3 ms.py")
else:
	os.system("python3 main2.py")
