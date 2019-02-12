import unittest
from create import Create
class Usertest(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_create = Create("wivine","wihogora","wivi@gmail.com","wivi","wivi") # create contact object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_create.first_name,"wivine")
        self.assertEqual(self.new_create.last_name,"wihogora")
        self.assertEqual(self.new_create.email,"wivi@gmail.com")
        self.assertEqual(self.new_create.username,"wivi")
        self.assertEqual(self.new_create.password,"wivi")

    def test_save_create(self):
        '''
        test_save_create test case to test if the contact object is saved into
        the contact list
        '''
        self.new_create.save_create() # saving the new contact
        self.assertEqual(len(Create.create_list),4)

    # create_list = [] # Empty contact list
    # # Init method up here
    # def save_create(self):

    #     '''
    #     save_create method saves contact objects into create_list
    #     '''

    #     Create.create_list.append(self)

    # Items up here...

    def test_save_multiple_create(self):
        '''
        test_save_multiple_create to check if we can save multiple users
        objects to our create_list
        '''
        self.new_create.save_create()
        test_create = Create("naima","niyigena","naima@gmail.com","mami","neimar") # new contact
        test_create.save_create()
        self.assertEqual(len(Create.create_list),6)
        '''
        test to delete
        '''
    def test_delete_create(self):
        '''
        test_delete_create to test if we can remove a user from our users list
        '''
        self.new_create.save_create()
        test_create = Create("mimi","niyigena","mimi@gmail.com","mymy","mimik") # new contact
        test_create.save_create()

        self.new_create.delete_create()# Deleting a create object
        self.assertEqual(len(Create.create_list),1)

    # def delete_create(self):

    #     '''
    #     delete_create method deletes a saved user from the create_list
    #     '''

    #     Create.create_list.remove(self)


    def test_find_create_by_username(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_create.save_create()
        test_create= Create("zawadi","mutoni","zawadi@gmail.com","zaza","zawady") # new contact
        test_create.save_create()

        found_create = Create.find_by_username("zaza")

        self.assertEqual(found_create.username,test_create.email)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        '''

        for create in cls.create_list:
            if create.username == username:
                return create



if __name__ == '__main__':
    unittest.main()
# pass