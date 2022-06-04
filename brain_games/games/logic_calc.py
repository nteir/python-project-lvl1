import random

# Random numbers range:
RANDOM_LOWER = 1
RANDOM_UPPER = 100
TASK = 'What is the result of the expression?'


def generate_qa():
    num1 = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    num2 = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    operand = random.choice(['+', '-', '*'])
    question = f"{num1} {operand} {num2}"
    correct_answer = str(eval(question))
    return question, correct_answer
