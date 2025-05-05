print("Welcome to the Python Pizza order station:")
size= input("Please enter the pizza size(S,M,L):\n")
add_pepperoni=input("Do you want us to add the pepperoni?(Y or N)\n")
extra_cheese= input("DO you want us to add extra cheese?(Y or N)\n")

#Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

price=0
# print(type(price))
if size == "S":
    price=15
elif size == "M":
    price=20
else:
    price=25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3

if add_pepperoni == "Y":
    if size == "S":
        price+=2
    else:
        price+=3
# Add extra cheese for any size pizza (Y or N): +$1
if extra_cheese == "Y":
    price+=1


print(f"Your final price is {price}")
print("---------Thank you, Visit again!------------")





