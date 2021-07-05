from abc import ABC, abstractmethod
from Pizza import *


class PizzaStore(ABC):

    def orderPizza(self, type):

        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
                
        return pizza
    @abstractmethod
    def createPizza(self, type):
        pass

class NYPizzaStore(PizzaStore):

    def createPizza(self, item):
        if item == "cheese": 
            return NYStyleCheesePizza()
        else:
            return None

class ChicagoPizzaStore(PizzaStore):

    def createPizza(self, item):
        if item == "cheese": 
            return ChicagoStyleCheesePizza()
        else:
            return None



