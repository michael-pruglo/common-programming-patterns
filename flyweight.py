#!/usr/bin/env python3

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"drawing {self.__dict__} at ({x}; {y})")

class TreeFactory:
    tree_types = []

    def get_tree_type(name, color, texture):
        type = next(filter(lambda tt: tt.name==name and tt.color==color and tt.texture==texture,
            TreeFactory.tree_types), None)
        if type is None:
            type = TreeType(name, color, texture)
            TreeFactory.tree_types.append(type)
        return type

class Tree:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
    def draw(self):
        self.type.draw(self.x, self.y)

class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        type = TreeFactory.get_tree_type(name, color, texture)
        self.trees.append(Tree(x, y, type))

    def draw(self):
        for t in self.trees:
            t.draw()


if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(1, 2, "Birch", "white", "smooth")
    forest.plant_tree(5, 3, "Oak", "brown", "rusty")
    forest.plant_tree(9, 1, "Birch", "white", "smooth")
    forest.plant_tree(2, 9, "Birch", "white", "smooth")
    forest.plant_tree(3, 2, "Birch", "white", "smooth")
    forest.plant_tree(4, 6, "Birch", "white", "smooth")
    forest.plant_tree(4, 1, "Birch", "white", "smooth")
    forest.plant_tree(7, 7, "Apple", "green", "bold")
    forest.draw()
    print("flyweights:")
    for tt in TreeFactory.tree_types:
        print(f"  {tt.__dict__}")
