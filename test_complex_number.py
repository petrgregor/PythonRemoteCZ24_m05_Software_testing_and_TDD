import unittest
from complex_number import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def test_init(self):
        c = ComplexNumber(1, 2)
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imag, 2)

    def test_eq(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 2)
        self.assertEqual(c1, c2)

    def test_lt(self):
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(2, 2)
        self.assertTrue(c1 < c2)

    def test_gt(self):
        c1 = ComplexNumber(2, 2)
        c2 = ComplexNumber(1, 1)
        self.assertTrue(c1 > c2)

    def test_repr(self):
        c = ComplexNumber(1, 2)
        self.assertEqual(repr(c), 'ComplexNumber(1, 2)')

    def test_str(self):
        c = ComplexNumber(1, 2)
        self.assertEqual(str(c), '1 + 2i')
    def test_add(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        self.assertEqual(c1.add(c2), ComplexNumber(4, 6))

    def test_subtract(self):
        c1 = ComplexNumber(5, 7)
        c2 = ComplexNumber(3, 4)
        self.assertEqual(c1.subtract(c2), ComplexNumber(2, 3))

    def test_multiply(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        self.assertEqual(c1.multiply(c2), ComplexNumber(-5, 10))

    def test_divide(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        result = c1.divide(c2)
        expected = ComplexNumber(0.44, 0.08)
        self.assertAlmostEqual(result.real, expected.real, places=2)
        self.assertAlmostEqual(result.imag, expected.imag, places=2)

    def test_conjugate(self):
        c = ComplexNumber(1, 2)
        self.assertEqual(c.conjugate(), ComplexNumber(1, -2))

    def test_absolute_value(self):
        c = ComplexNumber(3, 4)
        self.assertEqual(c.absolute_value(), 5)

if __name__ == '__main__':
    unittest.main()
