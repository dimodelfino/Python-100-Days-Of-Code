from art import logo
import random as rd

LEVEL_ATTEMPTS = {'easy': 10, 'hard': 5}

def verify_difficulty_input(diff_selected):
    while diff_selected not in ['easy', 'hard']:
        diff_selected = input('Invalid input. Choose a difficulty level. Type \'easy\' or \'hard\': ').lower()
    return diff_selected

def verify_keep_playing_input(choice):
    while diff_selected not in ['y', 'n']:
        diff_selected = input('Invalid input. Choose \'y\' or \'n\': ').lower()
    return diff_selected

def validate_int(value):
    is_valid = False
    while not is_valid:
        try:
            value = int(value)
            is_valid = True
        except ValueError:
            value = input('Invalid input. Please enter a valid integer \n')

    return value

def validate_guess(guess, num_to_guess):
    is_correct = False
    if guess < num_to_guess:
        print('Too low.\nGuess again.\n')
    elif guess > num_to_guess:
        print('Too high.\nGuess again.\n')
    else:
        print(f'Correct, you guessed! The number was {num_to_guess}.')
        is_correct = True
    return is_correct

def guessing_game():
    print(logo)
    keep_playing = 'y'
    while keep_playing == 'y':
        print('Welcome to the Number Guessing Game!')
        print('I\'m thinking of a number between 1 and 100.')
        difficulty_level = verify_difficulty_input(input('Choose a difficulty level. Type \'easy\' or \'hard\': ')).lower()
        remaining_attempts = LEVEL_ATTEMPTS[difficulty_level]
        number_to_guess = rd.randint(1, 100)
        guessed = False
        while remaining_attempts > 0 and not guessed:
            print(f'You have {remaining_attempts} attempts remaining to guess the number.')
            current_guess = validate_int(input('Guess a number between 1 and 100: '))
            guessed = validate_guess(current_guess, number_to_guess)
            if not guessed:
                remaining_attempts -= 1

        if not guessed:
            print(f"Sorry, you're out of attempts. The number was {number_to_guess}.\n")

        keep_playing = verify_keep_playing_input(input('Choose \'y\' or \'n\': ')).lower()
        print("\n" * 20)

    print('Thanks for playing, hope you had fun!')


guessing_game()










