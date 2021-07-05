from Ingredients import *

class PizzaIngredientFactory:

    @staticmethod
    def createDough(self):
        pass
    
    @staticmethod
    def createSauce(self):
        pass

    @staticmethod
    def createCheese(self):
        pass

    @staticmethod
    def createVeggies(self):
        pass

    @staticmethod
    def createPepperoni(self):
        pass

    @staticmethod
    def createClam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThinCrustDought()

    def createSauce(self):
        return MarinaraSouce()

    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        return "Veggies"

    def createPepperoni(self):
        return "Pepperoni"

    def createClam(self):
        return FreshClams()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThickCrustDought()

    def createSauce(self):
        return PlumTomatoSauce()

    def createCheese(self):
        return MozzarellaCheese()

    def createVeggies(self):
        return "Veggies"

    def createPepperoni(self):
        return "Pepperoni"

    def createClam(self):
        return FrozenClams()
