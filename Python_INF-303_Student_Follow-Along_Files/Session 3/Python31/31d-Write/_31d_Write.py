writeFile = open('log.txt', 'w')
toLog = input('Enter some text: ')
writeFile.write(toLog)
writeFile.close()

