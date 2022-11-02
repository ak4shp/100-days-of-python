import random
welcome = """Welcome to the number guessing game!
I'm thinking of a number between 1 and 100. Can you guess it?"""
print(welcome)

NUMBER = random.randint(1, 100)
attempts = 10

difficulty = input("Choose a difficulty. Type 'e' for easy, 'm' for moderate, 'h' for hard.: ").lower()
if difficulty == 'e':
    attempts = 10
elif difficulty == 'm':
    attempts = 7
elif difficulty == 'h':
    attempts = 4

print(NUMBER, attempts)

should_end_game = False

while not should_end_game:
    
    guessed_num = int(input("Make a guess: "))
    if guessed_num == NUMBER:
        print("You got it! The number is ", NUMBER)
        should_end_game = True
    elif guessed_num < NUMBER:
        print("Too low. Try again!")
    else:
        print("Too high !! Try again.")

    
    

