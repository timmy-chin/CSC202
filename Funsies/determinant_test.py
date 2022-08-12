import unittest
from Determinant import *


class Determinant_Test(unittest.TestCase):
    def test01_determinant(self):
        msg = 'Testing 10 by 10'

        self.assertEqual(det(matrix), -1204877246212860710, msg)

if __name__ == '__main__':
    unittest.main()
