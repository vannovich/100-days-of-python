print("SUPER SUBROUTINE")
def rout(color, word):
    if color == "red":
        print("\033[31m",word, sep=" ", end="")
    elif (color == "green"):
        print("\033[32m",word, sep=" ", end="")
    elif (color == "blue"):
        print("\033[34m",word, sep=" ", end="")
    else:
        print("\033[0m",word, sep=" ", end="")




print("With my",end="",sep=" ")
rout("red","new program")
rout("reset","I can just call red ('and') and that word will",)
print("end = \n","With no","\033[34m","Weird gaps","\033[0m")

