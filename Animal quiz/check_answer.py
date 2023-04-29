from sys import exit
score = 0
lives = 3

def checkAnswer(question, answer):
    if question == answer:
        print("Correct!")
        score += 1
    else:
        if lives != 0 & lives <= 3:
            print(f"You have {lives} left")
            print("Enter 'yes' to use it or 'q' to quit the quiz")
            response = input("> ")
            if response == "q":
                exit(0)
            elif response == "yes":
                lives -= 1
                print("Now you can try again")
                print(question)
            