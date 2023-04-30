from random import shuffle

def getSecretNumber():
    max_number = 3
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    secret_number = ""
    for i in range(max_number):
        secret_number += str(numbers[i])
        the_number = secret_number
    return the_number

def guessNumber():
    maxGuess = 10
    numOfTrial = 1
    guess = ""
    while (maxGuess != 0 & maxGuess <= 10) & (guess != getSecretNumber()):
        guess = input(f"Guess #{numOfTrial}: ")
        maxGuess -= 1
        numOfTrial += 1
        if guess == getSecretNumber():
            print("Correct!. You guess right")
        



        

