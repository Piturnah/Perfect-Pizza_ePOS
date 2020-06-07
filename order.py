"""order.py: coincidentally this is where the order class is"""

class Order:
    def __init__(self):
        self.pizzas = []


    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def removePizza(self, pizza):
        self.pizzas.remove(pizza)

    def priceDict(self):
        prices = {}
        for pizza in self.pizzas:
            prices[pizza] = pizza.price()
