import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_even(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = 1
    answer = ''
    while question_num < 4:
        num = random.randrange(1, 101)
        print(f'Question: {num}')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            question_num += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
    if question_num < 4:
        print(f"Let's try again, {username}!")
    else:
        print(f'Congratulations, {username}!')
