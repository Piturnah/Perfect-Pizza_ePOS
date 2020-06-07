from enum import Enum, auto

class Pizza:
    def __init__(self, pizzaType, toppings, size, crust):
        #PizzaType, array, PizzaSize
        self.pizzaType = pizzaType
        self.toppings = toppings
        self.size = size
        self.crust = crust


    def price():
        #Do this later thanks future me
        return 0

    def describe(self):
        return self.size.value + "\" " + self.crust.value + " crust " + self.pizzaType.value + " with " + ", ".join(self.toppings)

class PizzaType(Enum):
    MEAT_FEAST = "meat feast"
    PEPPERONI = "pepperoni"
    HAWAIIAN = "hawaiian"
    VEGETARIAN = "vegetarian"
    THREE_CHEESE = "three cheese"

class PizzaSize(Enum):
    SMALL = "11.5"
    LARGE = "13.5"

class PizzaCrust(Enum):
    CLASSIC = "classic"
    STUFFED = "stuffed"

if __name__ == "__main__":
    #テスト
    print(Pizza(PizzaType.HAWAIIAN, [], PizzaSize.SMALL, PizzaCrust.STUFFED))
