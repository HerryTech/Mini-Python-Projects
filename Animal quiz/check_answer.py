from sys import exit

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
        print("\nOops, that was a wrong guess!!!")
        while (lives != 0 & lives <=3) & (guess.lower() != answer.lower()):
                guess = input("Try again: ")
                lives -= 1
                if guess.lower() == answer.lower():
                    score += 1
                    print(f"Correct!. Your score is {score}")
                if (lives == 0) & (guess.lower() != answer.lower()):
                    print("Wrong answer! You have no more lives.")
                    print(f"Your score is {score}. Game over!")
                    exit(0)
                    
                
