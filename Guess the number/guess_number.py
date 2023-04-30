from sys import exit
from random import choice

print("Guess the number game")
print("I am thinking of a 3-digit number. Try to guess what it is")
print("\nGame instructions:")
print("RightWrong means One digit is correct but in the wrong position")
print("RightRight means One digit is correct and in the right position")
print("WrongWrong means No digit is correct")
print("You have 10 guesses")

response = input("\nAre you ready? Y/n: ")
if response.lower() == "y":
    print("I have thought of a number")
    
    the_number = f"{choice(numbers)}{choice(numbers)}{choice(numbers)}"
    print(the_number)
    guess = input("Guess the number?: ")
else:
    exit(0)


