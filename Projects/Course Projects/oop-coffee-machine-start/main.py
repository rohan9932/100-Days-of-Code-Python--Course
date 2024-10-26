from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def coffee_machine():
    while True:
        instruction = input("Kindly give an instruction: ")
        if instruction == "off":
            return
        elif instruction == "report":
            coffee_maker.report()
            money_machine.report()
        elif instruction == "order":
            order = input(f"What would you like? {menu.get_items()}: ").lower()
            drink = menu.find_drink(order) #finds the ordered drink
            drink_cost = drink.cost
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink_cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid input!!")


coffee_machine()