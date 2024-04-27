import os, time
print(">>>> ToDo List Manager >>>>>")
myList = ["Pray","code","Study","sing","write","create","Teach","Exercise"]
def printList():
    print()
    for i in myList:
        print(i)
    print()

while True:
    view = input("Do you want view list Or Do you want you Add or Remove from/List Or Replace?: ")
    if (view == "add" or view == "Add"):
        item = input("Next Item in ToDo List: ")
        myList.append(item)
    elif (view == "remove" or view == "Remove"):
        item = input("Next Item in ToDo List: ")
        if item in myList:
            myList.remove(item)
        else:
            print(f"{item} not in list")
    elif (view == "view" or view == "View"):
        printList()
    elif (view == "Replace" or view == "Replace"):
        number = int(input("Position of item to Replace: "))
        item = input("Enter new item: ")
        myList[number] = item
    printList()