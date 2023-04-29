from sys import exit
#from animal_quiz import showQuestion

def checkAnswer(guess, answer):
    score = 0
    lives = 3

    if guess == "q":
        exit(0)
    elif guess.lower() == answer.lower():
        score += 1   
        print(f"Correct!. Your score is {score}")
    else:
        while True:
            print("\nOops, that was a wrong guess")
            if lives != 0 & lives <= 3:
                guess = input("Try again: ")
                if guess.lower() == answer.lower():
                    score += 1   
                    print(f"Correct!. Your score is {score}")
                elif guess == "q":
                    exit(0)
            else:
                print("\nYou have no lives again")
                print(f"Your score is {score}. Game over!")
                exit(0)