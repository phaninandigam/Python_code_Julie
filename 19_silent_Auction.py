from replit import clear

# HINT: You can call clear() to clear the output in the console.

# creating an empty dictionary
bid = {}
proceed = True
while proceed:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bid[name] = bid_amount
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bid == "yes":
        clear()
    else:
        proceed = False

# print(bid)
# finding the highest bidder
list = []
for amount in bid:
    list.append(bid[amount])
    # print(list)

list.sort()
for amount in bid:
    if bid[amount] == list[-1]:
        winner_name = amount

print(f"The winner is {winner_name}  with a bid amount of {list[-1]}")

