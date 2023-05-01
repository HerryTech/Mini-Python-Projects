from random import choice
from string import punctuation
from password_words import adjectives, nouns
from sys import exit


def generatePassword():
    

name = input("What should I call you?: ")
print(f"\n{name}, Welcome to password generator!")
print("I will help you create strong and easy to remember password")
print("Are you ready?")
response = input("Enter 'yes' to generate or 'q' to quit: ")
if response == "yes":
    generatePassword()
else:
    exit(0)