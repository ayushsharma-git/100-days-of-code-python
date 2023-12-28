from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


while 1 == 1:
    userInput = str(input(f"What would you like? ({menu.get_items()}): "))
    if userInput == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(userInput)
        if menu_item is not None:
            if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)




