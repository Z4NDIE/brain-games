#!/usr/bin/env python3

from brain_games.engine import game_start
from brain_games.games import gcd


def main():
    game_start(gcd)


if __name__ == '__main__':
    main()
