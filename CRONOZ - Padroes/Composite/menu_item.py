from .menu_component import MenuComponent


class MenuItem(MenuComponent):
  """
  The MenuItem class represents the end objects of a composition. A leaf can't
  have any children.

  Usually, it's the MenuItem objects that do the actual work, whereas Menu
  objects only delegate to their sub-menucomponents.
  """

  name: str
  description: str
  vegetarian: bool
  price: float

  def __init__(self, name, description, vegetarian, price):
    self.name = name
    self.description = description
    self.vegetarian = vegetarian
    self.price = price

  def get_name(self) -> str:
    return self.name

  def get_description(self) -> str:
    return self.description

  def get_price(self) -> str:
    return self.price

  def is_vegetarian(self) -> bool:
    return self.vegetarian

  def print(self) -> None:
    print(f"  {self.name}", end=", ")
    if self.vegetarian:
      print("(v)", end=", ")
    print(f"R$ {self.price}")
    print(f'    -- {self.description}')
