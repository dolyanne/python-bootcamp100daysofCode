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
profit_gained = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit_gained}")


def check_resource(ingredients):
    """ Takes the users choice ingredient and compares to the available resources, return True if resources is enough
    to make coffee"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """ Takes the various coins entered and return the total"""
    print("Please insert coins")
    total = int(input("How many quarters?\n")) * 0.25
    total += int(input("How many dimes?\n")) * 0.10
    total += int(input("How many nickles?\n")) * 0.05
    total += int(input("How many pennies?\n")) * 0.01
    return total


def check_transaction_successful(money_received,drink_cost):
    """ Returns true if money received is greater or equal to the cost of coffee and
    false if money is insufficient to buy coffee"""
    if money_received >= drink_cost:
        change = money_received - drink["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")
        global profit_gained
        profit_gained += money_received
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_drink,ingredients):
    """ returns the final resource after deducting order ingredient from the available resources"""
    for item in ingredients:
        resources[item] -= ingredients [item]
    print(f"“Here is your {user_drink}. Enjoy! ☕️")


is_machine_on = True

# TODO 1 Prompt user to make an input

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    # TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        is_machine_on = False
    # TODO 3 Print report.
    elif user_choice == "report":
        report()
    else:
        drink = MENU[user_choice]
        # TODO 4 Check resources sufficient?
        if check_resource(drink["ingredients"]):
            # TODO  5 Process coins.
            payment = process_coins()
            # TODO  6. Check transaction successful?
            if check_transaction_successful(payment,drink["cost"]):
                # TODO  7. Make Coffee.
                make_coffee(user_choice,drink["ingredients"])














