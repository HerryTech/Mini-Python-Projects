def checkGuess(guess, secretWord, clue):
    for i in range(len(secretWord)):
        if guess in secretWord[i]:
            clue[i] = guess
        