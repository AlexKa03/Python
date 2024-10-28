import art

def highest_bid(bids):
    winner_bid = 0
    winner_name = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > winner_bid:
            winner_bid = bid_amount
            winner_name = bidder
    print("\n" * 20)
    print(art.logo)
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

auction_participants = {}
is_auction_continuing = True

while is_auction_continuing:
    print(art.logo)
    username = input("What is your name: ")
    bid = int(input("What is your bid: $"))

    auction_participants[username] = bid

    should_auction_continue = input("Are there any other bidders in this auction? Type YES or NO\n").lower()
    if should_auction_continue == "no":
        is_auction_continuing = False
        highest_bid(auction_participants)
    elif should_auction_continue == "yes":
        print("\n" * 20)