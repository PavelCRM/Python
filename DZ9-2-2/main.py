import random
from decorators import save_params, validate_input, play_multiple_times, notify_initial_attempts, display_remaining_attempts

@save_params
@validate_input
@play_multiple_times
@notify_initial_attempts
@display_remaining_attempts
def guessing_game(secret, attempts, guess):
    if guess is not None:
        if guess == secret:
            return True
        else:
            return False

secret = random.randint(1, 100)
attempts = 9

guessing_game(secret=secret, attempts=attempts, guess=None)
