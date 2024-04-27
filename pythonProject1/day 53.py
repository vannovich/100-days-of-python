print("INVENTORY")
print("=========")
import os, time
inventory = []
try:
    f = open("inventory.txt","r")
    inventory = eval(f.read())
    f.close()
except:
    pass

def AddItem():
    print()
    Item = input("Item to Add: ").upper()
    inventory.append(Item)
    print("Added")

def ViewItem():
    print()
    seen = set(inventory)
    for item in seen:
         print(f"{item} {inventory.count(item)}")

def removeItem():
    print()
    Item = input("Item to Add: ").upper()
    if Item in inventory:
        inventory.append(Item)
        print("Removed")
    else:
        print("Item Not in Inventory")

while True:
    time.sleep(1)
    print()
    menu = input("1: Add\n2: View\n3: remove\n>")
    if menu == "1":
        AddItem()
    elif menu == "2":
        ViewItem()
    else:
        removeItem()

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
