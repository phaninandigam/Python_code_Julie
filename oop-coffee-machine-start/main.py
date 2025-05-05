from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
# menu_items=MenuItem()
money_machine=MoneyMachine()
coffee_maker= CoffeeMaker()

continue_serve = True
while continue_serve:
    user_input=input(f"What would you like to have? ({menu.get_items()})").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == 'off':
        print("The machine has been turned off")
        continue_serve = False
    else:
        drink= menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            print("can make")
            print(drink.cost)
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





