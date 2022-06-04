#!/usr/bin/env python
import brain_games.common
from brain_games.games.logic_even import TASK, generate_qa


def main():
    brain_games.common.run_game(TASK, generate_qa)


if __name__ == '__main__':
    main()
