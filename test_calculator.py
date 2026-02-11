import unittest
from calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = ScientificCalculator()

    # -------- UNIT TESTS -------- #

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_sqrt(self):
        self.assertEqual(self.calc.square_root(16), 4)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)

    # -------- INTEGRATION TEST -------- #

    def test_combined_expression(self):
        result = self.calc.add(self.calc.sin(30), 5)
        self.assertAlmostEqual(result, 5.5, places=1)

if __name__ == "__main__":
    unittest.main()
