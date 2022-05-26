import prompt

ROUND_NUM = 3    # max number of rounds


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    return input('Your answer: ')


def check_answer(received, expected):
    if received == expected:
        print('Correct!')
        return True
    else:
        print(f"'{received}' is wrong answer ;(. Correct answer was '{expected}'.")
        return False


def say_bye(win, username):
    if win:
        print(f'Congratulations, {username}!')
    else:
        print(f"Let's try again, {username}!")
