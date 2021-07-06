from __future__ import annotations
from typing import List

from .menu_component import MenuComponent
from .menu_item import MenuItem
from .menu import Menu


class Menu(MenuComponent):
  """
  The Menu class represents the complex menucomponents that may have
  children. Usually, the Menu objects delegate the actual work to their
  children and then "sum-up" the result.
  """

  name: str
  description: str

  def __init__(self, name, description) -> None:
    self._children: List[MenuComponent] = []
    self.name = name
    self.description = description

  def get_name(self) -> str:
    return self.name

  def get_description(self) -> str:
    return self.description

  """
    A composite object can add or remove other menucomponents (both simple or
    complex) to or from its child list.
    """

  def add(self, menucomponent: MenuComponent) -> None:
    self._children.append(menucomponent)
    menucomponent.parent = self

  def remove(self, menucomponent: MenuComponent) -> None:
    self._children.remove(menucomponent)
    menucomponent.parent = None

  def is_composite(self) -> bool:
    return True

  def print(self) -> None:
    """
    The Menu executes its primary logic in a particular way. It
    traverses recursively through all its children, collecting and summing
    their results. Since the composite's children pass these calls to their
    children and so forth, the whole object full_menu is traversed as a result.
    """

    print('')
    print(f"{self.get_name()}, {self.get_description()}")
    print('-------------')
    for child in self._children:
      child.print()


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

  full_menu.add(menu_cafe)
  full_menu.add(menu_almoco)

  full_menu.print()

  print("\n\nADICIONANDO UM ITEM À HIERARQUIA")
  full_menu.add(simple)
  full_menu.print()
