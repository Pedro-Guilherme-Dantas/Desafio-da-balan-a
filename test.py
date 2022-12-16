import unittest
from desafio import find_ball
class Test(unittest.TestCase):
    def test_find_ball(self):
        for i in range (9):
                aux = [10,10,10,10,10,10,10,10,10]
                aux[i] = 20
                self.assertEqual(find_ball(aux), 20)