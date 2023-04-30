from sys import exit

print("Guess the number game")
print("I am thinking of a 3-digit number. Try to guess what it is")
print("\nGame instructions:")
print("RightWrong means One digit is correct but in the wrong position")
print("RightRight means One digit is correct and in the right position")
print("WrongWrong means No digit is correct")
print("You have 10 guesses")

response = input("\nAre you ready?Y/n: ")
if response.lower() == "y":
    print(2)
else:
    exit(0)


