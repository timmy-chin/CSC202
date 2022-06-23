import unittest
import Basic_Data_Structures as ds


class Test(unittest.TestCase):
    def test03(self):
        self.assertTrue(ds.palindrome('radar'))

    def test04(self):
        self.assertFalse(ds.palindrome('Heck'))

    def test05(self):
        self.assertEqual(ds.potato_game(['Adam', 'Celine', 'Timmy'], 2), 'Celine')


if __name__ == '__main__':
    unittest.main()