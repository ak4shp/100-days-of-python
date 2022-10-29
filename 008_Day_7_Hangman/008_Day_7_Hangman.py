import os
import random
from hangman_arts import stages, logo
from hangman_words import words_list
from hangman_word_meaning import get_meaning

print(logo)
print("Welcome to The Hangman Game. Guess correct letters to save the man from hanging!! ")

#Choosing random word from the list
word_list = words_list      
to_guess = random.choice(word_list)

#Track of correctly choosen words
guessed_list = ["_"]*len(to_guess)
life = 6

'''__MAIN Logic__'''
end_of_game = False
while not end_of_game:
    user_guessing = input("\nGuess a letter: ").lower()
    end_life = True

    #Clear the screen
    os.system("cls")

    #Check for already guessed letter
    if user_guessing in guessed_list:
        print(f"You've already chosen '{user_guessing}'. Ummh... Try out something else!")

    #Check for correct guess
    for i in range(len(to_guess)):
        if user_guessing == to_guess[i]:
            guessed_list[i] = user_guessing
            end_life = False

    #Check for remaining life
    if end_life:
        print(f"You guess '{user_guessing}', that's not in the word. You lose a Life :(")
        life -= 1
        if life <= 0:
            print("\nYou LOSE !!")
            end_of_game = True

    #Print all guessed letters so far with correct position
    print(f"{' '.join(guessed_list)}")

    #All letters guessed
    if "_" not in guessed_list:
        end_of_game = True
        print("\nYou WON !!")

    #How's the Hangman doing
    print(stages[life])

#Correct word
print("Correct word: ", to_guess)

#Get word meaning
print(f"\nPress (1) for meanings of '{to_guess}'\n Press any key to exit.")
meaning = input()
if meaning == '1':
    os.system("cls")
    get_meaning(to_guess)


input("Press enter to proceed...")
