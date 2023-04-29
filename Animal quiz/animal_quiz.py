from check_answer import checkAnswer
from questions_answers import questionAndAnswer
from random import choice

print("Guess the animal")
print("\nQuiz instructions:")
print("You have 3 lives through out the game")
print("Lives are accessible when you miss the question")
print("Quiz ends when you miss the question and don't have any live to sustain the quiz")
print("You can enter 'q' to end the quiz at anytime")
print("Goodluck!\n")

while True:
    question, answer = choice(list(questionAndAnswer.items()))
    guess = input(f"{question}: ")
    checkAnswer(guess, answer)