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
    correct_answer = 'yes'
    for x in range(3):
        flag = True
        question()
        if random_number % 2 != 0:
            if user_answer == 'no':
                flag = True
                correct()
                continue
            else:
                flag = False
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                game_over()
                break

        elif random_number % 2 == 0:
            if user_answer == correct_answer:
                flag = True
                correct()
                continue
            else:
                flag = False
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                game_over()
                break
    if flag:
        print(f'Congratulation, {cli.username}!')


def correct():
    print('Correct!')


def game_over():
    print(f"Let's try again, {cli.username}!")


def main():
    welcome_user()
    rules()
    even_or_odd()


if __name__ == '__main__':
    main()
