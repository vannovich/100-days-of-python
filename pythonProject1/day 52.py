import time,os
pizza = []
try:
    f = open("Pizza.txt","r")
    pizza = eval(f.read())
    f.close()
except:
    print("ERROR: No existing pizza list, using blank list")

def viewPizza():
    h1 = "Name"
    h2 = "Topping"
    h3 = "Size"
    h4 = "Quantity"
    h5 = "Total"
    print(f"{h1: ^10}{h2: ^10}{h3:^10}{h4:^10}{h5:^10}")
    for row in pizza:
        print(f"{row[0]: ^10}{row[1]: ^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")

def addPizza():
    time.sleep(1)
    os.system("clear")
    name = input("Name: ")
    topping = input("Topping: ")
    size = input("Size (s/l/m: ").lower()
    while True:
        try:
            qty = int(input("Quantity: "))
            break
        except:
            print("ERROR: Quantity must be a whole number!!")
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
    total = cost * qty
    total = round(total, 2)
    row = [name, topping, size, qty, total]
    pizza.append(row)


while True:
    time.sleep(1)
    os.system("clear")
    print("Rominos Pizza")
    print()
    menu = input("1: Add Pizza\n2: view pizza\n>")
    if menu == "1":
        addPizza()
    else:
        viewPizza()
    f = open("Pizza.txt", "w")
    f.write(str(pizza))
    f.close()
