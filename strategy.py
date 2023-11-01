#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b): pass

class AdditionStrategy(Strategy):
    def execute(self, a, b): return a + b
class SutractionStrategy(Strategy):
    def execute(self, a, b): return a - b
class MultiplicationStrategy(Strategy):
    def execute(self, a, b): return a * b

class Context:
    def set_strategy(self, strategy):
        self.strategy = strategy
    def execute(self, a, b):
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    op = "+-*"[random.randint(0, 2)]

    strat = {
        "+": AdditionStrategy(),
        "-": SutractionStrategy(),
        "*": MultiplicationStrategy(),
    }[op]
    context = Context()
    context.set_strategy(strat)
    res = context.execute(a, b)

    print(f"{a} {op} {b} = {res}")
