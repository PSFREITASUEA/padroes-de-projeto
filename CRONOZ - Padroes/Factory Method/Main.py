from PizzaStore import *

def main():

    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza("cheese")
    print ("Ethan ordered a ", pizza.name)

    print("")

    pizza = chicagoStore.orderPizza("cheese")
    print("Joel ordered a ", pizza.name)

main()

    