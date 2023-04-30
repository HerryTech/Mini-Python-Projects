from check_answer import checkAnswer
from questions_answers import questionAndAnswer
from random import choice

print("Guess the animal")
print("\nQuiz instructions:")
print("You have 3 lives throughout the game")
print("Which you can use when you miss a question")
print("Quiz ends when you miss the question and don't have any live to sustain the quiz")
print("Or you can enter 'q' to end the quiz at anytime")
print("Goodluck!\n")

score = 0
while True:
    question, answer = choice(list(questionAndAnswer.items()))
    guess = input(f"{question}: ")
    checkAnswer(guess, answer)