print("*** SECONDS IN A YEAR *****")
numOfSecInDay = 24 * 60 * 60
Year = int(input("Enter desired year: "))
if (Year % 4 == 0):
    numOfdays = 366
    numOfSec = numOfdays * numOfSecInDay
else:
    numOfdays = 365.25
    numOfSec = float(numOfdays * numOfSecInDay)

print("The number of seconds in a year: ", numOfSec)
