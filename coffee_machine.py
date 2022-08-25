MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(drink_name, ingredients):
    """Deduction of ingredients from  resources store"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"here is your {drink_name} ,Enjoy!")


def is_transaction_successful(money_received, drink_cost):
    """returns true if payment is accepted or false is money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your change amount: ${change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money Refunded! Insufficient amount")
        return False


def coins():
    """Returns total amount enetered by user"""
    print("please insert coin!")
    total = int(input("how many quarters : ")) * 0.25
    total += int(input("how many dimes : ")) * 0.1
    total += int(input("how many nickels : ")) * 0.05
    total += int(input("how many pennies : ")) * 0.01
    return total


def is_sufficient(ingredients):
    """returns true if drink can be made and false if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


profit = 0.0
is_on = True

while is_on:
    choice = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment = coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
