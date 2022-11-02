import random
from Number_Guessing_Game_art import logo

welcome = """Welcome to the number guessing game!
I'm thinking of a number between 1 and 100. Can you guess it?"""
print(logo)
print(welcome)

NUMBER = random.randint(1, 100)
EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURN = 7
HARD_LEVEL_TURN = 4

def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'e' for easy, 'm' for moderate, 'h' for hard.: ").lower()
    if difficulty_level == 'e':
        return EASY_LEVEL_TURNS
    elif difficulty_level == 'm':
        return MEDIUM_LEVEL_TURN
    elif difficulty_level == 'h':
        return HARD_LEVEL_TURN
     

def check_answer(guess, answer):
    if guess > answer:
        print("Too high. Try again.")
    elif guess < answer:
        print("Too low. Try again!")
    else:
        print("You got it! The answer is ", answer)


attempts = set_difficulty()
print(NUMBER)
while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.") 
    guess_number = int(input("Make a guess: "))
    check_answer(guess=guess_number, answer=NUMBER)
    if guess_number == NUMBER:
        break
    attempts -= 1
    if attempts == 0:
        print("Oops! No more guesses are allowed. You lose.")

