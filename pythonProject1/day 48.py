f = open("Text.txt","a+")
for i in range(0,9):
    initial = input("INITIALS > ")
    score = int(input("SCORE > "))
    f.write(f"{initial}  {score}\n")
    hell = input("Have we finished?: ").lower()
    if hell == "yes":
        break
    print()
f.close()