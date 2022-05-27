import random
import math

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 100


def form_qa():
    num1 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    num2 = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    question = str(num1) + ' ' + str(num2)
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
