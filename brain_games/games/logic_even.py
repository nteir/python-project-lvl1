import random

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 100


def form_qa():
    num = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    question = str(num)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return question, correct_answer
