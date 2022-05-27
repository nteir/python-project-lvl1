#!/usr/bin/env python
import brain_games.common
import brain_games.games.logic_calc


def main():
    username = brain_games.common.welcome_user()
    brain_games.common.run_game(username, 'calc')


if __name__ == '__main__':
    main()
