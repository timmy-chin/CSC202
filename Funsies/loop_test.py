import math
import unittest

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac


class Test(unittest.TestCase):
    for i in range(5000):
        exec(f'def test{i}(self):\n     self.assertEqual(math.factorial({i}), factorial({i}))')


if __name__ == '__main__':
    unittest.main()