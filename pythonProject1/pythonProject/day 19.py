print("****** Loan Calculator *****")
print()
print("$1000 over 10 years at 5% APR")
print()
MoneyOwed = 1000
numOfYears = 10
for loan in range(10):
    APR = ((5 / 100) * MoneyOwed)
    myLoan = MoneyOwed + APR
    myMoneyLoan = myLoan
    print("Year",loan + 1,"is",round(MoneyOwed, 2))
interest = MoneyOwed - 1000
print()
print("You paid",round(interest, 2),"in interest")