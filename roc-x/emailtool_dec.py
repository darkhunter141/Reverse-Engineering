import os
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
text=cyan+"\t\tDeveloped By : Sanaur Asif"+green+"\n\n\t\t★★ ROC-X E-Mail Bomber ★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option From Below")
	print(yellow+"\n\n [1] Start E-Mail Bombing\n\n [2] Back to ROC-X")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		text=green+"\n\n\t\t★★★ ROC-X E-Mail Bombing★★★   \n"
		notice=cyan+"\n\t[•] Connecting to the ROC-X Server...."
		os.system('clear')
		header()
		try:
			rocx=smtplib.SMTP('smtp.gmail.com','587')
			rocx.ehlo()
			rocx.starttls()
			os.system('clear')
			notice=green+"\n\t\t[✓] ROC-X Server Connected   "
			header()
			mvalid=1
			while mvalid<2:
				email=str(input(blue+"\n [>] Enter Your Own G-Mail : "+yellow))
				pwd=str(input(blue+"\n [>] Enter Your G-Mail Password : "+yellow))
				os.system('clear')
				text=green+"\n\n\t\t★★★ROC-X E-Mail Bombing★★★   \n" 
				notice=cyan+"\n\t\t[•] Trying to Login...."
				header()
				try:
					rocx.login(email,pwd)
					os.system('clear')
					notice=green+"\n\t\t[✓] Login Successful!"
					header()
					start=1
					while start<2:
						tmail=str(input(blue+"\n\n [>] Enter Your Target E-Mail : "+yellow))
						msg=str(input(blue+"\n [>] Enter Your Message : "+yellow))
						try:
							ammount=int(input(blue+"\n [>] Enter The Ammount : "+yellow))
						except:
							os.system('clear')
							notice=red+"\n [×] Wrong ammount entered. Try Again! "
							header()
							continue
						os.system('clear')
						notice=cyan+"\n\t   [•] ROC-X Tools in progress......\n\n"
						header()
						ammount2=1
						totalsent=0
						totalnotsent=0
						while ammount2<ammount+1:
							try:
								rocx.sendmail(email,tmail,msg)
								if ammount2==1:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+green+"[✓] 1st E-Mail Sent.")
								elif ammount2==2:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+green+"[✓] 2nd E-Mail Sent.")
								elif ammount2==3:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+green+"[✓] 3rd E-Mail Sent.")
								else:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+green+"[✓] "+str(ammount2)+"th E-Mail Sent.")
								time.sleep(1)
								totalsent+=1
								ammount2+=1
							except:
								if ammount2==1:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+red+"[×] 1st E-Mail Not Sent.")
								elif ammount2==2:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+red+"[×] 2nd E-Mail Not Sent.")
								elif ammount2==3:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+red+"[×] 3rd E-Mail Not Sent.")
								else:
									print(cyan+"\n\t  ★★ROC-X★★==>   "+red+"[×] "+str(ammount2)+"th E-Mail Not Sent.")
								try:
									print(blue+"\n\t\t [•] Sleeping 30s. Wait...")
									time.sleep(30)
									rocx=smtplib.SMTP('smtp.gmail.com','587')
									rocx.ehlo()
									rocx.starttls()
									rocx.login(email,pwd)
									ammount2+=1
								except:
									print(blue+"\n\t\t [•] Sleeping 30s. Wait...")
									time.sleep(30)
									ammount2+=1
									
								
						totalhit=ammount2-1
						totalnotsent=totalhit-totalsent
						print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
						print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
						print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
						lastt=str(input(cyan+"\n\n\t\t\t[✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
						os.system('clear')
						notice=""
						text=green+"\n\n\t\t★★★ROC-X E-Mail Tools★★★   \n" 
						header()
						opt()
						start=3
						mvalid=3
						
				except:
					os.system('clear')
					notice=red+"\n [×] Wrong G-Mail or Password! Or \'\'Less Secure App\'\' is not enabled. "
					header()
					print(yellow+"\n  [1] Try Again ! \n\n  [2] Back To E-Mail Tools")
					yti=str(input(blue+"\n\n  [>] Select Your Option : "+yellow))
					if yti=="1":
						os.system('clear')
						notice=""
						header()
						mvalid=1
					else:
						os.system("clear")
						os.system("python3 emailtool.py")
		except:
			os.system('clear')
			notice=red+"\n\t   [×]Check Your Internet Connection"
			header()
			opt()
			continue
			
			
	elif opt2=="2":
		os.system("python3 main2.py")
	else:
		text=green+"\n\n\t\t★★★ROC-X E-Mail Tools★★★   \n" 
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue

