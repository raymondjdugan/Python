from cgi import print_form
from recipe import MENU
from resources import machine_resources

def has_ingredients(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > machine_resources[ingredient]:
            print(f"​Sorry there is not enough {ingredient}.")
            return False
        return True

def format_money(money):
    return "{:0,.2f}".format(float(money))


def charge_user(cost):
    print(f"The cost for the drink is {format_money(int(cost))}")
    nickles = int(input(print("How many nickles do you put in?")))
    dimes = int(input(print("How many dimes do you put in?")))
    quarters = int(input(print("How many quarters do you put in?")))
    total_money = (nickles * .05) + (dimes * .10) + (quarters * .25)
    if total_money < int(cost):
        print("not enough money")
        return False
    else:
        print(f"Coffee Dispensing! Your change is ${total_money - int(cost)}")
        return True


def make_coffee(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        machine_resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

machine_on = True
machine_money = 0

while machine_on:
    answer = input(print("What would you like? (espresso/latte/cappuccino):")).lower()

    if answer == "off":
        machine_on = False
    elif answer == 'report':
        print(f"Water: {machine_resources['water']}ml")
        print(f"Milk: {machine_resources['milk']}ml")
        print(f"Coffee: {machine_resources['coffee']}ml")
        print(f"Money: ${format_money(machine_money)}")
    else:
        drink = MENU["answer"]
        if has_ingredients(drink["ingredients"]):
            if charge_user:
                make_coffee(answer, drink["ingredients"])