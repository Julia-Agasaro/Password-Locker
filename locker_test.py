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
        self.assertEqual(self.new_credential.user_name,'Julia')
        self.assertEqual(self.new_credential.password,'password')

    def test_authentication(self):
        '''
        Tests proper autentication for log in purposes
        '''
        self.new_credential = Credential('Julia','password')
        # self.new_credential.save_credential()
        credential1 = Credential('Melissa','passwd')
        # credential1.save_credential
if __name__ == '__main__':
    unittest.main()