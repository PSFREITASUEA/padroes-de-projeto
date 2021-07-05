from Pizza import *

class PizzaStore:

    def orderPizza(self, type):

        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
                
        return pizza

    @staticmethod
    def createPizza(self, type):
        pass

class NYPizzaStore(PizzaStore):

    def createPizza(self, item):

        ingredientFactory = NYPizzaIngredientFactory()

        if item == "cheese": 
            pizza = CheesePizza(ingredientFactory)
            pizza.name = "New York Style Cheese Pizza"
            return pizza

        elif item == "veggie": 
            pizza = VeggiePizza(ingredientFactory)
            pizza.name = "New York Style Veggie Pizza"
            return pizza
        
        elif item == "clam":
            pizza = ClamPizza(ingredientFactory)
            pizza.name = "New York Style Clam Pizza"
            return pizza

        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredientFactory)
            pizza.name = "New York Style Pepperoni Pizza"
            return pizza

        else:
            return None

class ChicagoPizzaStore(PizzaStore):

    def createPizza(self, item):

        ingredientFactory = ChicagoPizzaIngredientFactory()

        if item == "cheese": 
            pizza = CheesePizza(ingredientFactory)
            pizza.name = "Chicago Style Cheese Pizza"
            return pizza

        elif item == "veggie": 
            pizza = VeggiePizza(ingredientFactory)
            pizza.name = "Chicago Style Veggie Pizza"
            return pizza

        
        elif item == "clam":
            pizza = ClamPizza(ingredientFactory)
            pizza.name = "Chicago Style Clam Pizza"
            return pizza
        
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredientFactory)
            pizza.name = "Chicago Style Pepperoni Pizza"
            return pizza

        else:
            return None



