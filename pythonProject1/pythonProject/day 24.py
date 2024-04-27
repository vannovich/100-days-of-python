import random
print("Infinity Dice Roller")
def rolldice():
    time = int(input("How many sides?: "))
    you = random.randint(1, time)
    print("You rolled", you)

print()
roll = ""
while True:
    rolldice()
    roll = input("Roll again?: ")
    if roll == "yes":
        rolldice()
        roll = input("Roll again?: ")
    else:
        exit()









