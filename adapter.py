#!/usr/bin/env python3


from math import sqrt


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius

class SquarePeg:
    def __init__(self, width):
        self.width = width

class SquarePegAdapter(RoundPeg):
    def __init__(self, sq_peg:SquarePeg):
        self.peg = sq_peg
    def get_radius(self):
        return self.peg.width * sqrt(2) / 2

class RoundHole:
    def __init__(self, radius):
        self.radius = radius
    def fits(self, peg):
        print(f"trying to fit {peg.get_radius()} peg into {self.radius} hole")
        return peg.get_radius() <= self.radius


if __name__ == "__main__":
    r_hole = RoundHole(5)
    r_peg = RoundPeg(5)
    sq_peg = SquarePeg(6)

    assert r_hole.fits(r_peg)
    assert r_hole.fits(SquarePegAdapter(sq_peg))
