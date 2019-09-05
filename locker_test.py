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
    
    def test__init__(self):
        
        '''
		Test to if check the initialization/creation of user instances is properly done
		'''
        self.assertEqual(self.new_credential.user_name,'Julia')
        self.assertEqual(self.new_credential.password,'password')

if __name__ == '__main__':
    unittest.main()