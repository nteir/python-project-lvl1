#!/usr/bin/env python
import brain_games.common
import brain_games.games.logic_even


def main():
    username = brain_games.common.welcome_user()
    brain_games.games.logic_even.play_even(username)


if __name__ == '__main__':
    main()
