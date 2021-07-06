
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class MenuComponent(ABC):
  """
  The base MenuComponent class declares common operations for both simple and
  complex objects of a composition.
  """

  @property
  def parent(self) -> MenuComponent:
    return self._parent

  @parent.setter
  def parent(self, parent: MenuComponent):
    """
    Optionally, the base MenuComponent can declare an interface for setting and
    accessing a parent of the menucomponent in a full_menu structure. It can also
    provide some default implementation for these methods.
    """

    self._parent = parent

  """
  In some cases, it would be beneficial to define the child-management
  operations right in the base MenuComponent class. This way, you won't need to
  expose any concrete menucomponent classes to the client code, even during the
  object full_menu assembly. The downside is that these methods will be empty for
  the leaf-level menucomponents.
  """

  def add(self, menucomponent: MenuComponent) -> None:
    pass

  def remove(self, menucomponent: MenuComponent) -> None:
    pass

  def is_composite(self) -> bool:
    """
    You can provide a method that lets the client code figure out whether a
    menucomponent can bear children.
    """

    return False

  def get_name(self) -> str:
    raise NotImplementedError("Unsupported Operation")

  def get_description(self) -> str:
    raise NotImplementedError("Unsupported Operation")

  def get_price(self) -> float:
    raise NotImplementedError("Unsupported Operation")

  def is_vegetarian(self) -> bool:
    raise NotImplementedError("Unsupported Operation")

  def print(self) -> None:
    raise NotImplementedError("Unsupported Operation")

  @abstractmethod
  def print(self) -> None:
    """
    The base MenuComponent may implement some default behavior or leave it to
    concrete classes (by declaring the method containing the behavior as
    "abstract").
    """

    pass
