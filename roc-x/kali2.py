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
text=cyan+"\t\tDeveloped By : Sanaur Asif"+green+"\n\n\t\t★★ ROC-X Kali NetHunter★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option From Below")
	print(yellow+"\n\n [1] Download Required Software\n\n [2] Install Kali NetHunter\n\n [3] SetUp Kali NetHunter KeX\n\n [4] Start NetHunter KeX GUI\n\n [5] Back To ROC-X")
header()
print(cyan+"\n\t\t[•] Checking The Requirements")
time.sleep(0.7)
try:
	from google_drive_downloader import GoogleDriveDownloader as gdd
	import requests
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
	os.system("pip install googledrivedownloader && pip install requests")
from google_drive_downloader import GoogleDriveDownloader as gdd
#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		os.system("clear")
		header()
		print(cyan+"\n  The Following APK Files Will Be Downloaded : \n"+yellow+"\n  [1] Hacker\'s KeyBoard\n\n  [2] NetHunter KeX")
		nhopt=str(input(blue+"\n [>] Do You Want to Continue ? [y/n] : "+yellow))
		if nhopt=="y" or nhopt=="Y" or nhopt=="yes" or nhopt=="YES":
			try:
				try:
					os.system("rm -rf /sdcard/Hacker_Keyboard.apk")
				except:
					os.system("rm -rf $HOME/Desktop/Hacker_Keyboard.apk")
			except:
				pass
			try:
				try:
					os.system("rm -rf /sdcard/NetHunter_Kex.apk")
				except:
					os.system("rm -rf $HOME/Desktop/NetHunter_Kex.apk")
			except:
				pass
			print(cyan+"\n\n\t\t [•] Wait Upto 10/15 Minutes\n\n")
			try:
				gdd.download_file_from_google_drive(file_id='1-Xk5Ez-T3WZQAZxISr0xjiep7IhFErO6',dest_path='/sdcard/NetHunter_Kex.apk',unzip=False)
			except:
				gdd.download_file_from_google_drive(file_id='1-Xk5Ez-T3WZQAZxISr0xjiep7IhFErO6',dest_path='$HOME/Desktop/NetHunter_Kex.apk',unzip=False)
			print(cyan)
			try:
				gdd.download_file_from_google_drive(file_id='1-X8WJo3cY7JG9mFYQxrvAE2VwbNOyWzM',dest_path='/sdcard/Hacker_Keyboard.apk',unzip=False)
			except:
				gdd.download_file_from_google_drive(file_id='1-X8WJo3cY7JG9mFYQxrvAE2VwbNOyWzM',dest_path='$HOME/Desktop/Hacker_Keyboard.apk',unzip=False)
			lastt=str(input(cyan+"\n\n\t\t  "+yellow+"[✓] App Downloaded !"+cyan+"\n\n    [1] Now Install 2 Apps From Your Internal Storage\n\n\t\t[2] Press Enter To Continue "))
			os.system("clear")
			os.system("python3 kali.py")
		else:
			os.system("clear")
			os.system("python3 kali.py")

	elif opt2=="2":
		os.system("clear")
		header()
		print(cyan+"\n  Requirements For Installing Kali NetHunter : \n"+yellow+"\n  [1] Android Version 5.0+\n\n  [2] At Least 3 GB Internal Storage\n\n  [3] At Least 2 GB Data\n\n  [4] At Least 30-60 Minutes\n\n"+red+" [!] You will be not able to Quit or Minimize Termux during the Installation. So, Install it at your free time.")
		nhopt=str(input(blue+"\n [>] Do You Want to Continue ? [y/n] : "+yellow))
		if nhopt=="y" or nhopt=="Y" or nhopt=="yes" or nhopt=="YES":
			os.system("clear")
			header()
			print(cyan+"\n [>] It Can Take Up to 30-120 Minutes ! So, Be Patient.\n\n [>] Don't Close or Minimize Termux during Installation\n\n [>] Always Enter \"Y\" If Any Question Raise.\n\n")
			nhop=str(input(blue+"\n [>] Do You Want to Continue ? [y/n] : "+yellow))
			if nhop=="y" or nhopt=="Y" or nhopt=="yes" or nhopt=="YES":
				os.system("clear")
				header()
				print(cyan+"\t\t[>] Installing Kali NetHunter \n\n"+end)
				try:
					print(green)
					os.system("cd $HOME && pkg install wget -y")
					os.system("cd $HOME && wget -O install-nethunter-termux https://offs.ec/2MceZWr")
					print(green)
					os.system("cd $HOME && chmod +x install-nethunter-termux")
					print(green)
					os.system("cd $HOME && ./install-nethunter-termux")
					lastt=str(input(cyan+"\n\n\t\t"+green+"[✓] Installed Successfully!"+cyan+"\n\n\t    [•] Now Press Enter Key To Continue\n"))
					os.system("clear")
					os.system("python3 kali.py")
				except:
					lastt=str(input(cyan+"\n\n\t\t"+red+"[×] An Unknown Error Occurred !"+cyan+"\n\n\t    [•] Now Press Enter Key To Continue\n"))
					os.system("clear")
					os.system("python3 kali.py")
			else:
				os.system("clear")
				os.system("python3 kali.py")
		else:
			os.system("clear")
			os.system("python3 kali.py")
		
	elif opt2=="3":
		os.system("clear")
		header()
		print(cyan+"\n [>] Set A Password and Confirm it for the KeX: \n")
		print(yellow+"\n\t",end="")
		os.system("nh kex passwd")
		lastt=str(input(cyan+"\n\n\t\t"+green+"[✓] Password Set Successful !"+cyan+"\n\n\t    [•] Now Press Enter Key To Continue\n"))
		print(cyan+"\n [>] Set A Password and Confirm it for the KeX as Root : \n")
		os.system("nh -r kex passwd")
		lastt=str(input(cyan+"\n\n\t\t"+green+"[✓] Password Set Successful !"+cyan+"\n\n\t    [•] Now Press Enter Key To Continue\n"))
		ttyyyy=str(input(cyan+"\n\n   [>] Now Install Hacker KeyBoard and Set it as Input Method\n  [>] Now Install & Open The NetHunter KeX .\n  [>] Note The Port From Below (for ex : 5902) \n  [>] Enter the Port & password at NetHunter KeX and Click Connect\n  [>] Then Clear All Minimized App And Restart Termux and Start NetHunter KeX GUI\n  [>] Press Enter After Finished "))
		os.system("clear")
		header()
		os.system("nh kex &")
		a=input()
	elif opt2=="4":
		os.system("clear")
		header()
		print(cyan+"\n\n   [>] Now Install Hacker KeyBoard and Set it as Input Method\n  [>] Now Install & Open The NetHunter KeX .\n  [>] Note The Port From Below (for ex : 5902) \n  [>] Enter the Port & password at NetHunter KeX and Click Connect\n")
		os.system("nh -r kex &")
		a=input()
	elif opt2=="5":
		os.system("clear")
		os.system("python3 main2.py")
	else:
		text=cyan+"\t\tDeveloped By : Sanaur Asif"+green+"\n\n\t\t★★ ROC-X Kali NetHunter★★   \n" 
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue

