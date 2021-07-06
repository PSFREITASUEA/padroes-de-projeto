from modules.beverages import Decaf, Espresso, DarkRoast, HouseBlend
from modules.condiments import Mocha, Soy, SteamedMilk, Whip

if __name__ == "__main__":
    
    # espresso simples (sem decorators)
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.get_cost()))
    
    # duplo mocha dark roast com whip
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.get_cost()))
    
    # soy mocha house blend com whip
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.get_cost()))

    beverage4 = Decaf()
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    beverage4 = SteamedMilk(beverage4)
    print(beverage4.get_description() + " $" + str(beverage4.get_cost()))
