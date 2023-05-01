from random import choice
from sys import exit
from nine_lives_words import words
from check_guess import checkGuess

lives = 9
secret_word = choice(words)
clue = []
for i in range(len(secret_word)):
    clue.append("?")

heart_symbol = u'\u2764'
heart = []
for i in range(9):
    heart.append(heart_symbol)
hearts = "  ".join(heart)
print(hearts)

print("Guess the secret word")

print("\nGuess the secret word one letter at a time")
print("Choose your letter carefully because you have nine lives")
print("Lose all your lives and it's game over")
response = input("\nAre you ready? y/n: ")
if response == "y":
    print("\nGuess the word")
    print(secret_word)
    print(clue)
    guess = input("> ")
    checkGuess(guess, secret_word, clue)
else:
    exit(0)



