#!/usr/bin/env python
import brain_games.common
import brain_games.games.logic_gcd


def main():
    username = brain_games.common.welcome_user()
    brain_games.games.logic_gcd.play_gcd(username)


if __name__ == '__main__':
    main()
