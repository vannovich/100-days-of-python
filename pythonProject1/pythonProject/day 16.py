print("Fill-in the blank lyrics!")
print("(type in the blank lyrics, see if you're as cool as me)")

count = 0
while True:
    print("Never going to ____ you up")
    tries = input("key in your response: ")
    if (tries == "give" or tries == "Give"):
        count += 1
        print("well done, it took you", count,"attempts")
        break
    else:
        count += 1
        print("Nope, try again")
        if count == 10:
            print("You've had the maximum tries: ",count)
            break

