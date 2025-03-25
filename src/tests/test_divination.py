import unittest
from meihua.divination import Divination

class TestDivination(unittest.TestCase):

    def setUp(self):
        self.divination = Divination()

    def test_basic_divination(self):
        result = self.divination.perform_divination()
        self.assertIsNotNone(result)
        self.assertIn('hexagram', result)
        self.assertIn('interpretation', result)

    def test_divination_with_specific_parameters(self):
        parameters = {'method': 'random', 'times': 3}
        result = self.divination.perform_divination(parameters)
        self.assertIsNotNone(result)
        self.assertIn('hexagram', result)
        self.assertIn('interpretation', result)

    def test_invalid_divination_method(self):
        parameters = {'method': 'invalid_method'}
        with self.assertRaises(ValueError):
            self.divination.perform_divination(parameters)

if __name__ == '__main__':
    unittest.main()