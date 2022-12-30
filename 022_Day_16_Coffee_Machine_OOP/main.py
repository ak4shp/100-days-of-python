from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import LOGO


order = CoffeeMaker()
money = MoneyMachine()
print(LOGO)
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/) or (off/report): ")
    if choice == "report":
        order.report()
        money.report()

    elif choice == "off":
        is_on = False

    else:
        drink = Menu()
        drink_name = drink.find_drink(choice)

        if drink_name and order.is_resource_sufficient(drink_name):
            drink_cost = drink_name.cost
            if money.make_payment(drink_cost):
                order.make_coffee(drink_name)


"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)

"""

