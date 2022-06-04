import random

# Random numbers range:
RANDOM_LOWER = 1
RANDOM_UPPER = 100
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_qa():
    num = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    question = str(num)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return question, correct_answer
