#!/usr/bin/env python
import brain_games.common
import brain_games.games.logic_prime


def main():
    username = brain_games.common.welcome_user()
    brain_games.games.logic_prime.play_prime(username)


if __name__ == '__main__':
    main()
