import prompt
import brain_games.games.logic_calc
import brain_games.games.logic_even
import brain_games.games.logic_gcd
import brain_games.games.logic_prime
import brain_games.games.logic_progression

ROUND_NUM = 3    # max number of rounds
QA_FUNC_DICT = {
    'calc': brain_games.games.logic_calc.form_qa,
    'even': brain_games.games.logic_even.form_qa,
    'gcd': brain_games.games.logic_gcd.form_qa,
    'prime': brain_games.games.logic_prime.form_qa,
    'progression': brain_games.games.logic_progression.form_qa
}
TASK_DICT = {
    'calc': 'What is the result of the expression?',
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".',
    'progression': 'What number is missing in the progression?'
}


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


def run_game(username, game):
    print(TASK_DICT[game])
    question_num = 1
    answer = ''
    win = False   # did the user win all 3 rounds?
    while question_num < ROUND_NUM + 1:
        question, correct_answer = QA_FUNC_DICT[game]()
        ask_question(question)
        answer = get_answer()
        result = check_answer(answer, correct_answer)
        if not result:
            break
        question_num += 1
    if question_num > ROUND_NUM:
        win = True
    say_bye(win, username)
