import csv

total = 0.0

with open("January.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row["Net Toatal"])
        total += float(row["Net Total"])

print(f"Total: {total}")