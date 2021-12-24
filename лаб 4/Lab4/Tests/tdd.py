import unittest
from fabric import *

class MyTestCase(unittest.TestCase):
    car = None
    bike = None
    item1 = "Table"
    item2 = "Book"
    dist1 = 100
    dist2 = 77


    @classmethod
    def setUp(self):
        self.car = CarCreator().factory_method()
        self.car.take_item(self.item1)
        self.car.deliver(self.dist1)
        self.bike = BikeCreator().factory_method()
        self.bike.take_item(self.item2)
        self.bike.deliver(self.dist2)
#возвращается ли объект
    def test_not_none(self):
        self.assertIsNotNone(self.bike)
        self.assertIsNotNone(self.car)
#
    def test_item(self):
        self.assertEqual(self.car.item, self.item1)
        self.assertEqual(self.bike.item, self.item2)

#возвращает время доставки
    def test_upper(self):
        self.assertTrue(self.car.count_time() * self.car.speed
                        >= self.car.dist)
        self.assertTrue(self.bike.count_time() * self.bike.speed
                        >= self.bike.dist)
#проверка на наследство
    def test_instance(self):
        self.assertIsInstance(self.car, Transport)
        self.assertIsInstance(self.bike, Transport)


    @classmethod
    def tearDownClass(self):
        del self.bike
        del self.car
