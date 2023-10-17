#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def move(self, dx, dy): pass
    @abstractmethod
    def draw(self): pass

class CompoundGraphic(Graphic):
    def __init__(self):
        super().__init__()
        self.children = []
    def move(self, dx, dy):
        for ch in self.children:
            ch.move(dx, dy)
    def draw(self):
        for ch in self.children:
            ch.draw()
        #update boundaries
    def add(self, child:Graphic):
        self.children.append(child)
    def remove(self, child:Graphic):
        self.children.remove(child)

class Dot(Graphic):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def draw(self):
        print(f"drawing dot at {self.x}, {self.y}")

class Circle(Graphic):
    def __init__(self, x, y, r):
        super().__init__()
        self.center = Dot(x, y)
        self.radius = r
    def move(self, dx, dy):
        self.center.move(dx, dy)
    def draw(self):
        print(f"drawing circle at {self.center.x}, {self.center.y}")


if __name__ == "__main__":
    scene_graph = CompoundGraphic()
    scene_graph.add(Dot(5,6))
    scene_graph.add(Circle(1,2,1))
    footer = CompoundGraphic()
    footer.add(Dot(10,100))
    footer.add(Circle(60,100,20))
    scene_graph.add(footer)

    footer.move(-5,-10)
    scene_graph.draw()
