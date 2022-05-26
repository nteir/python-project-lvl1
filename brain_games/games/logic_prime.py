import random
import brain_games.common

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 15


def play_prime(username):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question_num = 1
    answer = ''
    win = False   # did the user win all 3 rounds?
    while question_num < brain_games.common.ROUND_NUM + 1:
        num = random.randrange(RAND_LOWER, RAND_UPPER + 1)
        brain_games.common.ask_question(str(num))
        correct_answer = 'yes' if is_prime(num) else 'no'
        answer = brain_games.common.get_answer()
        result = brain_games.common.check_answer(answer, correct_answer)
        if not result:
            break
        question_num += 1
    if question_num > brain_games.common.ROUND_NUM:
        win = True
    brain_games.common.say_bye(win, username)


def is_prime(num):
    if num == 1:
        return False    # 1 is not a prime
    half = num / 2
    i = 2
    while i <= half:
        if num % i == 0:
            return False
        i += 1
    return True    # no divisor was found in while loop
