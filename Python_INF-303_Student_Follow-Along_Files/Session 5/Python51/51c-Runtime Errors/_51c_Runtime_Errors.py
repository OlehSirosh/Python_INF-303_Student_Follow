a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a/b}.")
except:
    if b==0:
        raise
        print("This did not work. ")
else:
    print("You successfully used the python")
finally:
    print("Thank you for playing")