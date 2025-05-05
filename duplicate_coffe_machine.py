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
    "Coffe": 50,
    "Milk": 200,
    "Water": 300,
}
money=0

def process_coins(price,name):
    global money
    print("Please insert coins:")
    quarters=float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    provided_amount = ((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01))
    print(f"\tThe provided amount is {round(provided_amount,2)}$")

    if provided_amount<price:
        print(f"\tSorry, that's not enough money. Money refunded {round(provided_amount,2)}$")
        print(f"\tThe price of {name} is {price}$")
    elif provided_amount>price:
        print(f"\tHere is {round((provided_amount-price),2)}$ in change")
        print(f"\tHere is your {name} ☕☕☕ Enjoy!")
        money=money+price
    else:
        print(f"\tHere is your {name} ☕☕☕ Enjoy!")
        money = money+price

def resource_availablity(user_input):
    for item in menu[user_input]['ingredents']:
        name=item
        value= menu[user_input]['ingredents'][item]

        if value>resource[item]:
            print(f"Sorry, there is no enough {item}")
            return

        for item in resource:
            if name==item:
                resource[item]=(resource[item]-value)

    process_coins(menu[user_input]['cost'],user_input)


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
        new_value=int(input(f"{item} :"))
        resource[item]= new_value
    print("The current resources are:")
    for item in resource:
        print(f"{item} : {resource[item]}")

continue_serve = True
while continue_serve:
    user_input=input("What would you like to have?(espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        print("The machine has been turned off")
        continue_serve = False
    elif user_input == 'report':
        report(money)
    elif user_input=='update':
        update_resource()
    else:
        resource_availablity(user_input)
 
