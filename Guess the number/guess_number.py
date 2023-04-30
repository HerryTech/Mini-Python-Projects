from random import shuffle
from sys import exit

def theGame():
    print("Guess the number game")
    print("I am thinking of a 3-digit number. Try to guess what it is")
    print("\nGame instructions:")
    print("RW means One digit is correct but in the wrong position")
    print("RR means One digit is correct and in the right position")
    print("WW means No digit is correct")
    print("You have 10 guesses")
    
    response = input("\nAre you ready? Y/n: ")
    if response.lower() == "y":
        guessNumber()
    else:
        exit(0)

def getSecretNumber():
    max_number = 3
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    secret_number = ""
    for i in range(max_number):
        secret_number += str(numbers[i])
    return secret_number

def guessNumber():
    guess = ""
    print("\nI have thought of a number")
    print("You have 10 guesses to get it")
    maxGuess = 10
    numOfTrial = 1
    secretNumber = getSecretNumber()
    while (maxGuess != 0 & maxGuess <= 10) & (guess != secretNumber):
        guess = input(f"Guess #{numOfTrial}: ")
        try:
            guessClue = getClue(guess, secretNumber)
            print(guessClue)
        except:
            print(f"The number is longer than {len(secretNumber)}")
        maxGuess -= 1
        numOfTrial += 1
        if secretNumber == guess:
            print("\nCorrect! You guess right")
            print("Do you want to play again? yes or no")
            response = input("> ")
            if response == "yes":
                guessNumber()
            else:
                exit(0)
        if (maxGuess == 0) & (guess != secretNumber):
            print("\nYou ran out of guesses")
            print(f"The number is {secretNumber}")
            print("Do you want to play again? yes or no")
            response = input("> ")
            if response == "yes":
                guessNumber()
            else:
                exit(0)

def getClue(guess, secretNumber):
    clue = []
    for i in range(len(guess)):
       if guess[i] == secretNumber[i] :
           clue.append("RR")
       elif guess[i] in secretNumber:
           clue.append("RW")
       else:
           clue.append("WW")
    clue.sort()
    return " ".join(clue)

theGame()
        

