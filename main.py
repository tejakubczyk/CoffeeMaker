from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

while machine_on:
    drinks = menu.get_items()
    choice = input(f"What would you like? {drinks}")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee is None:
            continue
        elif coffeemaker.is_resource_sufficient(coffee) == True and moneymachine.make_payment(coffee.cost) == True:
            coffeemaker.make_coffee(coffee)
