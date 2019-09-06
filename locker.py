
class Credential:
      """
      Class for credentials, generate passwords and save passwords and user information
      """
      credential_list = []
      def __init__(self,user_name,password):
        '''
        __init__ method that helps us define properties for our objects.
        '''
        #instances
        self.user_name = user_name
        self.password = password
     
     
      def save_credentials(self):
        '''
        function which saves new created intances
        '''
        Credential.credential_list.append(self)

      @classmethod
      def authenticate_credential(cls, user_name, password):
        '''
        Method that checks if the username and password are correct
        '''
        for credential in cls.credential_list:
            if credential.user_name == user_name and credential.password == password:
                return credential
        return 0
      def generating_password(size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		generate_password=''.join(random.choice(char) for _ in range(size))
		return generate_password

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