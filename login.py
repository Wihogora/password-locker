Username=input()
Email=input()
Password=input()
PhoneNumber=input()
print(Username,Email,Password,PhoneNumber)
e=input()
f=input()
if(Email==e and Password==f):
    print("Welcome" +Username)
else:
    print("Failed to login ")  
