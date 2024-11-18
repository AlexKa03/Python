from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def machine():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    is_working = True

    while is_working:
        user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_selection == "off":
            is_working = False
            return
        elif user_selection == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_selection)
            if coffee_maker.is_resource_sufficient(drink):
                drink_cost = menu.find_drink(user_selection).cost
                if money_machine.make_payment(drink_cost):
                    coffee_maker.make_coffee(drink)

machine()