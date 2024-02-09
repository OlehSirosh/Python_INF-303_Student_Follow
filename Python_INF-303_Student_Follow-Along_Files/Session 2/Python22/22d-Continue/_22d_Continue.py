initialSalesGoal = 20000
multiplier = 100

for monthlyGoal in range(1,12):
    if monthlyGoal == 6:
        print("No goal for month")
        continue
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)

    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

print("Good luck with your goals.")
