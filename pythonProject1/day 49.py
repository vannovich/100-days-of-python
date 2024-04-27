import os,time
f = open("Text.txt","r")
scores = f.read().split("\n")
f.close()
highscore = 0
name = None
print(scores)
for row in scores:
    data = row.split()
    if data != []:
        if int(data[1]) > highscore:
            highscore = int(data[1])
            name = data[0]

print("The winner is",name,"with",highscore)

