import getpass


# You can also all input() here if you want to ask for the user's psasword.
user = getpass.getuser()
password = getpass.getpass()


def scv_login(user, password):
    if user == "brittainhard" and password == "potato":
        return True
    else:
        return False


if scv_login(user, password):
    print("yay!")
else:
    print("Boo!")
