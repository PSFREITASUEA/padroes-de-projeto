from __future__ import annotations
from typing import List

from menu_component import MenuComponent
from menu_item import MenuItem
from menu import Menu

if __name__ == "__main__":
  # This way the client code can support the simple leaf menucomponents...
  simple = MenuItem(name='Coca cola', description='refrigerante',
                    vegetarian=False, price=5.0)
  print("SIMPLES ITEM")
  simple.print()

  # ...as well as the complex composites.
  full_menu = Menu('Cardapio', 'Cardapio completo')

  menu_cafe = Menu(name="Café da manhã", description="Menu do café da manhã")
  menu_cafe.add(MenuItem(name='cafe', description='cafe simples',
                vegetarian=False, price=1.0))
  menu_cafe.add(MenuItem(name='leite', description='apenas leite',
                vegetarian=False, price=1.0))

  menu_almoco = Menu(name="Almoço", description="Menu do almoço")
  menu_almoco.add(MenuItem(name='Carne de sol', description='Uma deliciosa carne de sol',
                           vegetarian=False, price=100.0))

  submenu_sobremesa = Menu(name="Sobremesa", description="Menu de sobremesas")
  submenu_sobremesa.add(MenuItem(name='Pudim', description='Um delicioso pudim',
                                 vegetarian=False, price=100.0))

  full_menu.add(menu_cafe)
  full_menu.add(menu_almoco)

  full_menu.print()

  print("\n\nADICIONANDO UM ITEM À HIERARQUIA")

  menu_almoco.add(submenu_sobremesa)
  full_menu.print()
