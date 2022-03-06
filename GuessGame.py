def generate_number(chosen_difficulty):
    import random
    secret_number = int(random.randint(1, chosen_difficulty))
    return secret_number


def get_guess_from_user(chosen_difficulty):
    number = int(input(f"Guess a number from 1 to {chosen_difficulty}: "))
    return number


def compare_results(secret_number, number):
    if secret_number == number:
        return True
    else:
        return False


def play(chosen_difficulty):

    secret_number = generate_number(chosen_difficulty)
    number = get_guess_from_user(chosen_difficulty)
    print(compare_results(secret_number, number))
    if compare_results(secret_number=secret_number, number=number):
        return True
    else:
        return False


