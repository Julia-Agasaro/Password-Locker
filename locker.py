import random
import string

class Credential:
      """
      Class for credentials, generate passwords and save passwords and user information
      """
      credential_list = []
      def __init__(self,user_name, account_name,password):
        '''
        __init__ method that helps us define properties for our objects.
        '''
        #instances
        self.user_name = user_name
        self.account_name = account_name
        self.password = password
     
     
      def save_credentials(self):
        '''
        function which saves new created intances
        '''
        Credential.credential_list.append(self)

      def generate_password(size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
          
        '''
		Function to generate an 8 character password for a credential
		'''
		
        generate_password=''.join(random.choice(char) for _ in range(size))
		
        return generate_password
      @classmethod
      def authenticate_credential(cls, user_name, account_name, password):
        '''
        Method that checks if the username and password are correct
        '''
        user = ''
        for credential in cls.credential_list:
            if credential.user_name == user_name and credential.password == password:
                user = credential.user_name
                return user
        return 0
    

      @classmethod
	  def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credential_list = []
		for credential in cls.credential_list:
			if credential.user_name == user_name:
				user_credential_list.append(credential)
		return user_credential_list

# class User:
#     '''
#     class that generates new instances of the user 
#     '''
#      user_list = []
    
#     def __init__(self, account_name,account_username, account_password):
#         '''
#         Class to create user accounts and save their information
#         '''
#         self.acc_name = account_name
#         self.acc_username =  account_username
#         self.acc_password = account_password