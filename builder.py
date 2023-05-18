#!/usr/bin/env python3


class HouseBuilder():
    def __init__(self):
        self.reset()

    def reset(self):
        self.features = set()
    def get_result(self):
        res = "\n  - ".join([f"House with features:"] + list(self.features))
        self.reset()
        return res

    def add_garage(self, n):
        self.features.add(f"garage for {n} cars")
    def add_pool(self):
        self.features.add(f"swimming pool")
    def add_statues(self, n):
        self.features.add(f"{n} fancy statues")
    def add_garden(self, n):
        self.features.add(f"garden with {n} trees")

class Director:
    def __init__(self, builder:HouseBuilder):
        self.builder = builder

    def make_flat(self):
        self.builder.add_statues(2)
        return self.builder.get_result()
    def make_villa(self):
        self.builder.add_garage(3)
        self.builder.add_pool()
        self.builder.add_garden(1)
        return self.builder.get_result()


if __name__ == "__main__":
    director = Director(HouseBuilder())
    print(director.make_flat())
    print(director.make_villa())
