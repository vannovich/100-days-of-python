print("*** TIP CALCULATOR ***")
print("This will help you sort out you bills with ease")

myBill = float(input("What's my bill?: "))
numberOfPeople = int(input("Enter number of people: "))
answer = myBill / numberOfPeople
print("Each of you owe: ",round(answer,2))
