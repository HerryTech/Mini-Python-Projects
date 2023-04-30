from sys import exit
from random import choice
from guess_func import getSecretNumber, guessNumber

print("Guess the number game")
print("I am thinking of a 3-digit number. Try to guess what it is")
print("\nGame instructions:")
print("Love means One digit is correct but in the wrong position")
print("Peace means One digit is correct and in the right position")
print("Joy means No digit is correct")
print("You have 10 guesses")

def guessGame():
    response = input("\nAre you ready? Y/n: ")
    if response.lower() == "y":
        print("I have thought of a number")
        print("You have 10 guesses to get it")
        the_number = getSecretNumber()
        print(the_number)
        guessNumber()
    else:
        exit(0)
        
guessGame()


