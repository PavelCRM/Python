import random
from game_logic import create_guessing_game
from decorators import save_params, validate_input, play_multiple_times


@save_params
@validate_input
@play_multiple_times
def guessing_game(secret, attempts):
    while attempts > 0:
        guess = int(input("Угадайте число от 1 до 100: "))
        attempts -= 1

        if guess == secret:
            print("Поздравляю, вы угадали число!")
            return
        elif guess < secret:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret}.")


# Пример использования
secret = int(input("Введите число для загадывания (от 1 до 100): "))
attempts = int(input("Введите количество попыток (от 1 до 10): "))

guessing_game(secret=secret, attempts=attempts)
