import unittest
import РК2
class test(unittest.TestCase):
    def test_tasks(self):
        self.assertEqual(РК2.test1(),'Labs: Lab1 Lab2 Lab3 \nBookForLabs: Math Python_Book It \n')
        self.assertEqual(РК2.test2(), [['Film', 0], ['Labs', 116.33], ['Pycharm_programmers', 160.0], ['BookForLabs', 1016.67]])
        self.assertEqual(РК2.test3(),'Lab1\tLabs\nLab2\tLabs\nLab3\tLabs\n')
if __name__ == "__main__":
    unittest.main()