import random


def deal_card():
    ''''Returns a random card from deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards): #will return changed_score
    '''Takes a list of cards and returns total score. Also checks for blackjack and deals with Ace card(11) condition'''
    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Ace card 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Initialise both player and computer with two cards each
player_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]

is_game_over = False
while not is_game_over:
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        player_deal_choice = input("Type 'y' for another card, type 'n' for pass: ").lower()
        if player_deal_choice == 'y':
            player_cards.append(deal_card())
        else:
            is_game_over = True

# def compare_result(user_card, computer_card):
#     user = calculate_score(user_card)
#     computer = calculate_score(computer_card)

#     if blackout(computer_card):
#         return "Computer wins with blackout"
#     elif blackout(user_card):
#         return "You Win with blackout"
#     elif user == computer:
#         return "Draw"
#     elif user > 21 and computer > 21:
#         return "You both get over 21 You lose"
#     elif computer > 21:
#         return "Computer get over. You win"
#     elif user > 21:
#         return "You  get over 21. You lose"
#     elif user > computer:
#         return "You Win"
#     else:
#         return "You lose"


# print("______________ Start Game ___________")

# user_score = calculate_score(player_cards)
# computer_score = calculate_score(computer_cards)

# while True:
#     print("Your Cards", player_cards)
#     print(f"Your score so far is {user_score}")
#     print("Computer's first card", computer_cards[0])

#     if 
#     option = input("hit (y) or show (n)").lower()
#     if option == 'y':
#         player_cards.append(deal_card())
#         user_score = calculate_score(player_cards)

#     else:
#         while computer_score <= 16:
#             computer_cards.append(deal_card())
#             computer_score = calculate_score(computer_cards)
#         print(f"computer cards {computer_cards} and score {computer_score}")
#         print(compare_result(player_cards, computer_cards))
#         break





