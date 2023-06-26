import random

def create_guessing_game(secret_number, max_attempts):
    attempts = 0

    def guessing_game():
        nonlocal attempts
        while attempts < max_attempts:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1

            if guess == secret_number:
                print("Поздравляю, вы угадали число!")
                return
            elif guess < secret_number:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")

        print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret_number}.")

    return guessing_game
