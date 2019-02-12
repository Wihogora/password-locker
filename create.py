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

    def delete_create(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Create.create_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        '''

        for create in cls.create_list:
            if create.username == username:
                return create
                
    @classmethod
    def create_exist(cls,username):
        '''
        Method that checks if a user exists from the users list.
        '''
        for create in cls.create_list:
            if create.username == username:
                    return True

        return False
    @classmethod
    def display_create(cls):
        '''
        method that returns the users list
        '''
        return cls.create_list


if __name__ ==  '__main__':
    unittest.main()
pass