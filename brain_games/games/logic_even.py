import random
import brain_games.common

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 100


def play_even(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = 1
    answer = ''
    win = False   # did the user win all 3 rounds?
    while question_num < brain_games.common.ROUND_NUM + 1:
        num = random.randrange(RAND_LOWER, RAND_UPPER + 1)
        brain_games.common.ask_question(str(num))
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        answer = brain_games.common.get_answer()
        result = brain_games.common.check_answer(answer, correct_answer)
        if not result:
            break
        question_num += 1
    if question_num > brain_games.common.ROUND_NUM:
        win = True
    brain_games.common.say_bye(win, username)
