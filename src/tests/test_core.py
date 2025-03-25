import unittest
from meihua.core import calculate_hexagram  # 假设核心计算逻辑函数
from meihua.utils import generate_random_number  # 假设工具函数

class TestCore(unittest.TestCase):

    def test_calculate_hexagram(self):
        # 测试计算卦象的函数
        result = calculate_hexagram([1, 0, 1, 0, 1, 0])  # 示例输入
        expected = "坤为地"  # 假设的预期结果
        self.assertEqual(result, expected)

    def test_generate_random_number(self):
        # 测试随机数生成函数
        random_number = generate_random_number(1, 6)  # 生成1到6之间的随机数
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 6)

if __name__ == '__main__':
    unittest.main()