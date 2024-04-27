import random, os
f = open("MyIdea.txt","a+")
lists = []
print("MY IDEAS BOOK")
while True:
     print()
     menu = input("1. Add idea\n2. Load random idea\n>").lower()
     if menu == "1" or menu == "add idea":
         texter = input("Enter intented idea: ")
         print()
         lists.append(texter)
         f.write(f"{texter}\n")
     elif menu == "2" or menu == "load":
         print()
         if lists == "":
             print("Nothing to load")
         numb = random.choice(lists)
         print(numb)

f.close