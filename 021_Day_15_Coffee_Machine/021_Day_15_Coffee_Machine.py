from menu_resources import MENU, resources
from art import LOGO


def give_report() -> None:
    '''Prints resouces and money till now'''
    total_water = resources['water']
    total_milk  = resources['milk']
    total_coffee = resources['coffee']
    total_money = resources['money']
    print(f"\tWater: {total_water}ml\n\tMilk: {total_milk}ml\n\tCoffee: {total_coffee}g\n\tMoney: ${total_money}")


def coffee_kitchen(order : str)-> None:
    '''Checks for resources, Checks for money.
    Order coffee ->  deduce resouces, add money, return back the change money if any'''


    def check_resources(coffee_ingrades : dict)-> bool:
        '''Takes Coffee Ingradients, Checks if the ingrads are sufficient to make that order.'''

        for k, v in coffee_ingrades.items():
            if resources[k] < v:
                print(f"Sorry! there is not enough {k}.")
                return False
        return True


    def check_money(quarter:int, dimes:int, nickel:int, pennies:int, coffee_cost:float)-> bool:
        '''Takes quantity of each denomination, checks for sufficient money to bey the order. Returns Bool with change money if any.'''
        
        total_sum = 0.25 * quarter + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
        if total_sum >= coffee_cost:
            resources["money"] += coffee_cost
            change_money = total_sum - coffee_cost
        else:
            print("insufficient money to buy!")
            return False, None
        return True, "{:0.2f}".format(change_money)


    def reduce_resource(ingrades : dict)-> None:
        '''Takes ingrades, Reduces the raw materials from machine that is used by previous order'''
        for k, v in ingrades.items():
            resources[k] -= v
    

    def complete_the_order(order : str) -> None:
        '''Takes order, completes the order if sufficient resources and money. Returns None'''
        coffee_type = MENU[order]
        coffee_ingrades = coffee_type["ingredients"]
        coffee_cost =coffee_type["cost"]

        is_resources = check_resources(coffee_ingrades)
        if is_resources:
            print("Please insert some Coins: ")
            quarter_coins = int(input("Quarter: "))
            dimes_coins = int(input("Dimes: "))
            nickel_coins = int(input("Nickel: "))
            pennies_coins = int(input("Pennies: "))

            is_money, change_money = check_money(quarter_coins, dimes_coins, nickel_coins, pennies_coins, coffee_cost)
            if is_money:
                reduce_resource(coffee_ingrades)
                if change_money is not None:
                    print(f"Here is ${change_money} in change!") 
                print(f"Enjoy! Here is your {order} --> `(_)D ")

    complete_the_order(order)


def place_order() -> None:
    is_coffee_machine_on = True
    while is_coffee_machine_on:
        user_choice = input("\nWhat would you like? (espresso/latte/cappuccino) or (report/off): ")
        if user_choice == "report":
            give_report()
        elif user_choice == "off":
            print("Thanks for using Coffee Machine !")
            is_coffee_machine_on = False
        else:
            coffee_kitchen(user_choice)


print(LOGO)
place_order()


"""
Coffee Machine Program Requirements
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    a. Check the user's input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer.

2. Turn off the Coffee Machine by entering “off” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    the machine. Your code should end execution when this happens.

3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values. e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5

4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough
    resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    not continue to make the drink but print: “Sorry there is not enough water.”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    program should say “Sorry that's not enough money. Money refunded.”.

    b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5

    c. If the user has inserted too much money, the machine should offer change.
    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    places.


7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
        E.g. report before purchasing latte:
            Water: 300ml
            Milk: 200ml
            Coffee: 100g
            Money: $0
        Report after purchasing latte:
            Water: 100ml
            Milk: 50ml
            Coffee: 76g
            Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink.
"""
