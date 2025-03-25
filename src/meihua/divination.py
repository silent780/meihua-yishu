"""
占卜结果解释
"""

class Divination:
    """占卜结果解释"""
    
    @staticmethod
    def interpret(hexagram):
        """
        解释卦象的占卜含义
        :param hexagram: 卦象对象
        :return: 占卜结果解释
        """
        # 基础解释
        result = f"{hexagram.name}：{hexagram.text}\n\n{hexagram.explanation}"
        
        # 这里可以添加更复杂的解释逻辑，如考虑动爻、变卦等
        # 例如根据动爻数量和位置给出不同的解释
        
        return result