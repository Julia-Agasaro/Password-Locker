#!/usr/bin/env python3.6
from locker import User, Credential
def create_user(user_name,password):
	'''
	Function to create a new user account
	'''
	new_user = User(user_name,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(user_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.authenticate_credential(user_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	generate_password = Credential.generate_password()
	return generate_password

def create_credential(user_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def delete_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.delete_credential(site_name)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker We Help you store Your Passwords just in case you forgot them.')
	while True:
		print(' ')
		print("*"*74)
		print('Kindly Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("*"*60)
			print(' ')
			print('To create a new account:')
			user_name = input('Enter a Username of your choice - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(user_name,password))
			print(" ")
			print(f'New Account Created for: {user_name} using password: {password}')
		elif short_code == 'li':
			print("*"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your username - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("*"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n Delete- Delete Credential \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("*"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("*"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Sorry the option entered is wrong. Try again.')
						save_credential(create_credential(user_name,account_name,password))
						print(' ')
						print(f'Credential Created:Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'Delete':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to delete: ')
						delete_credential(chosen_site)
						print('')
					else:
						print('Oops! Sorry the option entered is wrong Try again.')

			else: 
				print(' ')
				print('Oops! Sorry the option entered is wrong. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Sorry the option entered is wrong. Try again.')
				






if __name__ == '__main__':
	main()