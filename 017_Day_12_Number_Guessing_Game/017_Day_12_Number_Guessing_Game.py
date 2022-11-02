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
