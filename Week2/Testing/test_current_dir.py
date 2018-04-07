import unittest
from simplify_fraction import simplify_fraction


class TestCurrentTasks(unittest.TestCase):
    def test_simplify_fraction(self):
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))

    def test_simplify_fraction_2(self):
        self.assertEqual(simplify_fraction((11, 44)), (1, 4))




if __name__ == '__main__':
    unittest.main()