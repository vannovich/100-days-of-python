import random
print("CHARACTER STATS GENERATOR")
def rolldice():
    time = int(input("How many sides?: "))
    you = random.randint(1, time)
    return you
def rollTD():
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,8)
    health = diceOne * diceTwo
    print("Their health Is",health,"hp")

name = input("Name your warrior: ")
rolldice()
rollTD()








