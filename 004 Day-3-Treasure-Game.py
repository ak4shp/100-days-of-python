print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[AAKASH]
*******************************************************************************
''')

welcome = "\n\n@@@ Welcome to the treasure game @@@ !!\nYou can choose 'left' or 'right'...\n"
choice1 = input(welcome).lower()
if choice1 == "left":
    stage1 = "Hurray !! You've reached the Great Mesito Lake. You can 'wait' for boat or 'swim'.\n"
    choice2 = input(stage1).lower()
    
    if choice2 == "wait":
        stage2 = '''Wow !! You showed great patience. Boat has arrived, you can onboard it and go to the next stage.
tin tin tin ....\nThere are three doors. 'red' 'yellow' and 'green'. Open one. Hurry up !!\n'''
        choice3 = input(stage2).lower()
        
        if choice3 == "red":
            print("You're in a room of fire!! You're burnt. You lost :(")
        elif choice3 == "yellow":
            print("Heyyy !! You got The Great Treasure. YOU WON :)")
        elif choice3 == "green":
            print("You're in a room with hungry lions. They're gonna eat you without salt and pepper. You lost :(")
        else:
            print("There is no such door. You lost :(")
            
    else:
        print("So impatient. There is a dangerous Croc. She'll eat you. You lost :(")
        
else:
    print("Oops !! You fallen into a ditch. Game over :(")

