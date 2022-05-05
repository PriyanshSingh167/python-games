import os
from art import logo

print(logo)

dict = {}

play_again = True

# def clear():
  
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
  
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')

while play_again:
    name = input("What is Your Name?: ")
    bid = int(input("What is your bid?: $"))
    dict[name] = bid
    x = input("Are there any other bidders? Type 'yes' or 'no'.")
    if x == "no":
        play_again = False
    elif x == "yes":
        os.system('cls')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

find_highest_bidder(dict)

    

