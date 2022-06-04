import random
import math

# Random numbers range:
RANDOM_LOWER = 1
RANDOM_UPPER = 15
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa():
    num = random.randrange(RANDOM_LOWER, RANDOM_UPPER + 1)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


def is_prime(num):
    if num == 1:
        return False    # 1 is not a prime
    lower = math.sqrt(num)
    i = 2
    while i <= lower:
        if num % i == 0:
            return False
        i += 1
    return True    # no divisor was found in while loop
