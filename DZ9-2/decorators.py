import random

def save_params(func):
    def wrapper(secret, attempts):
        wrapper.secret = secret
        wrapper.attempts = attempts
        return func(secret, attempts)

    return wrapper

def validate_input(func):
    def wrapper(secret, attempts):
        if secret < 1 or secret > 100 or attempts < 1 or attempts > 10:
            secret = random.randint(1, 100)
            attempts = random.randint(1, 10)
            print("Введены неподходящие числа. Загаданы случайные числа из диапазонов [1, 100] и [1, 10].")

        return func(secret, attempts)

    return wrapper

def play_multiple_times(func):
    def wrapper(secret, attempts):
        while True:
            func(secret, attempts)
            play_again = input("Хотите сыграть еще раз? (да/нет): ")
            if play_again.lower() != "да":
                break

    return wrapper
