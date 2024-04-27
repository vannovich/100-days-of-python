import random
print("GUESS THE NUMBER GAME!!!")
print("pick from 1 to 80")
count = 0
number = random.randint(1,80)
while True:
    guess = int(input("Your guess?: "))
    if count == 10:
        print("You've gotten the max tries!!")
        print("The correct answer is: ",number)
        print("Game will restart")
        continue
    if guess < 0:
        exit()
    elif guess < number:
        print("Too low")
        count += 1
    elif guess > number:
        print("Too high")
        count += 1
    elif guess == number:
        count += 1
        print("You're a genius, you got it right")
        break

print("Great you're a genius,You won with",count,"attempts")