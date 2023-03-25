#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self): print("Deliver by land in a box")
class Ship(Transport):
    def deliver(self): print("Deliver by sea in a container")


class Logistics(ABC):
    def plan_delivery(self):
        t = self.create_transport()
        t.deliver()

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

class RoadLogistics(Logistics):
    def create_transport(self): return Truck()
class SeaLogistics(Logistics):
    def create_transport(self): return Ship()


def client_code(logistics:Logistics):
    logistics.plan_delivery()


if __name__ == "__main__":
    client_code(RoadLogistics() if random.randint(0,1) else SeaLogistics())
