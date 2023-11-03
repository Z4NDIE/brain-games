# Общая логика всех игр Brain-games

import prompt

ATTEMPTS = 3


def game_start(game_name):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game_name.RULES)
    attempt = 1
    while attempt <= ATTEMPTS:
        question, correct_answer = game_name.question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'\n"
                  f"Let's try again, {username}!")
            break
        print('Correct!')
        attempt += 1
    else:
        print(f'Congratulations, {username}!')
