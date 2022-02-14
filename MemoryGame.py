import time


def generate_sequence(chosen_difficulty):
    import random
    random_numbers = []
    for number in range(chosen_difficulty):
        random_numbers.append(int(random.randint(1, 101)))
    print(random_numbers, "Remember this number/s!", end="")
    time.sleep(0.7)
    print("\r", end="")
    return random_numbers


def get_list_from_user(chosen_difficulty):
    user_numbers = []
    print(f" Please enter {chosen_difficulty} numbers")
    for x in range(chosen_difficulty):
        x = user_numbers.append(int(input("Enter a Number: ")))
    return user_numbers


def is_list_equal(random_numbers, user_numbers):
    random_numbers.sort()
    user_numbers.sort()
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(chosen_difficulty):
    random_numbers = generate_sequence(chosen_difficulty)
    user_numbers = get_list_from_user(chosen_difficulty)
    print(is_list_equal(random_numbers, user_numbers))
