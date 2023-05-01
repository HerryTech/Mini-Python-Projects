from random import choice, randint
from string import punctuation
from password_words import adjectives, nouns
from sys import exit


def generatePassword():
    adj = choice(adjectives)
    noun = choice(nouns)
    num = randint(0, 99)
    punct = choice(punctuation)
    password = adj + noun + str(num) + punct
    return password

generatePassword()  

name = input("What should I call you?: ")
print(f"\n{name}, Welcome to password generator!")
print("I will help you create strong and easy to remember password")
print("Are you ready?")
response = input("Enter 'yes' to generate or 'q' to quit: ")
if response == "yes":
    pwd = generatePassword()
    print(pwd)
else:
    exit(0)