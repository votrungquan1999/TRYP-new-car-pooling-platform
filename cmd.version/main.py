from login import *
from driver_interface import *

def try_login():
    while (1):
        user = input("Please enter your username: ")
        passw = input("Please enter your password: ")
        acct = get_user(user, passw)
        if (acct != None):
            return acct
        print("You enter the wrong user or password, please try again!")

if __name__ == '__main__':
    user = try_login()
    #print(user)
    while (1):
        choice = input("Are you a driver(d) or a passenger(p)? Please enter the initial of your choice: ")
        if (choice == "d" or choice == "p"):
            if (choice == "d"):
                driver_interface(user)
        else:
            print("Your choice is not valid, please choose again!")