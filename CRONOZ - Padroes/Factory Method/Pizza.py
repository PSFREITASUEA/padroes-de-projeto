from abc import ABC

class Pizza(ABC):

    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
    
    def prepare(self):
        print("Preparing", self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print("  ", topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")


class NYStyleCheesePizza(Pizza):
    
    def __init__(self):
        super(NYStyleCheesePizza, self).__init__("NY Style Sauce and Cheese Pizza",
                                                 "Thin Crust Dough",
                                                 "Marinara Sauce",
                                                ["Grated Reggiano Cheese"])

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__("Chicago Style Deep Dish Cheese Pizza",
                                                      "Extra Thick Crust Dough",
                                                      "Plum Tomato Sauce",
                                                      ["Shredded Mozzarella Cheese"])
