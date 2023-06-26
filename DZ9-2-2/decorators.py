import random

def save_params(func):
    def wrapper(*args, **kwargs):
        wrapper.secret = kwargs.get('secret')
        wrapper.attempts = kwargs.get('attempts')
        return func(*args, **kwargs)

    return wrapper

def validate_input(func):
    def wrapper(*args, **kwargs):
        secret = kwargs.get('secret')
        attempts = kwargs.get('attempts')

        if secret < 1 or secret > 100 or attempts < 1 or attempts > 10:
            print("Введены неподходящие числа. Загаданы случайные числа из диапазонов [1, 100] и [1, 10].")
            secret = random.randint(1, 100)
            attempts = random.randint(1, 10)
            kwargs['secret'] = secret
            kwargs['attempts'] = attempts

        return func(*args, **kwargs)

    return wrapper

def play_multiple_times(func):
    def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
            play_again = input("Хотите сыграть еще раз? (yes/no): ")
            if play_again.lower() != "yes":
                break

    return wrapper

def notify_initial_attempts(func):
    def wrapper(*args, **kwargs):
        attempts = kwargs.get('attempts')
        print(f"У вас {attempts} попыток.")
        print("Угадайте число от 1 до 100.")
        return func(*args, **kwargs)

    return wrapper

def display_remaining_attempts(func):
    def wrapper(*args, **kwargs):
        secret = kwargs.get('secret')
        attempts = kwargs.get('attempts')
        count = 0
        guessed_attempts = 0

        while count < attempts:
            remaining_attempts = attempts - count
            print(f"У вас осталось {remaining_attempts} попыток.")

            guess = int(input("Введите число: "))
            kwargs['guess'] = guess

            guess_correctly = func(*args, **kwargs)

            if guess_correctly:
                guessed_attempts = count + 1
                break
            elif count < attempts - 1:
                if guess < secret:
                    print("Загаданное число больше.")
                else:
                    print("Загаданное число меньше.")

            count += 1

        if guess_correctly:
            print(f"Поздравляю, вы угадали число! Это заняло {guessed_attempts} попыток.")
        else:
            print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret}.")

    return wrapper
