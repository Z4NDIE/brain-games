from random import randint
from math import gcd

RULES = 'Find the greates common divisor of given numbers.'


def question_and_correct_answer():
    min_number = 1
    max_number = 10
    first_number = randint(min_number, max_number)
    second_number = randint(min_number, max_number)
    question = f'{first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)
    return question, str(correct_answer)
