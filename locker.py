import random
import string
#Created a global variable which will be accessible to all functions
global user_list 

         #First class for User

class User:
	'''
	Class to create user accounts and save his/her informations
	'''
	# Class Variables
	# global user_list
	user_list = []
	def __init__(self,user_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		
		self.password = password

	def save_user(self):
   
		'''
		Function to save a newly created user instance
		'''
		User.user_list.append(self)
		

    # Second Class  For Credential

class Credential:
      """
      Class for credentials, generate passwords and save passwords and user information
      """
      credential_list = []
	    
      user_credentials_list = []
      @classmethod
      def authenticate_credential(cls, user_name, password):
        '''
        Method that checks if the username and password are correct
        '''
        user = ''
        for user in User.user_list:
            if (user.user_name == user_name and user.password == password):
                user = user.user_name
                return user
        return 0

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
      
    
    
      # def delete_credential(self):
		  
      # '''
		  # function  that deletes  credentials  that are no longer needed in the application.

      # '''
	  	
      # User.user_list.remove(self)  

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

     