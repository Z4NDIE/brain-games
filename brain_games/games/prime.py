from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return 'no'
    return 'yes'


def question_and_correct_answer():
    min_number = 3
    max_number = 31
    number = randint(min_number, max_number)
    question = number
    return question, is_prime(number)
