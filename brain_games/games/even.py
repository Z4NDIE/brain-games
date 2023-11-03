from random import randint

RULES = "Answer 'yes' if the number even otherwise answer 'no'."


def question_and_correct_answer():
    min_number = 1
    max_number = 100
    number = randint(min_number, max_number)
    question = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
