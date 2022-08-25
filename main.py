from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

wallet = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}) ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        wallet.report()
        maker.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink) and wallet.make_payment(drink.cost):
            maker.make_coffee(drink)