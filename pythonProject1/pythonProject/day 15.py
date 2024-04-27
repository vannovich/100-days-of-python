print("**** ANIMAL SOUND TELLER  *******")
exit = ""
while exit != "yes":
    animalsound = input("What animal do you want to hear the sound of?: ")
    if animalsound == "cow":
        print(animalsound, "Goes moo")
        exit = input("Do you want to exit?: ")
    elif animalsound == "fowl":
        print(animalsound," goo cocoricoo")
        exit = input("Do you want to exit?: ")
    elif animalsound == "cat":
        print(animalsound," Goes miaoo")
        exit = input("Do you want to exit?: ")
    elif animalsound == "lesser spotted lemur":
        print(animalsound," Goes Awooga")
        exit = input("Do you want to exit?: ")
    elif animalsound == "dog":
        print(animalsound, " Goes raoo raooo")
        exit = input("Do you want to exit?: ")