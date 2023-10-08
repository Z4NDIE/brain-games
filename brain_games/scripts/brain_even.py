#!/usr/bin/env python3
import random
import prompt
from brain_games import cli
from brain_games.cli import welcome_user

def rules():
    print('Answer "yes" if number even otherwise answer "no".')


def question():
    global random_number
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')

global user_answer
    user_answer = prompt.string('Your answer: ')


def even_or_odd():
    for x in range(3):
        question() 
        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            continue
        elif random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            continue
        elif random_number % 2 == 0 and user_answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {cli.username}!")
            break
        elif random_number % 2 != 0 and user_answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {cli.username}!")
            break
        elif user_answer != 'yes' and user_answer != 'no':
            print('This is the wrong answer ;(.')
            print(f"Let's try again, {cli.username}!")
            break



def main():
    welcome_user()
    rules()
    question()


if __name__ == '__main__':
    main()
