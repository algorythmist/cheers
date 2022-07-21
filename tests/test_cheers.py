import unittest

from cheers import *


class CheersTestCase(unittest.TestCase):

    def test_recursive1(self):
        solutions = list_solutions_recursive1(15)
        self.assertEqual([0, 0, 1, 1, 3, 5, 8, 11, 15, 19, 24, 29, 35, 41, 48, 55], solutions)

    def test_recursive2(self):
        solutions = list_solutions_recursive2(15)
        self.assertEqual([0, 0, 1, 1, 3, 5, 8, 11, 15, 19, 24, 29, 35, 41, 48, 55], solutions)

    def test_closed_form(self):
        self.assertEqual([0, 0, 1, 1, 3, 5, 8, 11, 15, 19, 24, 29, 35, 41, 48, 55],
                         list_solutions_closed_form(15))

    def test_number_of_clinks(self):
        self.assertEqual(24, number_of_clinks(10))
        self.assertEqual(2499, number_of_clinks(100))
        self.assertEqual(249999, number_of_clinks(1000))
        self.assertEqual(24999999, number_of_clinks(10000))
        self.assertEqual(2499999999, number_of_clinks(100000))
        self.assertEqual(249999999999, number_of_clinks(1000000))

    def test_generate_first_few(self):
        table = solutions_in_table(range(3, 13))
        print(table)

    def test_generate_powers_of_10(self):
        table = solutions_in_table([10 ** i for i in range(1, 10)])
        print(table)
