#!/usr/bin/env python3
import random
import prompt


from brain_games.cli import welcome_user


def rules():
    print('Answer "yes" if number even otherwise answer "no".')


def question():
    global random_number
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')

    global user_answer
    user_answer = prompt.string('Your answer: ')

    if random_number % 2 == 0:
        if user_answer == 'yes':
            print('Correct!')
            question()
        else:
            print(f''''no' is wrong answer ;'('. Correct answer is 'yes'.
                Let's try again, {welcome_user.name}!''')

    if random_number % 2 != 0:
        if user_answer == 'no':
            print('Correct!')
            question()
        else:
            print("'yes' is wrong answer ;(. Correct answer is 'no'.")


def main():
    welcome_user()
    rules()
    question()


if __name__ == '__main__':
    main()
