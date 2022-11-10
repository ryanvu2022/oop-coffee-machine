from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_machine_off = False

while not is_machine_off:
    print(logo)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_machine_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
