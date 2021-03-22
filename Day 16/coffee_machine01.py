
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
myMenu = Menu()
myMaker = CoffeeMaker()
moneyManager = MoneyMachine()
switchedOn = True
while switchedOn:
    print(f"What would you like? {myMenu.get_items()}:")
    choice = input("which one do you choose? ")
    if choice in myMenu.get_items().split("/"):
        myItem = myMenu.find_drink(choice)
        if myMaker.is_resource_sufficient(myItem):
            if moneyManager.make_payment(myItem.cost):
                myMaker.make_coffee(myItem)
    else:
        if choice == 'report':
            myMaker.report()
            moneyManager.report()
        elif choice == 'off':
            switchedOn = False
