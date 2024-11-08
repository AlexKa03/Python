from random import randint
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, correct_number, turns_left):
    """Checks the user answer and updates the turns accordingly."""
    if user_guess > correct_number:
        print("Too High!")
        return turns_left - 1
    elif user_guess < correct_number:
        print("Too Low!")
        return turns_left - 1
    else:
        print(f"YOU WIN! You have guessed the number - {correct_number}")

def difficulty_selector():
    """Sets the total turns that the user will have based on the user difficulty selection."""
    difficulty = input("Please select your difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    """This is the game core code"""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("The chosen number is between 1 and 100.")
    answer = randint(1, 100)
    print(f"DEBUGGING FEATURE! Correct answer is {answer}")

    turns = difficulty_selector()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("YOU LOSE! You have no remaining turns.")
            return
        elif guess != answer:
            print(f"TRY AGAIN! Number {guess} is not the correct number.")



game()