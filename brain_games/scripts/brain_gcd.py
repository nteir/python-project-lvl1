#!/usr/bin/env python
import brain_games.common
from brain_games.games.logic_gcd import TASK, form_qa


def main():
    brain_games.common.run_game(TASK, form_qa)


if __name__ == '__main__':
    main()
