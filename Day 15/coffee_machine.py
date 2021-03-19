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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(resources_required):
    k = ''
    not_available_list = []
    for item in resources_required:
        if resources[item] >= resources_required[item]:
            k = 'all avail'
        else:
            not_available_list.append(item)
 
    if len(not_available_list) == 0:
        return k
    else:
        return not_available_list
 
def process_coin():
    quarter = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickel = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return quarter + dimes + nickel + pennies
 
def check_transaction(choice, total):
    menu_cost = MENU[choice]['cost']
    if menu_cost <= total:
        change = total - menu_cost
        if change > 0:
            print(f"Here is your {round(change, 2)} change.")
            return 'success'
        elif change == 0:
            return 'success'
 
    elif menu_cost > total:
        return 'failed'
 
machine_state = 'on'
profit = 0
while machine_state != 'off':
 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        resources_required = MENU[choice]['ingredients']
        is_avail = check_resources(resources_required)
 
        if is_avail == 'all avail':
            print(f"Cost of {choice} is ${MENU[choice]['cost']}")
            print(f"Please insert coins: ")
            total = process_coin()
 
            if total > 0:
                transaction_state = check_transaction(choice, total)
                if transaction_state == 'success':
                    for item in resources_required:
                        resources[item] -= MENU[choice]['ingredients'][item]
                    profit += MENU[choice]['cost']
                    print(f"Here is your {choice}☕., Enjoy!")
 
                elif transaction_state == 'failed':
                    print(f"Sorry, that's not enough money. Money refunded")
 
            elif total == 0:
                print(f"Sorry! You didn't insert any coins")
 
        else:
            print(f"Sorry!, that is not enough {is_avail}.")
 
    elif choice == 'report':
        for key, value in resources.items():
            if key == 'coffee':
                print(f"{key} : {value}g")
            else:
                print(f"{key} : {value}ml")
 
        print(f"Profit: ${profit}")
 
    elif choice == 'off':
        print("Machine is shutting down")
        machine_state = 'off'
                  
