import unittest
from main import f
import math

class TestFunc(unittest.TestCase):

    def test_func(self):
        self.assertEqual(f(1,1,1),math.sin(1)**2/3)
        self.assertEqual(f(2,2,2),math.sin(8)**2/12)
