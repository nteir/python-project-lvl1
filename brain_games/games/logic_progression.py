import random

PROGRESSION_LEN = 10
STEP_RANGE = (2, 7)
START_RANGE = (1, 15)    # first number in progression
TASK = 'What number is missing in the progression?'


def generate_qa():
    step_min, step_max = STEP_RANGE
    start_min, start_max = START_RANGE
    step = random.randrange(step_min, step_max)
    hidden_num_index = random.randrange(0, PROGRESSION_LEN)
    hidden_num = 0
    start = random.randrange(start_min, start_max)
    prog_str = ''
    prog_head = start
    for i in range(0, PROGRESSION_LEN):
        if i == hidden_num_index:
            prog_str += '.. '
            hidden_num = prog_head
        else:
            prog_str += str(prog_head) + ' '
        prog_head += step
    prog_str = prog_str.strip()
    return prog_str, str(hidden_num)
