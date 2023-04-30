from sys import exit
#from animal_quiz import showQuestion

score = 0
lives = 3
def checkAnswer(guess, answer):
    global score
    global lives 
    if guess == "q":
        exit(0)
    elif guess.lower() == answer.lower():
        score += 1   
        print(f"Correct!. Your score is {score}")
    else:
        print("\nOops, that was a wrong guess!")
        while (lives != 0 & lives <= 3):
            guess = input("Try again: ")
            if guess.lower() == answer.lower():
                score += 1   
                lives -= 1
                print(f"Correct!. Your score is {score}")
            elif guess == "q":
                exit(0)
            else:
                print("\nYou have no lives again")
                print(f"Your score is {score}. Game over!")
                exit(0)