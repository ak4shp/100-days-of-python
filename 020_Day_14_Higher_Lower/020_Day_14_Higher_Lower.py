# to-do
# -> import ramdom, game data
import os
import random
from game_data import data
from art import logo, vs


# 1. random generate a data from game data 
def generate_subject():
    """Returns a random account from data that has never been previously used."""
    to_compare = random.choice(data)
    #  -> that was not used previously
    while to_compare['used']:
        to_compare = random.choice(data)
    idx = data.index(to_compare)
    data[idx]['used'] = True
    return to_compare

# 2. show with whom to compare with formate : <name>, a <prefession>, from <country>.
def start(A, B):
    """Takes two accounts, Prints formatted message, ask user to choose and returns user's choice"""
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    player_choice = input("Choose A or B: ").upper()
    return player_choice

# 3. Compare function : compare by followers count in dict. return boolean.
def compare(A, B, user):
    """Takes two accounts and user's choice, compare user's choice with higher follower account. Returns boolean."""
    A_followers = A["follower_count"]
    B_followers = B["follower_count"]
    
    # winner = None
    if A_followers > B_followers:
        more_followers = "A"
        # winner = A
    else:
        more_followers = "B"
        # winner = B

    if user == more_followers:
        return True
    return False

# 4. play game() if guess guess is wrong end game with total score.
def play_game():
    """Main game starts"""
    print(logo)
    # random A, B
    subject_A = generate_subject()
    subject_B = generate_subject()  
    score = 0
    # Loop start ...
    game_loop = True
    while game_loop:
        # clear screen
        # show msg()
        user = start(subject_A, subject_B)
        # compare(A, B) Tr, Fl
        res = compare(subject_A, subject_B, user)
        os.system("cls")
        print(logo)
        if res: 
            score += 1
            subject_A = subject_B
            subject_B = generate_subject() 
            print(f"You are right! Current score : {score}.")
        else:
            print("Oops! That's wrong. Final score :", score)
            game_loop = False

play_game()
