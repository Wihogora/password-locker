from create import User
# new_user= {}
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
    return User.user_exist(username)

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

    print("New User")
    print("-"*10)
    print ("first_name ....")
    first_name = input()
    print("last_name ...")
    last_name = input()
    print("email ...")
    email = input()
    print("username ...")
    username = input()
    print("password ...")
    password = input()
    new_user = User(first_name,last_name,email,username,password)
    save_user(new_user)
    # save_user(create_user(first_name,last_name,email,username,password)) # create and save new user.
    print ('\n')
    print(f"New User {first_name} {last_name} created")
    print ('\n')
    while True:
            print("Use these short codes : cu - create a new user, du - display user, fu - find a user , np - new password , gp - generate password , dl - delete user, ex -exit the user list ")

            short_code = input().lower()

        #     if short_code == 'cu':
                        

            if short_code == 'du':

                        if display_user():
                                print("Here is a list of all your user")
                                print('\n')

                                for user in display_user():
                                        print(f"First name.......{user.first_name}")
                                        print(f"Last name.......{user.last_name}")
                                        print(f" Email.......{user.email}")
                                        

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any user saved yet")
                                print('\n')

            elif short_code == 'fu':

                        print("Enter the username you want to search for")

                        search_username = input()
                        if check_existing_user(search_username):
                                search_user = find_user(search_username)
                                print(f"{search_user.first_name} {search_user.last_name}")
                                print('-' * 20)

                                print(f"email.......{search_user.email}")
                                print(f"password.......{search_user.password}")
                        else:
                                print("That user does not exist")
            elif short_code == 'dl':

                        print("Enter the username you want to delete")

                        search_username = input()
                        # print(new_user)
                        if check_existing_user(search_username):
                                # new_user = User(first_name,last_name,email,username,password) 
                                del_user(new_user)
                                # print(f"{search_user.first_name} {search_user.last_name}")
                                # print('-' * 20)

                                 
                         

                                print(f"Deleted")
                                
                        else:
                                print("That user does not exist")

            elif short_code == "ex":
                        print("Bye .......")
                        break
            else:
                        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()






























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
