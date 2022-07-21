import unittest

from cheers import *


class CheersTestCase(unittest.TestCase):

    def test_recursive1(self):
        solutions = recursive1(15)
        print(solutions)

    def test_recursive2(self):
        solutions = recursive2(15)
        print(solutions)

    def test_explicit(self):
        print(explicit(15))

