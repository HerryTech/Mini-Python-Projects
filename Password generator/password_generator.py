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

def showPassword():
    name = input("What should I call you?: ")
    print(f"\n{name}, Welcome to password generator!")
    print("I will help you create strong and easy to remember password")
    print("\nAre you ready?")
    response = input("Enter 'yes' to generate or 'q' to quit: ")
    if response == "yes":
            pwd = generatePassword()
            print(f"\nHere is your password: {pwd}")
            while True:
                print("\nDo you like the password or would you like to generate a new one?")
                response = input("'y' to generate a new one, 'no' to quit y/n: ")
                if response == "y":
                    print(f"\nHere is your new password: {pwd}")
                else:
                    exit(0)
    else:
        exit(0)
        
showPassword()