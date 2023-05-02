from random import choice
from sys import exit
from nine_lives_words import words

lives = 9
secret_word = choice(words)
clue = []
for i in range(len(secret_word)):
    clue.append("?")

heart_symbol = u'\u2764'

def checkGuessWord(guessWord, secretWord, clue):
    for i in range(len(secretWord)):
        if guessWord == secretWord[i]:
            clue[i] = guessWord
    return clue
  

print("Guess the secret word game")

print("\nGuess the secret word, one letter at a time")
print("Choose your letter carefully because you have nine lives")
print("Lose all your lives and it's game over")
response = input("\nAre you ready? y/n: ")
if response == "y":
    while lives > 0:
        print(f"\n{clue}")
        print("Lives left: " + heart_symbol * lives)
        guess_word = input("Guess a letter: ")
        if len(guess_word) == 2:
            print("\nNope, one letter at a time")
        checkGuessWord(guess_word, secret_word, clue) 
        if (len(guess_word) == 1) & (guess_word not in secret_word):
            print("\nIncorrect! You lose a life")
            lives -= 1
        if lives == 0:
            print("Game over!")
        if "".join(clue) == secret_word:
            print(f"\nThe secret word = {clue}")
            print("Correct! You won")
            exit(0)
else:
    exit(0)



