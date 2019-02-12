class Credential:
        """
        Class that generates new instances of user

        """
        credential_list = [] # Empty credential list
        def __init__(self,first_name,last_name,email,username,password):

            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.username = username
            self.password = password
        
        # Init method up here
        def save_credential(self):

            '''
            save_credential method saves users objects into user_list
            '''

            Credential.credential_list.append(self)

        def delete_credential(self):

            '''
            delete_credential method deletes a saved user from the credential_list
            '''

            Credential.credential_list.remove(self)

        @classmethod
        def find_by_username(cls,username):
            '''
            Method that takes in a username and returns a user that matches that username.

            '''

            for credential in cls.credential_list:
                if credential.username == username:
                    return credential
                    
        @classmethod
        def credential_exist(cls,username):
            '''
            Method that checks if a user exists from the users list.
            '''
            for credential in cls.credential_list:
                if credential.username == username:
                        return True

            return False
        @classmethod
        def display_credential(cls):
            '''
            method that returns the users list
            '''
            return cls.credential_list


if __name__ ==  '__main__':
    unittest.main()
pass