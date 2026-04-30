import sys
import unittest

from src.calculation import add, sub, mul, div, ne


class TestCalculation(unittest.TestCase):
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15, res, msg='Addition Error')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5, res, msg='Subtraction Error')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50, res, msg='Multiplication Error')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2, res, msg='Division Error')

    @unittest.skipIf(sys.version_info >= (3, 14) ,reason='Not implemented yet')
    def test_ne(self):
        res = ne(10,10)
        self.assertTrue(res, msg='NE')

    def test_diverr(self):
        with self.assertRaises(ZeroDivisionError, msg='No Exception'):
            div(10, 0)


