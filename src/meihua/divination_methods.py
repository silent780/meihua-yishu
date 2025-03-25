"""
梅花易数的多种取卦方式
"""
import random
import datetime
import hashlib
from .yao import Yao
from .bagua import Hexagram
from core import calculate_hexagram
class DivinationMethods:
    """梅花易数的取卦方法集合"""
    
    # 八卦数字对应关系（用于数字取卦）
    DIGITS_TO_TRIGRAM = {
        1: "乾", # 天
        2: "兑", # 泽
        3: "离", # 火
        4: "震", # 雷
        5: "巽", # 风
        6: "坎", # 水
        7: "艮", # 山
        8: "坤", # 地
        9: "乾", # 循环，9对应1
        0: "坤", # 0对应8坤
    }
    
    # 五行与八卦的对应关系（用于突发事务取卦）
    FIVE_ELEMENTS = {
        "金": ["乾", "兑"],
        "木": ["震", "巽"],
        "水": ["坎"],
        "火": ["离"],
        "土": ["坤", "艮"]
    }
    
    # 汉字笔画数到六爻的映射表（用于测字取卦）
    STROKES_TO_YAO = {
        1: Yao.YANG,  # 阳爻
        2: Yao.YIN,   # 阴爻
        3: Yao.YANG,
        4: Yao.YIN,
        5: Yao.YANG,
        6: Yao.YIN,
        7: Yao.YANG,
        8: Yao.YIN,
        9: Yao.YANG,
        0: Yao.YIN,   # 10或更多笔画取余后为0时
    }
    
    @staticmethod
    def time_based_divination():
        """
        基于当前时间的取卦方法
        根据年、月、日、时、分、秒各取一爻
        """
        now = datetime.datetime.now()
        
        # 从时间取得6个数值
        year_yao = now.year % 2  # 年份奇数为阳，偶数为阴
        month_yao = now.month % 2
        day_yao = now.day % 2
        hour_yao = now.hour % 2
        minute_yao = now.minute % 2
        second_yao = now.second % 2
        
        # 创建六爻
        yao_list = [
            Yao(second_yao),  # 初爻（最下）
            Yao(minute_yao),  # 二爻
            Yao(hour_yao),    # 三爻
            Yao(day_yao),     # 四爻
            Yao(month_yao),   # 五爻
            Yao(year_yao)     # 上爻（最上）
        ]
        
        # 计算变爻（秒的十位个位之和取3的余数确定哪一爻为动爻）
        dynamic_position = (now.second // 10 + now.second % 10) % 6
        if dynamic_position < len(yao_list):
            yao_list[dynamic_position].state = Yao.DYNAMIC
        
        print(f"基于时间取卦：{now}")
        return yao_list
    
    @staticmethod
    def event_based_divination(event_description):
        """
        基于突发事件的取卦方法
        根据事件描述的特征判断所属五行，然后生成卦象
        
        :param event_description: 事件描述，包含事件类型、方位、颜色等信息
        :return: 六爻列表
        """
        # 五行关键词判断
        five_element_keywords = {
            "金": ["金属", "白色", "秋季", "西方", "圆形", "硬币", "车辆", "武器"],
            "木": ["木材", "绿色", "春季", "东方", "植物", "树木", "家具", "纸张"],
            "水": ["水", "黑色", "冬季", "北方", "流动", "下降", "河流", "海洋"],
            "火": ["火", "红色", "夏季", "南方", "上升", "光明", "电器", "热量"],
            "土": ["土", "黄色", "四季末", "中央", "稳定", "建筑", "山地", "农业"]
        }
        
        # 计算事件描述中包含的五行关键词数量
        element_counts = {element: 0 for element in five_element_keywords}
        for element, keywords in five_element_keywords.items():
            for keyword in keywords:
                if keyword in event_description:
                    element_counts[element] += 1
        
        # 找出最匹配的五行
        dominant_element = max(element_counts, key=element_counts.get)
        if element_counts[dominant_element] == 0:
            # 如果没有明显五行特征，使用事件描述的哈希值
            return DivinationMethods.hash_based_divination(event_description)
        
        # 从对应五行中选择一个八卦作为上卦
        upper_trigram = random.choice(DivinationMethods.FIVE_ELEMENTS[dominant_element])
        
        # 从所有八卦中随机选择一个作为下卦
        all_trigrams = list(Hexagram.BAGUA.keys())
        lower_trigram = random.choice(all_trigrams)
        
        # 根据上下卦生成六爻
        upper_values = Hexagram.BAGUA[upper_trigram]
        lower_values = Hexagram.BAGUA[lower_trigram]
        
        yao_list = [
            Yao(lower_values[0]),
            Yao(lower_values[1]),
            Yao(lower_values[2]),
            Yao(upper_values[0]),
            Yao(upper_values[1]),
            Yao(upper_values[2])
        ]
        
        # 根据事件描述的长度确定动爻位置
        dynamic_position = len(event_description) % 6
        yao_list[dynamic_position].state = Yao.DYNAMIC
        
        print(f"基于事件取卦：{event_description} (五行: {dominant_element})")
        return yao_list
    
    @staticmethod
    def number_based_divination(number):
        """
        基于数字的取卦方法
        
        :param number: 一个整数，用于生成卦象
        :return: 六爻列表
        """
        # 确保数字是正整数
        number = abs(int(number))
        
        # 分解数字的每一位
        digits = [int(digit) for digit in str(number)]
        
        # 如果数字位数少于6，则重复使用这些数字
        while len(digits) < 6:
            digits.extend(digits[:6-len(digits)])
        
        # 只保留前6位数字
        digits = digits[:6]
        
        # 将每个数字映射到八卦
        trigram_indices = [DivinationMethods.DIGITS_TO_TRIGRAM[d] for d in digits]
        
        # 使用前3个数字确定下卦，后3个数字确定上卦
        lower_trigram = trigram_indices[0]
        upper_trigram = trigram_indices[3]
        
        # 从八卦到爻值的转换
        lower_values = Hexagram.BAGUA[lower_trigram]
        upper_values = Hexagram.BAGUA[upper_trigram]
        
        # 创建六爻列表（从下到上）
        yao_list = [
            Yao(lower_values[0]),
            Yao(lower_values[1]),
            Yao(lower_values[2]),
            Yao(upper_values[0]),
            Yao(upper_values[1]),
            Yao(upper_values[2])
        ]
        
        # 使用数字本身来确定动爻
        dynamic_position = number % 6
        yao_list[dynamic_position].state = Yao.DYNAMIC
        
        print(f"基于数字取卦：{number}")
        return yao_list
    
    @staticmethod
    def character_based_divination(character):
        """
        基于汉字测字取卦法
        根据汉字的笔画数生成卦象
        
        :param character: 一个汉字
        :return: 六爻列表
        """
        # 获取汉字笔画数的函数（这里使用简化版，实际应用中可能需要查询字典）
        def get_stroke_count(char):
            # 使用unicodedata或其他库获取笔画数
            # 这里使用字符的unicode码点作为简易替代
            return ord(char) % 10
        
        # 确保只取一个字符
        if len(character) > 1:
            character = character[0]
        
        # 获取笔画数
        stroke_count = get_stroke_count(character)
        
        # 生成六个爻（每个爻的阴阳根据笔画奇偶而定）
        char_hash = hashlib.md5(character.encode()).hexdigest()
        
        # 从哈希值中提取6个数字
        hash_digits = [int(char_hash[i], 16) % 2 for i in range(6)]
        
        # 创建六爻
        yao_list = [Yao(digit) for digit in hash_digits]
        
        # 使用笔画数确定动爻位置
        dynamic_position = stroke_count % 6
        yao_list[dynamic_position].state = Yao.DYNAMIC
        
        print(f"基于测字取卦：'{character}' (笔画数估计: {stroke_count})")
        return yao_list
    
    @staticmethod
    def hash_based_divination(text):
        """
        基于文本哈希的取卦方法（用于其他方法无法应用时）
        
        :param text: 任意文本
        :return: 六爻列表
        """
        # 计算文本的哈希值
        hash_value = hashlib.md5(text.encode()).hexdigest()
        
        # 取哈希值的前6位十六进制数字，并转换为0或1
        yao_values = [int(int(hash_value[i], 16) % 2) for i in range(6)]
        
        # 创建六爻列表
        yao_list = [Yao(value) for value in yao_values]
        
        # 使用哈希值后6位确定动爻
        dynamic_bits = [int(hash_value[i+6], 16) % 2 for i in range(6)]
        for i, is_dynamic in enumerate(dynamic_bits):
            if is_dynamic:
                yao_list[i].state = Yao.DYNAMIC
        
        print(f"基于哈希取卦：{text[:20]}...")
        return yao_list

if __name__ == "__main__":
    # 例如使用时间取卦
    yao_list = DivinationMethods.time_based_divination()
    hexagram = calculate_hexagram(yao_list)