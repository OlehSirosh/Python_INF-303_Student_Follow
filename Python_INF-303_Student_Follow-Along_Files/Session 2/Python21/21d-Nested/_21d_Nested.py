annualSales = 300000
region = "West"

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
#add if statement here    
    if region == 'North':
        print("Send a snowboard")
    elif region != 'North':
        print("Send a baseball bat")


elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")

