# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
has_more_bidders = 'yes'
highest_bidder = ""
bidders = {}

while has_more_bidders != 'no':
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    if name in bidders:
        if bidders[name] < bid_amount:
            bidders[name] = bid_amount
    else:
        bidders[name] = bid_amount

    if bidders and highest_bidder:
        if bidders[name] > bidders[highest_bidder]:
            highest_bidder = name
    else:
        highest_bidder = name

    has_more_bidders = input("Are there any other bidders? (yes/no): ").lower()
    if has_more_bidders != 'no':
        print("\n" * 20)

print(f"\nThe winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")