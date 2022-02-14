import random
from currency_converter import CurrencyConverter


def get_money_interval(chosen_difficulty):
    real_time_data = CurrencyConverter()
    real_time_data = real_time_data.convert(1, 'USD', 'ILS')
    random_num = int(random.randint(1, 100))
    t = random_num * real_time_data
    mini = int(t - (5 - chosen_difficulty))
    maxi = int(t + (5 - chosen_difficulty))
    return random_num, t, mini, maxi


def get_guess_from_user(random_num):
    while True:
        try:
            user_guess = int(input(f"Guess the value of {random_num}$ in ILS: "))
        except ValueError:
            print("Invalid chars, please enter numbers only!")
            continue
        return user_guess


def play(chosen_difficulty):
    random_num, t, mini, maxi = get_money_interval(chosen_difficulty)
    user_guess = get_guess_from_user(random_num)
    if maxi >= user_guess >= mini:
        print(True)
    else:
        print(False)
