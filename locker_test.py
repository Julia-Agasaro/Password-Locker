import unittest
from locker import Credential
# from user import User

class Testcredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    '''

    def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_credential = Credential("Julia","password")
    
    def tearDown(self):
        '''
        clean up after running each test
        '''
        Credential.credential_list = []
    
    
    
    
    
    def test__init__(self):
        
        '''
		Test to if check the initialization/creation of user instances is properly done
		'''
        self.assertEqual(self.new_credential.user_name,'agajulia4')
        self.assertEqual(self.new_credential.password,'pswd4')

    def test_authentication(self):
        '''
        Tests proper autentication for log in purposes
        '''
        self.new_credential = Credential('agajulia4','snapchat','pswd4')
        self.new_credential.save_credentials()
        credential1 = Credential('Melissa','snapchat','passwd')
        credential1.save_credentials
    def setUp(self):
        
        '''
		Function to create an account's credentials before each test
		'''
        
        self.new_credential = Credential('agajulia4','snapchat','pswd4')
    

    def test__init__(self):
        
        '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		
        self.assertEqual(self.new_credential.user_name,'agajulia4')
		
        self.assertEqual(self.new_credential.account_name,'snapchat')
		
        self.assertEqual(self.new_credential.password,'pswd4')

    def test_save_credentials(self):
		
        '''
		Test to check if the new credential informations are saved into the credentials list
		'''
		
        self.new_credential.save_credentials()
		
        snapchat = Credential('agajulia4','snapchat','pswd4')
		
        snapchat.save_credentials()
		
        self.assertEqual(len(Credential.credential_list),2)

if __name__ == '__main__':
    unittest.main()