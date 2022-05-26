#!/usr/bin/env python
import brain_games.common
import brain_games.games.logic_progression


def main():
    username = brain_games.common.welcome_user()
    brain_games.games.logic_progression.play_progression(username)


if __name__ == '__main__':
    main()
