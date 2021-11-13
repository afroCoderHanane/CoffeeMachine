from MENU import MENU
from RESSOURCES import resources


# TODO: functions

def report(x):
    for i in x:
        print(i, ": ", x[i])


def sufficient_resources(x):
    if x == "espresso":
        if (MENU[x]["ingredients"]["water"] <= resources["water"]) and (
                MENU[x]["ingredients"]["coffee"] <= resources["coffee"]):
            return True
    elif x == "latte" or x == "cappuccino":
        if (MENU[x]["ingredients"]["water"] <= resources["water"]) and (
                MENU[x]["ingredients"]["coffee"] <= resources["coffee"]) and (
                MENU[x]["ingredients"]["milk"] <= resources["milk"]):
            return True
    return False


def set_coins():
    quarter = int(input("How many quarter"))
    dime = int(input("How many dime"))
    nickel = int(input("How many nickel"))
    cent = int(input("How many cent"))
    return quarter, dime, nickel, cent


def update_resources(customer_input):
    if "money" not in resources:
        resources["money"] = 0
    resources["water"] -= MENU[customer_input]["ingredients"]["water"]
    resources["coffee"] -= MENU[customer_input]["ingredients"]["coffee"]
    if customer_input != "espresso":
        resources["milk"] -= MENU[customer_input]["ingredients"]["milk"]
    resources["money"] += MENU[customer_input]["cost"]


# print report
def coffee_machine():
    customer_input = input("What would you like?").lower()

    if customer_input == "report":
        report(resources)
    elif customer_input == "off":
        print("Bye Bye")
        exit()
    else:
        if sufficient_resources(customer_input):
            print("Insert Coins")
            coins_quarter, coins_dime, coins_nickel, coins_cent = set_coins()
            total_inserted = .25 * coins_quarter + .10 * coins_dime + .05 * coins_nickel + .01 * coins_cent
            if total_inserted < MENU[customer_input]["cost"]:
                print("Sorry Not Enough Money, Money Refunded")
            else:

                update_resources(customer_input)

                if total_inserted > MENU[customer_input]["cost"]:
                    print(f"Your change is {round(total_inserted - MENU[customer_input]['cost'], 2)} $")
                print(f" Here is your {customer_input} ☕. Enjoy!")

        else:
            if resources["water"] < MENU[customer_input]["ingredients"]["water"]:
                print(f"Sorry There is not enough water")
            elif resources["coffee"] < MENU[customer_input]["ingredients"]["coffee"]:
                print(f"Sorry There is not enough coffee")
            else:
                if customer_input != "espresso":
                    print(f"Sorry there is not enough milk")
    coffee_machine()


coffee_machine()
