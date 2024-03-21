import os
if os.path.exists("log.txt"):
    with open("log.txt", "a") as writeFile:

        toLog = input("What do you want to write to the log? ")
        writeFile.write("\n" + toLog)
        writeFile.close()

