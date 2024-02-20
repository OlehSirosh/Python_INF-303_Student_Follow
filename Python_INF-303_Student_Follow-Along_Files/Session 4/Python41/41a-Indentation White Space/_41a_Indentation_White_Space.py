region = "West"
annualSales = 500000
firstName = "Tony"
if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")
print(f"Your sales representative is {firstName}," \
f" you are in the {region} region," \
f"and you had {annualSales} in sales last year. Thanks!")
