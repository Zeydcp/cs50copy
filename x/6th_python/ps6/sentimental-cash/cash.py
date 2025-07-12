# TODO
from cs50 import get_float
import math


def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents = round(cents - quarters * 0.25, 2)

    dimes = calculate_dimes(cents)
    cents = round(cents - dimes * 0.1, 2)

    nickels = calculate_nickels(cents)
    cents = round(cents - nickels * 0.05, 2)

    pennies = calculate_pennies(cents)
    cents = round(cents - pennies * 0.01, 2)

    coins = quarters + dimes + nickels + pennies

    print(coins)


def get_cents():
    while True:
        cents = get_float("Change owed: ")
        if cents >= 0:
            break

    return cents


def calculate_quarters(cents):
    quarters = math.floor(cents / 0.25)
    return quarters


def calculate_dimes(cents):
    dimes = math.floor(cents / 0.1)
    return dimes


def calculate_nickels(cents):
    nickels = math.floor(cents / 0.05)
    return nickels


def calculate_pennies(cents):
    pennies = math.floor(cents / 0.01)
    return pennies


main()
