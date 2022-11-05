# to-do
# -> import ramdom, game data
import random
from game_data import data

# 1. random generate a data from game data 
def generate_unused_name():
    to_compare = random.choice(data)
    return to_compare
#       -> that was not used previously

subject_A = generate_unused_name()
subject_B = generate_unused_name()

print(subject_A, "\n", subject_B)

# 2. show with whom to compare with formate : <name>, a <prefession>, from <country>.
#       -> Vs
#       whom to compare

# 3. Compare function : compare by followers count in dict return boolean.
def compare(A, B):
    A_followers = A["follower_count"]
    B_followers = B["follower_count"]

    if A_followers > B_followers:
        return True
    return False

print(compare(subject_A, subject_B))

# 4. play game() if guess guess is wrong end game with total score.

