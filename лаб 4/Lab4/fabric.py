import math
from abc import ABC, abstractmethod
import unittest


from Tests.tdd import *

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

class CarCreator(Creator):
    def factory_method(self):
        return Car()

class BikeCreator(Creator):
    def factory_method(self):
        return Bike()

class Transport(ABC):
    @abstractmethod
    def deliver(self, *args):
        pass

    @abstractmethod
    def take_item(self, *args):
        pass

    @abstractmethod
    def count_time(self):
        pass

class Car(Transport): # Грузовик
    speed = 10 # скорость
    dist = None # расстояние
    item = None # Товар

    def deliver(self, dist):
        self.dist = dist

    def take_item(self, item):
        self.item = item

    def count_time(self):
        return math.ceil(self.dist / self.speed) # округление в большую сторону

class Bike(Transport): # Корабль
    speed = 5 # скорость
    dist = None # расстояние
    item = None # Товар

    def deliver(self, dist):
        self.dist = dist

    def take_item(self, item):
        self.item = item

    def count_time(self):
        return math.ceil(self.dist / self.speed) # округление в большую сторону

if __name__ == '__main__':
    unittest.main()

