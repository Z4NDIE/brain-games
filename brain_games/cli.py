#!/usr/bin/env python3

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')


if __name__ == '__main__':
    welcome_user()
