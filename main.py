#!/usr/bin/env python

"""main.py: yes"""

__author__ = "I don't want to take credit for this"

from pizza import *
from order import *

import time
import csv


def takeOrder():
    currentOrder = Order()

    while input("Add another pizza (y/n)") == "y":
        
        pizzaType = makeChoice({
            "1" : PizzaType.MEAT_FEAST,
            "2" : PizzaType.PEPPERONI,
            "3" : PizzaType.HAWAIIAN,
            "4" : PizzaType.VEGETARIAN,
            "5" : PizzaType.THREE_CHEESE
            },
              "\nTYPE:\n\n1. MEAT FEAST\n2. PEPPERONI\n3. HAWAIIAN\n4. VEGETARIAN\n5. THREE CHEESE\n\n> ")

        toppings = addToppings()

        pizzaSize = makeChoice({
            "1" : PizzaSize.SMALL,
            "2" : PizzaSize.LARGE
            },
              "\nSIZE:\n\n1. 11.5\"\n2. 13.5\"\n\n> ")

        pizzaCrust = makeChoice({
            "1" : PizzaCrust.CLASSIC,
            "2" : PizzaCrust.STUFFED
            },
              "\nCRUST:\n\n1. CLASSIC\n2. STUFFED\n\n> ")

        currentOrder.addPizza(Pizza(pizzaType, toppings, pizzaSize, pizzaCrust))

    print("\nHere is the current order:")
    for index, pizza in enumerate(currentOrder.pizzas):
        print(str(index) + ". " + pizza.describe())


def makeChoice(dictionary, displayText):
    try:
        return dictionary[input(displayText)]
    except:
        print("\nNOT A VALID CHOICE, TRY AGAIN")
        time.sleep(1)
        return makeChoice(dictionary, displayText)

def addToppings():
    toppingsDict = {}
    with open("pricesheet.csv", mode = "r") as infile:
        reader = csv.reader(infile)
        toppingsDict = {rows[0] : rows[1] for rows in reader}

    toppings = list(toppingsDict.keys())
    selectedToppings = []
    while input("Add a topping (y/n)") == "y":

        print()
        for index, topping in enumerate(toppings):
            print(str(index + 1) + ". " + topping)

        selectedToppings.append(toppings[int(input("\nIndex of topping to add > ")) - 1])

    return selectedToppings


def main():
    selectionDict = {
        "1" : takeOrder,
        "2" : lambda : print("Eventually this feature will be added"),
        "3" : quit
        }

    try:
        selectionDict[input("\n1. Take order\n2. Daily sales report\n3. Quit\n\n> ")]()
    except KeyError:
        print("That ain't an option chief")
        main()

if __name__ == "__main__":
    main()
