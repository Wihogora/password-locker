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

    def check_existing_user(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(Username)

    def display_user():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()

    def main():
    print("Hello Welcome to your user list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new user, dc - display user, fc -find a user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("first_name ....")
                            f_name = input()

                            print("last_name ...")
                            l_name = input()

                            print("email ...")
                            p_number = input()

                            print("username ...")
                            e_address = input()

                            print("password ...")
                            e_address = input()


                            save_contacts(create_contact(first_name,last_name,email,username,password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {first_name} {last_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your user")
                                    print('\n')

                                    for user in display_user():
                                            print(f"{user.first_name} {user.last_name} .....{user.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

































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
