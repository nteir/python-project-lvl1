import random
import brain_games.common

PROGRESSION_LEN = 10
STEP_RANGE = (2, 7)
START_RANGE = (1, 15)    # first number in progression


def play_progression(username):
    print('What number is missing in the progression?')
    question_num = 1
    answer = ''
    win = False   # did the user win all 3 rounds?
    while question_num < brain_games.common.ROUND_NUM + 1:
        step = random.randrange(STEP_RANGE[0], STEP_RANGE[1])
        prog_str, hidden_num = build_progression_string(PROGRESSION_LEN, step)
        brain_games.common.ask_question(prog_str)
        correct_answer = hidden_num
        answer = brain_games.common.get_answer()
        result = brain_games.common.check_answer(answer, correct_answer)
        if not result:
            break
        question_num += 1
    if question_num > brain_games.common.ROUND_NUM:
        win = True
    brain_games.common.say_bye(win, username)


def build_progression_string(length, step):
    hidden_num_index = random.randrange(0, length)
    hidden_num = 0
    start = random.randrange(START_RANGE[0], START_RANGE[1])
    prog_str = ''
    prog_head = start
    for i in range(0, length):
        if i == hidden_num_index:
            prog_str += '.. '
            hidden_num = prog_head
        else:
            prog_str += str(prog_head) + ' '
        prog_head += step
    prog_str = prog_str.strip()
    # returns question string and the missing number
    return prog_str, hidden_num
