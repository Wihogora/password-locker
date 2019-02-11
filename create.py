import unittest # Importing the unittest module

class create:
    """
    Class that generates new instances of create

    """
def __init__(self,first_name,last_name,email,username,password):

    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.username = username
    self.password = password

def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_create = create("wivine","wihogora","0712345678","wivi","wivi@gmail.com","wivi") # create contact object
def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_create.first_name,"wivine")
    self.assertEqual(self.new_create.last_name,"wihogora")
    self.assertEqual(self.new_create.phone_number,"0712345678")
    self.assertEqual(self.new_create.email,"wivi")
    self.assertEqual(self.new_create.email,"wivi@gmail.com")
    self.assertEqual(self.new_create.email,"wivi")


if __name__ == '__main__':
    unittest.main()
pass