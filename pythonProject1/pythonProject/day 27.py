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

while True:
    name = input("Name Your Legend: \n")
    type = input("Character Type (Human, Elf, Wizard, Orc):\n")
    print()
    print(name)
    print("HEALTH:",health())
    print("STRENGTH:",strength())
    print()
    print("May your name go down in Legend....")
    Again = input("Again?: ")
    if (Again == "No") or (Again == "no"):
        break
    time.sleep(1)
    os.system("clear")
