import os, time

Mokedex = {}

def prettyPrint():
    print(f"Name\tType\tHP\tMP")
    for key, value in Mokedex.items():
        print(f"""{key: ^10}|{value["type"]: ^6}|{value["hp"]:^6}|{value["mp"]:^6}""")


while True:
    print("Add your Beast!")
    name = input("Name> ").title()
    type = input("Type> ").title()
    hp = int(input("HP> "))
    mp = int(input("MP> "))
    Mokedex[name] = {"type": type, "hp": hp, "mp":mp}
    print("_______________________")
    print()
    prettyPrint()