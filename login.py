from user import *
    def create_user(first_name,last_name,email,username,password):
        '''
        Function to create a new user
        '''
        new_user = User(first_name,last_name,email,username,password)
        return new_user
    
    def save_user(user):
        '''
        Function to save user
        '''
        user.save_user()

    def del_user(user):
        '''
        Function to delete a user
        '''
        user.delete_user()

    def find_user(username):
        '''
        Function that finds a user by username and returns the user
        '''
        return User.find_by_username(username)
































# Username=input()
# Email=input()
# Password=input()
# PhoneNumber=input()
# print(Username,Email,Password,PhoneNumber)
# e=input()
# f=input()
# if(Email==e and Password==f):
#     print("Welcome" +Username)
# else:
#     print("Failed to login ")  
