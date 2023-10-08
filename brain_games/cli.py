#!/usr/bin/env python3
import prompt


def welcome_user():
    global username
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
