initialSalesGoal = 20000
multiplier = 100

for monthlyGoal in range (1,13):
    monthlySalaryGoal = initialSalesGoal + (monthlyGoal * multiplier)
    print("You sales goal from month " + str(monthlyGoal) + " is " + str(monthlySalaryGoal))
print("Good luck with you goals")
