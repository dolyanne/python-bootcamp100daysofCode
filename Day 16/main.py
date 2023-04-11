from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# access report method from each class

menu = Menu()
is_on = True


# check if resources are sufficient
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option}\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        if is_resource_sufficient:
            # process payment
            make_payment = money_machine.make_payment(drink.cost)
            if make_payment:
                # make coffee
                coffee_maker.make_coffee(drink)










