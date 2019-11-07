import unittest
import Calculator as calculator
class TestCalculator(unittest.TestCase):
    def test_int_add(self):
        self.assertEqual(calculator.add(9, 3), 12)

    def test_int2_add(self):
        self.assertEqual(calculator.add(9, 4), 13)

    def test_float_add(self):
        self.assertEqual(calculator.add(4.2, 3), 7.2)

    def test_int_minus(self):
        self.assertEqual(calculator.minus(9, 3), 6)

    def test_int2_minus(self):
        self.assertEqual(calculator.minus(9, 4), 5)

    def test_float_minus(self):
        self.assertEqual(calculator.minus(4.2, 3.2), 1.0)

    def test_int_times(self):
        self.assertEqual(calculator.times(9, 3), 27)

    def test_int2_times(self):
        self.assertEqual(calculator.times(9, 4), 36)

    def test_float_times(self):
        self.assertEqual(calculator.times(4.2, 3.3), 13.86)

    def test_int_divided(self):
        self.assertEqual(calculator.divided(9, 3), 3)

    def test_int2_divided(self):
        self.assertEqual(calculator.divided(9, 0), "無限")

    def test_float_divided(self):
        self.assertEqual(calculator.divided(5.4, 3), 1.8)

if __name__ == '__main__':
    unittest.main()