import random

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 100


def form_qa():
    num1 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    num2 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    operand = random.choice(['+', '-', '*'])
    question = str(num1) + ' ' + operand + ' ' + str(num2)
    correct_answer = str(eval(question))
    return question, correct_answer
