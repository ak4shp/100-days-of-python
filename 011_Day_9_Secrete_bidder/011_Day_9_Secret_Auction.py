import os
from Secret_Auctio_art import logo

print(logo)
print("Welcome to the Secret Auction programm.\n\n")
bidders = {}

def find_winner(bidders):
    winner_name = ''        
    winner_amount = 0
    for w_name in bidders:
        amount = bidders[w_name]
        if amount >= winner_amount:
            winner_amount = amount
            winner_name = w_name

    print(f"The winner is {winner_name} with a bid of ${winner_amount}.")

more_bidders = True
while more_bidders:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bidders[bidder_name] = bid_amount

    other_bidders = input("\nAre there any other bidders? \nType 'no' to end bid or press any key to continue bidding...\n").lower()
    os.system("cls")

    if other_bidders == 'no':
        more_bidders = False
        find_winner(bidders)
        