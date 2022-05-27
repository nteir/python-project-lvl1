import random

# Random numbers range:
RAND_LOWER = 1
RAND_UPPER = 15


def form_qa():
    num = random.randrange(RAND_LOWER, RAND_UPPER + 1)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer


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
