import unittest
from main import func
import math

class TestFunc(unittest.TestCase):

    def test_func(self):
        self.assertEqual(func(1,1,1),math.sin(1)**2/3)
        self.assertEqual(func(2,2,2),math.sin(8)**2/12)