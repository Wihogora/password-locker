class User:
        """
        Class that generates new instances of user

        """
        user_list = [] # Empty user list
        def __init__(self,first_name,last_name,email,username,password):

            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.username = username
            self.password = password
        
        # Init method up here
        def save_user(self):

            '''
            save_user method saves users objects into user_list
            '''

            User.user_list.append(self)

        def delete_user(self):

            '''
            delete_user method deletes a saved user from the user_list
            '''

            User.user_list.remove(self)

        @classmethod
        def find_by_username(cls,username):
            '''
            Method that takes in a username and returns a user that matches that username.

            '''

            for user in cls.user_list:
                if user.username == username:
                    return user
                    
        @classmethod
        def user_exist(cls,username):
            '''
            Method that checks if a user exists from the users list.
            '''
            for user in cls.user_list:
                if user.username == username:
                        return True

            return False
        @classmethod
        def display_user(cls):
            '''
            method that returns the users list
            '''
            return cls.user_list


if __name__ ==  '__main__':
    unittest.main()
pass