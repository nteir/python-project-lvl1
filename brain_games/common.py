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
    if str(received) == str(expected):
        print('Correct!')
        return True
    else:
        print(f"'{received}' is wrong answer ;(.", end='')
        print(f"Correct answer was '{expected}'.")
        return False


def say_bye(win, username):
    if win:
        print(f'Congratulations, {username}!')
    else:
        print(f"Let's try again, {username}!")


def run_game(task, qa_func):
    username = welcome_user()
    # print(TASK_DICT[game])
    print(task)
    question_num = 1
    win = True   # optimistic, are we?
    while question_num < ROUND_NUM + 1:
        question, correct_answer = qa_func()
        ask_question(question)
        answer = get_answer()
        result = check_answer(answer, correct_answer)
        if not result:
            win = False
            break
        question_num += 1
    say_bye(win, username)
