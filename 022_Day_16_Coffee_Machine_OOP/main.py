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


