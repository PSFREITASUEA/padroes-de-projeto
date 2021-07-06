from menu_component import MenuComponent
from typing import List


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
