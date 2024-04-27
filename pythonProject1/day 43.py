import random

def ran():
    number = random.randint(1,90)
    return number


numbers = []

for i in range(8):
    numbers.append(ran())

def printBingo():
    for row in bingo:
        print(row)

numbers.sort()

bingo = [[numbers[0],numbers[1],numbers[2]],
         [numbers[3],"BINGO",numbers[4]],
         [numbers[5],numbers[6],numbers[7]]]

printBingo()

