annualSales = 200000
newCustomer = True

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
#add compound conditional statement here
elif annualSales > 100000 and newCustomer:
        print("Bronze Custouer and first-time prize winner")
elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")

