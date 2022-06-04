import random
import math

# Random numbers range:
RANDOM_LOWER = 1
RANDOM_UPPER = 100
TASK = 'Find the greatest common divisor of given numbers.'


def generate_qa():
    num1 = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    num2 = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
