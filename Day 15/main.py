from recipe import MENU
from resources import machine_resources


def format_money(money):
    return "{:0,.2f}".format(float(money))


def charge_user(cost):
    print(f"The cost for the drink is {format_money(cost)}")
    nickles = int(input(print("How many nickles do you put in?")))
    dimes = int(input(print("How many dimes do you put in?")))
    quarters = int(input(print("How many quarters do you put in?")))
    total_money = (nickles * .05) + (dimes * .10) + (quarters * .25)
    if total_money < int(cost):
        print("not enough money")
        return
    else:



def make_coffee(coffee):
    for ingredient, value in coffee["ingredients"].items():
        if machine_resources[ingredient] < value:
            print("Not Enough")
            return
    charge_user(coffee["cost"])


def coffee_machine():
    machine_on = True
    machine_money = 0

    while machine_on:
        answer = input(print("What would you like? (espresso/latte/cappuccino):")).lower()

        if answer == "off":
            machine_on = False
        elif answer == 'report':
            print(f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\nCoffee: {machine_resources['coffee']}ml\nMoney: ${format_money(machine_money)}")
        elif answer == "espresso":
            make_coffee(MENU[answer])



coffee_machine()

# TODO: Turn off the Coffee Machine by entering “off” to the prompt

# # TODO: Print report
