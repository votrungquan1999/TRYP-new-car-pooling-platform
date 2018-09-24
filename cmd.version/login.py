def get_user(user = "", passw = ""):
    file = open("user_passw.txt", "r")
    lines = file.readlines()
    for i in lines:
        user1 = (i.split(sep = "|"))[0]
        passw1 = (i.split(sep = "|"))[1]
        if ((user == user1) and (passw == passw1)):
            return((i.split(sep = "|"))[2])
    return None