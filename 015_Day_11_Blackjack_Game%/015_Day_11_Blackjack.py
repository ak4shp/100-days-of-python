import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def blackout(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return True


def calculate_score(terms_card): #will return changed_score:
    if 11 in terms_card and sum(terms_card) > 21:
        terms_card.remove(11)
        terms_card.append(1)
    return sum(terms_card)


def compare_result(user_card, computer_card):
    user = calculate_score(user_card)
    computer = calculate_score(computer_card)

    if blackout(computer_card):
        return "Computer wins with blackout"
    elif blackout(user_card):
        return "You Win with blackout"
    elif user == computer:
        return "Draw"
    elif user > 21 and computer > 21:
        return "You both get over 21 You lose"
    elif computer > 21:
        return "Computer get over. You win"
    elif user > 21:
        return "You  get over 21. You lose"
    elif user > computer:
        return "You Win"
    else:
        return "You lose"


player_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]

print("______________ Start Game ___________")

user_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)

while True:
    print("Your Cards", player_cards)
    print(f"Your score so far is {user_score}")
    print("Computer's first card", computer_cards[0])

    option = input("hit (y) or show (n)").lower()
    if option == 'y':
        player_cards.append(deal_card())
        user_score = calculate_score(player_cards)

    else:
        while computer_score <= 16:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"computer cards {computer_cards} and score {computer_score}")
        print(compare_result(player_cards, computer_cards))
        break





