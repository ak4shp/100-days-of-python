# to-do
# -> import ramdom, game data
import random
from game_data import data

# 1. random generate a data from game data 
def generate_subject():
    to_compare = random.choice(data)
    # print("+++++", to_compare)
    while to_compare['used']:
        to_compare = random.choice(data)
    idx = data.index(to_compare)
    data[idx]['used'] = True
    return to_compare
#       -> that was not used previously

subject_A = generate_subject()
subject_B = generate_subject()

# print(subject_A, "\n", subject_B)

# 2. show with whom to compare with formate : <name>, a <prefession>, from <country>.
#       -> Vs
#       whom to compare
def start(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}. -{A['follower_count']}-")
    print("\nVs\n")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}. -{B['follower_count']}-")
    player_choice = input("Choose A or B: ").upper()
    return player_choice

# 3. Compare function : compare by followers count in dict. return boolean.
def compare(A, B, user):
    A_followers = A["follower_count"]
    B_followers = B["follower_count"]
    
    winner = None
    if A_followers > B_followers:
        more_followers = "A"
        winner = A
    else:
        more_followers = "B"
        winner = B
    # print("inside sompare fn-----, user, winner", user, more_followers)
    if user == more_followers:
        return True, winner
    return False, None

# 4. play game() if guess guess is wrong end game with total score.

def play_game():
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
        res, winner= compare(subject_A, subject_B, user)
        # tr: score += 1
        if res:
            score += 1
            subject_A = winner
            subject_B = generate_subject() 
        #  fl : show score, return
        else:
            print("Total score: ", score)
            game_loop = False

play_game()
