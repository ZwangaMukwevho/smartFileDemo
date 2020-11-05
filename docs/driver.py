import os
import subprocess
import fileManager
import time
import fileTransfer
import admin

FM = fileManager.fileManager()
FT = fileTransfer.fileTransfer()
AD = admin.admin()

class runner:
	
	def welcome():
		"""Functions that automatically desplays hello that is generated in ASCii
		"""
		os.system('clear')
		print("            _________                               _____     ")
		print("|        | |            |           |             /       \   ")
		print("|        | |            |           |            /         \  ")
		print("|--------| | --------   |           |           |           | ")
		print("|        | |            |           |            \         / ")
		print("|        | |_________   |_________  |_________    \ _____ /  ")
		print("")
		print("-------------------------------------------------------------")
		print("")
	
		

	def mainMenu():
		"""This is the function that creates deals with interaction with the user, It uses the functions from the other utilities file. (FileTransfer.py and FileManager.py)
		"""
		option = input("Select an option: D - Download | S - Search | E - delete | T - Transfer file | Q - Quit\n")
		option = option.upper()

		if option == "D":

			option2 = input("Press 1 the link is from a website that requires logging in, press 2 if the website does not require user logging in - Quit\n\n")

			if option2 == "2":
				downloadLink = input("Please enter download link: \n")
			
				# Downloading the file using fileManager class
				uList =FM.splitUrl(downloadLink) 
				if uList == 'invalid URL given':
					print("invalid download link given\n")
				else:
					name = FM.obtainName(uList)
					typ = FM.obtainType(uList) 
					output = FM.donwloadFile(downloadLink,name,typ )
					print("download successful :-) \n")
				
				print("")
				time.sleep(1)
			
			elif option2 == "1":
				name = input("Enter your username: \n")
				password = input("Enter your password: \n")
				downloadLink = input("Enter the link to the file to be downloaded: \n")

				# Downloading the file using fileManager class
				uList =FM.splitUrl(downloadLink) 
				fileName = FM.obtainName(uList)
				typ = FM.obtainType(uList) 
				outName = fileName + "." + typ
				
				if uList == 'invalid URL given':
					print("invalid download link given\n")
				else:
					FM.authDownload(downloadLink,name,password,outName )
					print("download successful :-) \n")
			
			else:
				print("Invalid option chosen")
				print()

		elif option == "S":	
			searchName = input("Please enter the name of the file: \n")
			output = FM.searchFile(searchName)
			outLength = len(output)
			if outLength == 0:
				time.sleep(1)
				print("Unfortunately the file was not found :(")
			else:
				time.sleep(1)
				print("The file "+searchName+" exists")
			print("")
			

		elif option == "E":
			deleteName = input("Please enter the name of the file to be deleted: \n")
			output = FM.deleteFile(deleteName)
			print("")
			time.sleep(1)

		elif option == "Q":
			time.sleep(1)
			print("Come back soon to get more files")
			exit()
		
		elif option == "T":
			print("connect to server below to get your file, Make sure you are connected to eduroam")
			FT.getIP()
			time.sleep(1)
		else:
			print("Invalid option, please choose one from the ones given below")
			time.sleep(1)

	def login():
		"""Functions that authenticates the user before they are given access to the functionalities they want to use

		:return: If the user is signing in, Returns ``False`` if they succesfully login and ``True`` if they did not succefuly login. It returns True one they have successfuly signed up
		:rtype: Bool
		"""
		login = input("Welcome, select an option below\n1 - sign in: | 2 - sign up \n")
		if login == "1":
			name = input("Enter your username \n")
			password = input("Enter your password\n")
			
			checkBool = AD.check(name,password)
			if (checkBool):
				time.sleep(0.3)	
				os.system('clear')
				print("welcome "+name)

				return False
			else:
				time.sleep(0.3)	
				print("Sorry, wrong username or password was entered , please recheck your cridentials and sign in again")
				return True
		
		elif login == "2":
			print("welcome new user \n")
			name = input("Enter your username that you will use in log in \n")
			password = input("Enter your password that you will use to log in\n")
			checkBool = AD.createUser(name,password)
			time.sleep(0.3)	
			print("Congratulations, you have been successfully reqistered, now choose option 1 to sign in with your current details\n")
			return True
			

		else:
			print("Oops, you entered an unknown option, please choose between 1 and 2")
			time.sleep(0.3)	
			
	if __name__ == "__main__":
		try:
			welcome()
			checkLogin = login()
			while(checkLogin):
				checkLogin = login()

			while True:
				mainMenu()
				pass
		except Exception as e:
			print(e)
