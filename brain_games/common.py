import prompt

ROUNDS_COUNT = 3    # max number of rounds


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


def run_game(task, qa_func):
    username = welcome_user()
    print(task)
    question_num = 1
    win = True   # optimistic, are we?
    while question_num < ROUNDS_COUNT + 1:
        question, correct_answer = qa_func()
        ask_question(question)
        answer = get_answer()
        result = check_answer(answer, correct_answer)
        if not result:
            win = False
            break
        question_num += 1
    if win:
        print(f'Congratulations, {username}!')
    else:
        print(f"Let's try again, {username}!")
