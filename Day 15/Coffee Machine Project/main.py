# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
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
    "money": 0
}


def create_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def complete_transaction(cost):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if paid >= cost:
        resources["money"] = resources["money"] + cost
        change = round(paid - cost)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_is_resources_are_enough(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False


def make_coffee(user_input, ingredients):
    for ingredient in ingredients:
        resources[ingredient] = resources[ingredient] - ingredients[ingredient]
    print(f"Here is your {user_input} ☕️. Enjoy!")


def order_coffee(user_input):
    coffee_details = MENU[user_input]
    if check_is_resources_are_enough(coffee_details["ingredients"]) is not False:
        transaction_status = complete_transaction(coffee_details["cost"])
        if transaction_status is True:
            make_coffee(user_input, coffee_details["ingredients"])


while 1 == 1:
    userInput = str(input("What would you like? (espresso/latte/cappuccino): "))
    if userInput == "report":
        create_report()
    else:
        order_coffee(userInput)
