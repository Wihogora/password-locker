import unittest
from create import *
class Usertest(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("wivine","wihogora","wivi@gmail.com","wivi","wivi") # create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"wivine")
        self.assertEqual(self.new_user.last_name,"wihogora")
        self.assertEqual(self.new_user.email,"wivi@gmail.com")
        self.assertEqual(self.new_user.username,"wivi")
        self.assertEqual(self.new_user.password,"wivi")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),6)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_cuser to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("naima","niyigena","naima@gmail.com","mami","neimar") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),5)
        '''
        test to delete
        '''
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our users list
        '''
        self.new_user.save_user()
        test_user = User("mimi","niyigena","mimi@gmail.com","mymy","mimik") # new contact
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user= User("zawadi","mutoni","zawadi@gmail.com","zaza","zawady") # new contact
        test_user.save_user()

        found_user = User.find_by_username("zaza")

        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user
        test_user = User("melody","umutoni","melody@gmail.com","melo","melodi") # new user
        test_user.save_user()

        user_exists = User.user_exist("melo")

        self.assertTrue(user_exists)

    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_user(),User.user_list)


if __name__ == '__main__':
    unittest.main()
pass