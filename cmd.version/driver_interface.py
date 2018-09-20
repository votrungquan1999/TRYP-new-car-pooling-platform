def get_filter():
    pass

def print_car_pool(acct):
    filename = "carpool{0}".format(acct)
    file = open(filename, "r")

def get_info():
    while (1):
        date = input("Please enter date(mm/dd/yyyy): ")
        if (len(date) != 10):
            print("Your choice is not valid, please choose again!")
        else:
            break

    while (1):
        time = input("Please enter time(24 hours format)(hh:mm): ")
        if (len(time) != 5):
            print("Your choice is not valid, please choose again!")
        else:
            break

    destination = input("Please enter your destination(State/City)")
    destination = destination.lower()
    departure = input("Please enter your departure(State/City)")
    departure = departure.lower()
    return(date, time, destination, departure)

def post_car_pool():
    pass

def driver_interface(acct):
    while (1):
        print("1. Check your car poolings.")
        print("2. Post car poolings.")
        print("3. Search for need-a-drive post.")
        choice = input('Please enter your choice: ')
        if (choice == "1" or choice == "2" or choice == "3"):
            if choice == "1":
                print_car_pool(acct)
            if choice == "2":
                print("You choose to post a car pooling.")
                date, time, destination, departure = get_info()
                post_car_pool(date,time,destination,departure)
            if choice == "3":
                date, time, destination, departure = get_filter()
        else:
            print("Your choice is not valid, please choose again!")