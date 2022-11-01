import random
import os

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


def compare(player_score, computer_score):
    '''Takes player and computer's score, compares and return appropriate result message.'''

    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose!, Computer wins with Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over 21. You Lose 😭"
    elif computer_score > 21:
        return "Computer went over. You Win 😁"
    elif player_score > computer_score:
        return "You Win 😃"
    else:
        return "You Lose 😤"


def play_game():
    '''Starts the Blackjack Game'''
    # Initialise both player and computer with two cards each
    print("____________________ Start Game ____________________")
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # Player's term
    is_game_over = False
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            # Give more card
            player_deal_choice = input("Type 'y' for another card, type 'n' for pass: ").lower()
            if player_deal_choice == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Computer's term
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Game ends
    print(f"\n    Your final cards: {player_cards}, Final score: {player_score}")
    print(f"    Computer's final card: {computer_cards}, Final score: {computer_score}")
    print(compare(player_score= player_score, computer_score= computer_score))

# Play many time
while input("\nWant to play Blackjack? type 'y' or 'n': ").lower() == 'y':
    os.system("cls")
    play_game()






