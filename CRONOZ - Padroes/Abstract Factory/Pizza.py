from PizzaIngredientFactory import *
from Ingredients import *

class Pizza:

    def __init__(self, name, veggies, cheese, pepperoni):
        self.name = name
        self.dough = Dough()
        self.sauce = Sauce()
        self.cheese = Cheese()
        self.clams = Clams()
        self.veggies = veggies
        self.pepperoni = pepperoni
    
    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")

class CheesePizza(Pizza):

    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing ", self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()

class ClamPizza(Pizza):

    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing ", self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()

class VeggiePizza(Pizza):

    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing ", self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.veggies = self.ingredientFactory.createVeggies()

class PepperoniPizza(Pizza):

    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing ", self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.pepperoni = self.ingredientFactory.createPepperoni()
        
        
        





