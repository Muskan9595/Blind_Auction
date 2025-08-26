logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def find_highest_bidder(bidding_dictionary):
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if highest_bid < bid_amount:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    print("||___________Congratulations___________||")

bids={}
more_bids=True
while more_bids:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue=="no":
        more_bids=False
        find_highest_bidder(bids)
    elif should_continue=='yes':
        print("\n" * 20)