print("Math Games!")
print()
number = int(input("Name your multiple: "))
point = 0
for i in range(1,11):
    multiple = i*number
    print(i,"*",number,"=")
    tries = int(input(""))
    if tries == multiple:
        point += 1
        print("Great job, Keep Going")
        i += 1
    else:
        print("You failed, The Answer is",multiple)
        i += 1
if point == 10:
    print("You are a real genius, Congratulations")
print()
print("You scored",point,"out of 10")


