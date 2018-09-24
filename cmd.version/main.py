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

def get_user_info():
    file = open("user_passw.txt", "r")
    lines = file.readlines()  # check if user exists
    for i in range(len(lines)):
        lines[i] = lines[i].split("|")[0]
    length = len(lines)
    while (1):
        user = input("enter user: ")
        check = 0
        for i in lines:
            if i == user:
                print("your user already exists")
                check = 1
                break
        if check == 0:
            break
    passw = input("enter password: ")
    file.close()
    return user, passw, length

def add_user(user, passw, length):
    file = open("user_passw.txt", "a")
    file.write("\n" + user + "|" + passw + "|" + str(length))

if __name__ == '__main__':
    choose = input("Login or Sign up?")                                         #login or sign up
    if choose == "l":                                                           #login
        user = try_login()                                                      #connect to data base
        #print(user)
        while (1):
            choice = input("Are you a driver(d) or a passenger(p)? Please enter the initial of your choice: ")
            if (choice == "d" or choice == "p"):
                if (choice == "d"):
                    driver_interface(user)
            else:
                print("Your choice is not valid, please choose again!")
    elif choose == "s":                                                         #sign up
        user, passw, acct_num = get_user_info()
        add_user(user, passw, acct_num)