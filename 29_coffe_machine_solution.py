menu = {
    "espresso": {
        "ingredents": {
            "Water": 50,
            "Coffe": 18
        },
        "cost": 1.5
    },

    "latte": {
        "ingredents": {
            "Water": 200,
            "Coffe": 24,
            "Milk": 150
        },
        "cost": 2.5
    },

    "cappuccino": {
        "ingredents": {
            "Water": 250,
            "Coffe": 24,
            "Milk": 100
        },
        "cost": 3.0
    }
}

resource = {
    "Coffe": 50,
    "Milk": 200,
    "Water": 300,
}
money = 0


def process_coins(price, name):
    print("Please insert coins:")
    total = float(input("How many quarters? ")) *0.25
    total+= float(input("How many dimes? ")) *0.10
    total+= float(input("How many nickles? ")) *0.05
    total+= float(input("How many pennies? ")) *0.01

    print(f"\tThe provided amount is {round(total, 2)}$")
    return total

def is_trnsaction_scusssfull(amount_recieved, price_of_item,name):
    global money
    if amount_recieved < price_of_item:
        print(f"\tSorry, that's not enough money. Money refunded {round(amount_recieved, 2)}$")
        print(f"\tThe price of {name} is {price_of_item}$")
        return False
    elif amount_recieved > price_of_item:
        print(f"\tHere is {round((amount_recieved - price_of_item), 2)}$ in change")
        print(f"\tHere is your {name} ☕☕☕ Enjoy!")
        money = money + price_of_item
        return True
    else:
        print(f"\tHere is your {name} ☕☕☕ Enjoy!")
        money = money + price_of_item
        return True


def resource_availablity(user_input):
    for item in menu[user_input]['ingredents']:
        name = item
        value = menu[user_input]['ingredents'][item]

        if value > resource[item]:
            print(f"Sorry, there is no enough {item}")
            return False

    return True




def report(money):
    for item in resource:
        # print(item)
        print(f"{item}: {resource[item]} Ml")
    print(f"Money: {money} $")


def update_resource():
    print("The current resources are:")
    for item in resource:
        print(f"{item} : {resource[item]}")
    print("Please enter the new values")
    for item in resource:
        new_value = int(input(f"{item} :"))
        resource[item] = new_value
    print("The current resources are:")
    for item in resource:
        print(f"{item} : {resource[item]}")

def make_coffe(drink_name,ingerdants):
    for item in ingerdants:
        resource[item]-=ingerdants[item]


continue_serve = True
while continue_serve:
    user_input = input("What would you like to have?(espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        print("The machine has been turned off")
        continue_serve = False
    elif user_input == 'report':
        report(money)
    elif user_input == 'update':
        update_resource()
    else:
        if resource_availablity(user_input):
            amount_recieved=process_coins(menu[user_input]['cost'], user_input)
            if is_trnsaction_scusssfull(amount_recieved,menu[user_input]['cost'],user_input):
                make_coffe(user_input,menu[user_input]['ingredents'])

