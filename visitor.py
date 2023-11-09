#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random


class Shape(ABC):
    def __init__(self):
        self.id = random.randint(0, 99999)
        self.x = random.randint(0, 1920)
        self.y = random.randint(0, 1080)
    @abstractmethod
    def draw(self): pass
    @abstractmethod
    def accept(self, visitor): pass

class Dot(Shape):
    def draw(self):
        print(f"drawing Dot #{self.id} at ({self.x}; {self.y})")
    def accept(self, visitor):
        return visitor.visit_dot(self)

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.r = random.randint(1, 1000)
    def draw(self):
        print(f"drawing Circle #{self.id} at ({self.x}; {self.y}), radius={self.r}")
    def accept(self, visitor):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.h = random.randint(1, 1000)
        self.w = random.randint(1, 1000)
    def draw(self):
        print(f"drawing Rectangle #{self.id} at ({self.x}; {self.y}) height={self.h} width={self.w}")
    def accept(self, visitor):
        return visitor.visit_rectangle(self)

class CompoundShape(Shape):
    def __init__(self, children):
        super().__init__()
        self.children = children
    def draw(self):
        print(f"drawing CompoundShape #{self.id} with children " + ', '.join(str(c.id) for c in self.children))
    def accept(self, visitor):
        return visitor.visit_compound_shape(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot): pass
    @abstractmethod
    def visit_circle(self, circle): pass
    @abstractmethod
    def visit_rectangle(self, rectangle): pass
    @abstractmethod
    def visit_compound_shape(self, compound_shape): pass

class XMLExportVisitor(Visitor):
    def visit_dot(self, dot):
        return f'<shape type="dot"><id>{dot.id}</id><x>{dot.x}</x><y>{dot.y}</y></shape>'
    def visit_circle(self, circle):
        return f'<shape type="circle"><id>{circle.id}</id><x>{circle.x}</x><y>{circle.y}</y><r>{circle.r}</r></shape>'
    def visit_rectangle(self, rectangle):
        return f'<shape type="rectangle"><id>{rectangle.id}</id><x>{rectangle.x}</x><y>{rectangle.y}</y><width>{rectangle.w}</width><height>{rectangle.h}</height></shape>'
    def visit_compound_shape(self, compound_shape):
        return f'<shape type="compound_shape"><id>{compound_shape.id}</id>' + ''.join(f'<child_id>{c.id}</child_id>' for c in compound_shape.children) + '</shape>'

def export_shapes_xml(shapes):
    export_visitor = XMLExportVisitor()
    xml = ""
    for sh in shapes:
        xml += sh.accept(export_visitor)
    return xml


if __name__ == "__main__":
    all_shapes = [
        Dot(), Circle(), Rectangle(),
        CompoundShape([Dot(), Circle(), Circle()]),
    ]

    for sh in all_shapes:
        sh.draw()
    print()

    print(export_shapes_xml(all_shapes))
