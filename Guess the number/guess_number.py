from sys import exit
from random import choice
from guess_func import getSecretNumber

print("Guess the number game")
print("I am thinking of a 3-digit number. Try to guess what it is")
print("\nGame instructions:")
print("Love means One digit is correct but in the wrong position")
print("Peace means One digit is correct and in the right position")
print("Joy means No digit is correct")
print("You have 10 guesses")

response = input("\nAre you ready? Y/n: ")
if response.lower() == "y":
    print("I have thought of a number")
    the_number = getSecretNumber()
    guess = input("Guess the number?: ")
else:
    exit(0)


