"""
爻的定义与操作
"""
import random

class Yao:
    """表示一个爻，可以是阴爻或阳爻，也可以是动爻或静爻"""
    
    YIN = 0  # 阴爻
    YANG = 1  # 阳爻
    
    STATIC = 0  # 静爻
    DYNAMIC = 1  # 动爻
    
    def __init__(self, value, state=0):
        """
        初始化一个爻
        :param value: YIN(0)或YANG(1)
        :param state: STATIC(0)或DYNAMIC(1)
        """
        self.value = value  # 阴阳
        self.state = state  # 动静
    
    @classmethod
    def random(cls):
        """随机生成一个爻"""
        # 使用传统的三枚铜钱方法
        coins = [random.randint(0, 1) for _ in range(3)]
        coin_sum = sum(coins)
        
        if coin_sum == 3:  # 三阳，老阳爻（动爻）
            return cls(cls.YANG, cls.DYNAMIC)
        elif coin_sum == 2:  # 二阳一阴，少阳爻（静爻）
            return cls(cls.YANG, cls.STATIC)
        elif coin_sum == 1:  # 一阳二阴，少阴爻（静爻）
            return cls(cls.YIN, cls.STATIC)
        else:  # 三阴，老阴爻（动爻）
            return cls(cls.YIN, cls.DYNAMIC)
    
    def __str__(self):
        if self.value == self.YANG:
            return "——" if self.state == self.STATIC else "≡"
        else:
            return "--" if self.state == self.STATIC else "≈"
        
