def checkGuessWord(guessWord, secretWord, clue):
    for i in range(len(secretWord)):
        if guessWord == secretWord[i]:
            clue[i] = guessWord
    return clue

        
    