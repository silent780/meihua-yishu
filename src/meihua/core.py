"""
梅花易数核心计算功能
"""
from .bagua import Hexagram

def calculate_hexagram(yao_list):
    """
    计算六爻卦象
    :param yao_list: 六个爻的列表，从下到上排列
    :return: 卦象对象
    """
    if len(yao_list) != 6:
        raise ValueError("爻列表必须包含6个爻")
    
    # 从爻列表创建卦象
    hexagram = Hexagram.from_yao_list(yao_list)
    
    return hexagram