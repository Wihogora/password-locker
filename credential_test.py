import unittest
from credential import *
class Credentialtest(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("wivine","wihogora","wivi@gmail.com","wivi","wivi") # create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.first_name,"wivine")
        self.assertEqual(self.new_credential.last_name,"wihogora")
        self.assertEqual(self.new_credential.email,"wivi@gmail.com")
        self.assertEqual(self.new_credential.username,"wivi")
        self.assertEqual(self.new_credential.password,"wivi")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the user object is saved into
        the credential list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list),5)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple users
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("naima","niyigena","naima@gmail.com","mami","neimar") # new user
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),7)
        '''
        test to delete
        '''
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("mimi","niyigena","mimi@gmail.com","mymy","mimik") # new contact
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''

        self.new_credential.save_credential()
        test_credential= Credential("zawadi","mutoni","zawadi@gmail.com","zaza","zawady") # new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_username("zaza")

        self.assertEqual(found_credential.username,test_credential.username)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential
        test_credential = Credential("melody","umutoni","melody@gmail.com","melo","melodi") # new user
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("melo")

        self.assertTrue(credential_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credential saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)


if __name__ == '__main__':
    unittest.main()
pass