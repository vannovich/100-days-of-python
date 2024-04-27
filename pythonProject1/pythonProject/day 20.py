print("List Generator")
print()
start = int(input("Start at : "))
end = int(input("End before : "))
between = int(input("Increment between values : "))
print()
for i in range(start,end,between):
    print(i)