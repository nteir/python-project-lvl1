import random
import math
import brain_games.common

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 100


def play_gcd(username):
    print('Find the greatest common divisor of given numbers.')
    question_num = 1
    answer = ''
    win = False   # did the user win all 3 rounds?
    while question_num < brain_games.common.ROUND_NUM + 1:
        num1 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
        num2 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
        question = str(num1) + ' ' + str(num2)
        brain_games.common.ask_question(question)
        correct_answer = math.gcd(num1, num2)
        answer = brain_games.common.get_answer()
        result = brain_games.common.check_answer(answer, correct_answer)
        if not result:
            break
        question_num += 1
    if question_num > brain_games.common.ROUND_NUM:
        win = True
    brain_games.common.say_bye(win, username)
