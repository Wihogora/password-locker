import unittest
from create import Create
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
    self.assertEqual(len(Create.create_list),1)

contact_list = [] # Empty contact list
 # Init method up here
def save_create(self):

    '''
    save_create method saves contact objects into create_list
    '''

    Create.create_list.append(self)

if __name__ == '__main__':
    unittest.main()