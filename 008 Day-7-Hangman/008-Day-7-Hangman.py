import random
from hangman_stages import stages, logo
from hangman_words import words_list

print(logo)
print("Welcome to The Hangman Game. Guess correct letters to save the man from hanging!! ")

#Choosing random word from the list
word_list = words_list      
to_guess = random.choice(word_list)

#Track of correctly choosen words
guessed_list = ["_"]*len(to_guess)
life = 6

# main logic
end_of_game = False
while not end_of_game:
    user_guessing = input("\nGuess a letter: ").lower()
    end_life = True

    #Check for correct guess
    for i in range(len(to_guess)):
        if user_guessing == to_guess[i]:
            guessed_list[i] = user_guessing
            end_life = False

    #Check for remaining life
    if end_life:
        life -= 1
        if life <= 0:
            print("You lose !!")
            end_of_game = True

    print(f"{' '.join(guessed_list)}")

    #All letters guessed
    if "_" not in guessed_list:
        end_of_game = True
        print("You Won !!")

    #How's The Hangman
    print(stages[life])

print("Correct word: ", to_guess)
