class Create:
    """
    Class that generates new instances of create

    """
    create_list = []
    def __init__(self,first_name,last_name,email,username,password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
    
    # Init method up here
    def save_create(self):

        '''
        save_create method saves contact objects into contact_list
        '''

        Create.create_list.append(self)




 
#     def test_save_create(self):
#         '''
#         test_save_contact test case to test if the contact object is saved into
#             the contact list
#         '''
#         self.new_create.save_create() # saving the new contact
#         self.assertEqual(len(Create.create_list),1)

if __name__ ==  '__main__':
    unittest.main()
pass