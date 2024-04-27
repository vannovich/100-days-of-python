import os,time,random
print("CHARACTER BUILDER")
def rolldice(dice):
    roll = random.randint(1,dice)
    return roll

def health():
    healthStat = (rolldice(6)*rolldice(12)/2) + 10
    return healthStat

def strength():
    strengthStat = (rolldice(6)*rolldice(8)/2) + 12
    return strengthStat

C1name = input("Name Your Legend: \n")
C1type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(C1name)
C1health = health()
C1strength = strength()
print("HEALTH:",C1health)
print("STRENGTH:",C1strength)
print()
print("Who are battling....")
C2name = input("Name Your Legend: \n")
C2type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(C2name)
C2health = health()
C2strength = strength()
print("HEALTH:", C2health)
print("STRENGTH:", C2strength)
print()
round = 1
winner = None

while True:
    time.sleep(1)
    print()
    print("Battle begins")

    C1Dice = rolldice(6)
    C2Dice = rolldice(6)

    diff = abs(C1strength - C2strength) + 1
    if C1Dice > C2Dice:
        C2health -= diff
        if round == 1:
            print(C1name, "wins the first blow")
        else:
            print(C1name, "Wins round", round)

    elif C2Dice > C1Dice:
        C1health -= diff
        if round == 1:
            print(C2name, "wins the first blow")
        else:
            print(C2name, "Wins round", round)
    else:
        print("Their swords clash and they drew round", round)

        print()
        print(C1name)
        print("HEALTH:", C1health)
        print()
        print(C2name)
        print("HEALTH:", C2health)
        round += 1
        
        if C1health <= 0:
            print(C1name, "Has died")
            winner = C1name
            break
        elif C2health <= 0:
            print(C2name, "Has died")
            winner = C2name
            break
        else:
            print("And they're both standing for the next round")
            round += 1
time.sleep(1)
print("Battle Time")
print()
print("The battle begins")
print(winner,"Has won in",round,"rounds")