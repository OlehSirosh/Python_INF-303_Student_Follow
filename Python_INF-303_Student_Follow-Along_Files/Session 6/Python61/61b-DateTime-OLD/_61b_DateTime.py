import datetime

todayWithTime = datetime.datetime.now()
todayWithoutTime = datetime.date.today()

print(todayWithTime)
print(todayWithoutTime)

print("The current date is", todayWithoutTime.strftime("%m/%d/%Y"))
print("The current time is", todayWithTime.strftime("%H:%M:%S"))


