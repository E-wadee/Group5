import getpass
import string
import os

# creatinga lists of users, their PINs and bank statements
users = ['selorm', 'thadius', 'suzzy', 'farouk','esi','raihana']
pins = ['0001', '1111', '2222', '3333', '4444', '5555']
amounts = [10000, 20000, 30000, 40000,50000,60000]
count = 0
# while loop checks the validity of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		elif user == users[2]:
			n = 2
		elif user == users[3]:
			n = 3
		elif user == users[4]:
			n = 4
		else:
			n = 5
		break
            
	else:                        #Response if an Invalid Username is entered.
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'selorm':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('PIN NOT VALID')
				print('***********')
				print('-----------')
				print()

		if user == 'thadius':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'suzzy':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'farouk':
			if pin == pins[3]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'esi':
			if pin == pins[4]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'raihana':
			if pin == pins[5]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
	else:
		print('------------------------')
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		print('------------------------')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('-----------------------------------')
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	print('-----------------------------------')
	exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome to Group5 ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nBalance__(B) \nWithdraw___(W) \nDeposit__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['b', 'w', 'd', 'p', 'q']
	response = response.lower()
	if response == 'b':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'GHC IN YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
		print('---------------------------------------------')
		if cash_out%10 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 GHC NOTES')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			print('-----------------------------------')
			print('***********************************')
			print('WITHDRAWAL SUCCESSFUL. YOUR NEW BALANCE IS: ', amounts[n], 'GHC')
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'd':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if cash_in%10 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 10 GHC NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			print('----------------------------------------')
			print('****************************************')
			print('DEPOSIT WAS SUCCESSFUL. YOUR NEW BALANCE IS: ', amounts[n], 'GHC')
			print('****************************************')
			print('----------------------------------------')
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN DOES NOT MATCH')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('YOUR PIN HAVE BEEN UPDATED SUCCESSFULLY')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('-------------------------------------')
    ##if the user chooses to quit.
	elif response == 'q':
		userReceipt = input('Would You Like To Print A Receipt For This Transaction? Y/N: ')
		if userReceipt == "Y":
			print('******************')
			print('Transaction Successfully Completed')
			print('Transaction ID is 0101224566621225')
			print('Transaction Type: Deposit')
			print('Deposit Amount: GHC 5000')
			print('Current Available Balance = 15000')
			print('Date: 11TH OCT. 2021')
			print('*********************')
			print('Thank you for Banking with Group5')
		else:
			print("Thank you for Banking with Group5")

		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')

