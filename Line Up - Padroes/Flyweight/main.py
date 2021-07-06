from abc import ABC, abstractmethod


class Object(ABC):
    @abstractmethod
    def display(self):
        pass


class Tree(Object):
    def __init__(self, x_cord, y_cord, age):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.age = age

    def get_x_cord(self):
        return self.x_cord

    def get_y_cord(self):
        return self.y_cord

    def get_age(self):
        return self.age

    def display(self):
        print(f'displaying tree {self.age} at {self.x_cord}/{self.y_cord}')


class TreeManager:
    @property
    def tree_list(self) -> list[Tree]:
        return self._tree_list

    def __init__(self):
        self._tree_list = []

    def get_tree(self, x_cord, y_cord, age):
        for i in range(len(self.tree_list)):
            if self.tree_list[i].get_x_cord() == x_cord and \
               self.tree_list[i].get_y_cord() == y_cord and \
               self.tree_list[i].get_age() == age:
                tree = self.tree_list[i]
                print(f'Found tree {age} at {x_cord}/{y_cord}')
                return
        self.add_tree(x_cord, y_cord, age)

    def add_tree(self, x_cord, y_cord, age):
        tree = Tree(x_cord, y_cord, age)
        self.tree_list.append(tree)
        print(f'Adding tree {age} at {x_cord}/{y_cord}')

    def display_all_trees(self):
        for i in range(len(self.tree_list)):
            self.tree_list[i].display()


def main():
    tree_manager = TreeManager()
    tree_manager.add_tree(10,10, 10)
    tree_manager.add_tree(9, 9, 9)
    tree_manager.get_tree(10, 10, 10)
    tree_manager.display_all_trees()


if __name__ == "__main__":
    main()
