from sys import exit
#from animal_quiz import showQuestion

def checkAnswer(guess, answer):
    score = 0
    lives = 3

    if guess == "q":
        exit(0)
    elif guess == answer:
        print("Correct!")
        score += 1   
    else:
        print("\nOops, that was a wrong guess")
        if lives != 0 & lives <= 3:
            response = input("Try again: ")
            if response == "q":
                exit(0)
            elif response == "yes":
                lives -= 1
                print("Now you can try again")
                guess = input("> ")
            else:
                print("Not valid!. Enter 'yes' or 'q'")
        else:
            print("You have no lives again. Game over!")
            exit(0)