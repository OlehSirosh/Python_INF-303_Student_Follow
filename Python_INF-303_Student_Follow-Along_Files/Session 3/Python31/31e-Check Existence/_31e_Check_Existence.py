import os

if os.path.isfile(log.txt):
    writeFile = open('log.txt', 'a')
else:
    writeFile = open('log.txt', 'w')

# otherwise, open a new log

toLog = input("What do you want to write to the log? ")
writeFile.write("\n" + toLog)
writeFile.close()


# import os

# if os.path.isfile('log.txt'):
#     with open('log.txt', 'a') as writeFile:
#         toLog = input("What do you want to write to the log? ")
#         writeFile.write("\n" + toLog)
# else:
#     with open('log.txt', 'w') as writeFile:
#         toLog = input("What do you want to write to the log? ")
#         writeFile.write(toLog)
