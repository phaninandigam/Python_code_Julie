menu={
    "espresso":{
        "ingredents":{
            "Water": 50,
            "Coffe": 18
        },
        "cost":1.5
    },

    "latte":{
        "ingredents":{
            "Water": 200,
            "Coffe": 24,
            "Milk": 150
        },
        "cost":2.5
    },

    "cappuccino":{
        "ingredents":{
            "Water": 250,
            "Coffe": 24,
            "Milk": 100
        },
        "cost": 3.0
    }
}

resource={
    "Coffe": 30,
    "Milk": 200,
    "Water": 300,
}

def process_coins(price,name):
    print("Please insert coins:")
    quarters=float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    provided_amount = ((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01))
    print(f"provided amount is {round(provided_amount,2)}$")

    if provided_amount<price:
        print(f"Sorry, that's not enough money. Money refunded {round(provided_amount,2)}$")
        print(f"The price of {name} is {price}$")
    elif provided_amount>price:
        print(f"Here is {provided_amount-price}$ in change")
        print(f"Here is your {name} ☕☕☕ Enjoy!")
    else:
        print(f"Here is your {name} ☕☕☕ Enjoy!")

def resource_availablity(user_input):
    process_coins(menu[user_input]['cost'], user_input)
    for item in menu[user_input]['ingredents']:
        name=item
        value= menu[user_input]['ingredents'][item]

        if value>resource[item]:
            print(f"Sorry, there is no enough {item}")
            return

        for item in resource:
            if name==item:
                resource[item]=(resource[item]-value)

    print("We have the resources")
    # process_coins(menu[user_input]['cost'],user_input)


def procced(user_input):
    for item in menu:
        if user_input == item:
            print(f"userinput in proceed funation {user_input}")
            resource_availablity(user_input)


def report():
    for item in resource:
        # print(item)
        print(f"{item}: {resource[item]} Ml")

continue_game = True
while continue_game:
    user_input=input("What would you like to have?(espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        print("The machine has been turned off")
        continue_game = False
    elif user_input == 'report':
        report()
    else:
        procced(user_input)




