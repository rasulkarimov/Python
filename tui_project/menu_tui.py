#!/usr/bin/python3
import os
import getpass

os.system("tput setaf 1")
print("\t\t\tWelcome to my TIU")
os.system("tput setaf 5")
print("\t\t\t---------------------------")

passwd = getpass.getpass("Enter you password: ")
authpass = "test"
if passwd != authpass:
  print("Password incorrect")
  exit()

print("Where you want to perform you job local/remote")
location = input()

if location == "remote":
        remoteIP = input("Enter you IP: ")
        availprobe = os.system("ping -c3 {}".format(remoteIP))
        if availprobe == 0:
          print("remote system is avail\n")
        else:
            print("remote sys isn't avail")
            exit()
while True:
	print("""Press 1: to see date
	Press 2: to check cal
	Press 3: to cong web server
	Press 4: to create user
	Press 5: create file
	Press 9: to exit""")

	print("Enter your choice:" , end="\n")
	ch = input()

	if location == "local":
		if int(ch) == 1: 
	  		os.system("date")
		elif int(ch) == 2:
	  		os.system("cal")
		elif int(ch) == 3:
  			os.system("yum install httpd -y")
		elif int(ch) == 4:
			print("Enter username:")
			user = input()
			os.system("sudo useradd {}".format(user))
		elif int(ch) == 5:
			os.system("touch testfile")
		elif int(ch) == 9:
			exit()

	elif location == "remote":
		if int(ch) == 1:
			os.system("ssh {} date".format(remoteIP))
		elif int(ch) == 2:
			os.system("ssh {} cal".format(remoteIP))
		elif int(ch) == 3:
			os.system("ssh {} yum install httpd -y".format(remoteIP))
		elif int(ch) == 4:
			print("Enter username:")
			user = input()
			os.system("ssh root@{1} sudo useradd {0}".format(user,remoteIP))
		elif int(ch) == 5:
			os.system("ssh 192.168.0.12 touch testfile")
		elif int(ch) == 9:
			exit()
	input("Enter to continue...")
	os.system("clear")
