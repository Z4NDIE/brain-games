from random import randint, choice
from operator import add, sub, mul

RULES = 'What is the result of the expression?'


def question_and_correct_answer():
    min_number = 1
    max_number = 10
    first_number = randint(min_number, max_number)
    second_number = randint(min_number, max_number)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    correct_answer = operation(first_number, second_number)
    question = f'{first_number} {operator} {second_number}'
    return question, str(correct_answer)
