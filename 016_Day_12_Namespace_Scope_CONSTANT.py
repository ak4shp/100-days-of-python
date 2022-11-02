"""_____________ Scope ____________"""
''' NOTE : There is no separate Block space in python for IF-else, Loops etc.
They are are considered in that functions local space.
Only when function is created then a Local scope comes.'''


# Global Scope -->
player_health = 100
user = "Gamer999"
enemies = 1   # Global 
print(f"Enemies in global -> {enemies}, global name -> {user}, and total health {player_health}")

def drink_potion(): # Local Scope -->
    '''Trying to modify global variable in local scope --> causes "UnboundLocalError".'''
    enemies = 2  # Local (completely new variable)
    user = "Player001"
    potion_strength = 50
    if player_health < 30: #UnboundLocalError: local variable 'player_health' referenced before assignment.
        player_health += potion_strength
    print(f"Fn1: Enemies in local -> {enemies}, local name -> {user} and health {player_health}")


def drink_potion_2(): # Local Scope -->
    '''Modifies global variable in local scope --> using "global" keyword. 
        But it is not recommanded to modify global variable this way.'''
    global player_health
    player_health = 20
    enemies = 2  # Local (completely new variable)
    user = "Player"
    potion_strength = 50
    if player_health < 30:
        player_health += potion_strength
    print(f"Fn2: Enemies in local -> {enemies}, local name -> {user}, and new health {player_health}")

drink_potion_2()
print(f"Fn2: Updated health of player is {player_health}.")


def drink_potion_3(players_health): # Local Scope -->
    '''Right way to modify global variable in local scope.
    >> pass in parameters
    >> modify 
    >> return modified value and store in a new variable.'''
    enemies = 2  # Local (completely new variable)
    user = "Player"
    potion_strength = 50
    if players_health < 30:
        players_health += potion_strength
    print(f"Fn3: Enemies in local -> {enemies}, local name -> {user}, and new health {players_health}")
    return players_health

new_health = drink_potion_3(players_health = player_health)
# player_health = drink_potion_3(players_health = player_health)  #You can also reassign to the same variable.
print(f"Fn3: Updated health of player is {new_health}.")


"""_____________ CONSTANTS ____________"""

"""Never modify a constant, never!"""
PI = 3.1432
URL = "https:\\\\www.ekkhiokavita.blogspot.com"
GITHUB_ID = "https://github.com/ak4shp"
