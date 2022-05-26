#!/usr/bin/env python
import brain_games.common


def main():
    username = brain_games.common.welcome_user()
    brain_games.common.play_even(username)


if __name__ == '__main__':
    main()
