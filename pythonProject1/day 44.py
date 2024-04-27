import random

def ran():
    number = random.randint(1,90)
    return number

def printBingo():
    for row in bingo:
        print(row)
numbers = []

for i in range(8):
    numbers.append(ran())
numbers.sort()
bingo = [[numbers[0], numbers[1], numbers[2]],
         [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]]

while True:
    printBingo()
    num  = int(input("Next Number: "))
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"