#!/usr/bin/env python3

from abc import ABC, abstractmethod


class GameAI(ABC):
    def __init__(self) -> None:
        self.money = 0
        self.built_structures = []
        self.units = 0

    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def collect_resources(self):
        for payout in self.built_structures:
            self.money += payout

    @abstractmethod
    def build_structures(self): pass
    @abstractmethod
    def build_units(self): pass

    def attack(self):
        print(f"attacking with ${self.money} structures {self.built_structures} units {self.units}")

class OrcsAI(GameAI):
    def build_structures(self):
        self.built_structures.append(11)
        if self.money > 10:
            self.built_structures.append(7)

    def build_units(self):
        if self.money > 60:
            self.units += 1

class MonstersAI(GameAI):
    def build_structures(self):
        pass  # monsters don't build
    def build_units(self):
        self.units += 3


if __name__ == "__main__":
    for ai in [OrcsAI(), MonstersAI()]:
        print(f"\n{ai}:")
        for t in range(5):
            ai.turn()
