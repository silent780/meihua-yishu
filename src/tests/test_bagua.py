import unittest
from meihua.bagua import Bagua

class TestBagua(unittest.TestCase):

    def setUp(self):
        self.bagua = Bagua()

    def test_bagua_names(self):
        expected_names = ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']
        self.assertEqual(self.bagua.get_names(), expected_names)

    def test_bagua_attributes(self):
        attributes = self.bagua.get_attributes()
        self.assertEqual(len(attributes), 8)
        for attr in attributes:
            self.assertIn('name', attr)
            self.assertIn('image', attr)
            self.assertIn('meaning', attr)

    def test_bagua_meaning(self):
        meaning = self.bagua.get_meaning('乾')
        self.assertEqual(meaning, '天，代表创始、强大、积极')

    def test_invalid_bagua(self):
        with self.assertRaises(ValueError):
            self.bagua.get_meaning('无效卦')

if __name__ == '__main__':
    unittest.main()