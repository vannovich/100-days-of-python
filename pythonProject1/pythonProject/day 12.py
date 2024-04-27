print("EXAMS GRADE CALCULATOR")
subject = input("Course Title: ")
print("Max possible score","\033[35m",100,"\033[0m")
score = int(input("Your score: "))
percentage = score
if (score < 0 or score > 100):
    print("No allocated Grade")
elif (score < 50):
    print("You got ",percentage,"% which is ","\033[31m","U","\033[0m","a fail!! Too bad")
elif (score >= 50 and score < 60):
    print("You got ",percentage,"% which is ","\033[31m","D","\033[0m", "a fail!! Too bad")
elif (score >= 60 and score < 70):
    print("You got a ",percentage,"% which is ","\033[32m","C","\033[0m"," Good job !!")
elif (score >= 70 and score < 80):
    print("You got a ",percentage,"% which is ","\033[32m","B","\033[0m"," Very Good job !!")
elif (score >= 80 and score < 90):
    print("You got a ",percentage,"% which is ","\033[32m","A-","\033[0m","Excellent Good job !!")
elif (score >= 90 and score < 101):
    print("You got a ",percentage,"% which is ","\033[32m","A+","\033[0m"," Very Excelent job !!")
else:
    print("Please enter a valid score!!!")
