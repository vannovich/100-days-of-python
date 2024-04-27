print("TODO List Management System")
ToDo = []

f = open("Event.txt","r")
ToDo = eval(f.read())
f.close()
def prettyPrint():
    print()
    for i in ToDo:
        for j in i:
            print(j,end=" | ")
def add():
    TodoIs = input("Item to add: ")
    DueBy = input("Due by: ")
    print("Importance is either low, high or medium")
    Importance = input("How important: ")
    row = [TodoIs, DueBy, Importance]
    ToDo.append(row)

def view():
    menu = input("1: View all\n2: view priority\n>")
    if (menu == "1"):
        prettyPrint()
    elif (menu == "2"):
        menu = input("High , low or medium: ").strip().lower()
        if (menu == "high") or (menu == "medium") or (menu == "low"):
            for row in ToDo:
                if menu in row:
                    for i in row:
                        print(i, end=" | ")

def remove():
    menu = input("What do you want to remove?: ")
    for row in ToDo:
        if menu in row:
            ToDo.remove(row)
        else:
            print()
            print("Item's not in my ToDo list")

while True:
    print()
    menu = input("1: Add\n2: view\n3: Remove\n4: edit\n>")
    if (menu == "1"):
        add()

    elif (menu == "2"):
        view()

    elif (menu == "3"):
        remove()

    elif (menu == "4"):
        menu = input("What do you want to edit: ")
        for row in ToDo:
            if menu in row:
                edit = input("New item: ")
                menu = edit

    f = open("Event.txt","w")
    f.write(str(ToDo))
    f.close()
