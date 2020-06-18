import unittest
from add import add_two_numbers


class Testing(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_two_numbers(1, 3), 4)


if __name__ == '__main__':
    unittest.main()
