import random

#Options
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
options = ["rock", "paper", "scissors"]

#Play
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

#Check for limits of choice by user
if you < 0 or you >= 3:
    print("You typed a wrong number. You lose")
    
else:
    #prints images
    print("You chose: " + options[you])
    print(game_images[you])
    print("Computer chose: " + options[computer])
    print(game_images[computer])

    #Main logic
    if you == computer:
        print("It's a draw")
    elif (you == 0 and computer == 2) or (you == 2 and computer == 1) or (you == 1 and computer == 0):
        print("You won")
    else:
        print("You lose")


