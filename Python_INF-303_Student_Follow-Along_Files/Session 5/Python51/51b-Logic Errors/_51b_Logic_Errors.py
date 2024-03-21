capitalGuess = input("What is the capital of Latvia? ").upper()
numberOfGuesses = 1

while capitalGuess != "RIGA":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("You guessed incorrectly three times. Game over.")
        break
    capitalGuess = input("Guess again. ")


print("You guessed it. Riga is the capital of Latvia. It took you " + str(numberOfGuesses) + " guesses.")
