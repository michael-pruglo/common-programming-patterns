#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

class Chair(ABC): pass
class Table(ABC): pass
class Sofa(ABC): pass

class ModernChair(Chair): pass
class VictorianChair(Chair): pass
class ArtdecoChair(Chair): pass

class ModernTable(Table): pass
class VictorianTable(Table): pass
class ArtdecoTable(Table): pass

class ModernSofa(Sofa): pass
class VictorianSofa(Sofa): pass
class ArtdecoSofa(Sofa): pass


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self): pass
    @abstractmethod
    def create_table(self): pass
    @abstractmethod
    def create_sofa(self): pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self): return ModernChair()
    def create_table(self): return ModernTable()
    def create_sofa(self): return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self): return VictorianChair()
    def create_table(self): return VictorianTable()
    def create_sofa(self): return VictorianSofa()

class ArtdecoFurnitureFactory(FurnitureFactory):
    def create_chair(self): return ArtdecoChair()
    def create_table(self): return ArtdecoTable()
    def create_sofa(self): return ArtdecoSofa()


def client_code(furniture_factory:FurnitureFactory):
    room = [
        furniture_factory.create_chair(),
        furniture_factory.create_table(),
        furniture_factory.create_sofa(),
    ]
    print(room)


if __name__ == "__main__":
    client_code(ModernFurnitureFactory() if random.randint(0,1) else VictorianFurnitureFactory())
