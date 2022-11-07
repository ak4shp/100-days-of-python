from menu_resources import MENU, resources

# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#     a. Check the user's input to decide what to do next.
#     b. The prompt should show every time action has completed, e.g. once the drink is
#     dispensed. The prompt should show again to serve the next customer.
def give_report():
    '''Prints resouces and money till now'''
    total_water = resources['water']
    total_milk  = resources['milk']
    total_coffee = resources['coffee']
    total_money = resources['money']
    print(f"\twater: {total_water}\n\tmilk: {total_milk}\n\tcoffee: {total_coffee}\n\tmoney: {total_money}")


def coffee_kitchen(order):
    '''Checks for resources, Checks for money
    Order coffee ->  deduce resouces, add money, give changes if any'''
    coffee_type = MENU[order]
    coffee_ingrades = coffee_type["ingredients"]
    coffee_cost =coffee_type["cost"]


    def check_resources()-> bool:
        print(coffee_ingrades)
        for k, v in coffee_ingrades.items():
            # print(11)
            if resources[k] >= v:
                resources[k] -= v
            else:
                print(f"Sorry there is not enough {k}.")
                return False
        return True

    print("resources: ", check_resources())


    def check_money(quarter, dimes, nickel, pennies)-> bool:
        total_sum = 0.25 * quarter + 0.1 * dimes + 0.05 * nickel + 0.01 * pennies
        if total_sum >= coffee_cost:
            resources["money"] += coffee_cost
            change_money = total_sum - coffee_cost
        else:
            print("insufficient money to buy!")
            return False, None
        return True, float("{:0.2f}".format(change_money))
    
    print("money: ",check_money(10, 2, 10, 2))


    def process_order():
        pass
        # resources deduction -> done in check_resource()
        # add money to machine's account -> done in check_money()
        # rerurn changes(change money) if any -> done in check_money()
    pass


user_choice = input("What would you like? (espresso/latte/cappuccino): ")

if user_choice == "report":
    give_report()
elif user_choice == "off":
    # break
    pass
else:
    coffee_kitchen(user_choice)


"""
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
