print("REPLIT LOGIN SYSTEM")
print()
def login():
    print("Whoops! I don't recognise this password or name")

name = ""
password = ""
while True:
    name = input("What is your name: ")
    password = input("What is your password: ")

    if name == "david" and password == "baldles4life":
        print()
        print("WELCOME TO REPLIT!")
        break
    else:
        print()
        login()
