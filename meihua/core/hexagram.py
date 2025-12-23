"""
卦象类 - 六十四卦的表示和操作
"""
from .constants import BAGUA_MAP, HEXAGRAMS_64

class Hexagram:
    """
    卦象类 - 表示完整的六爻卦象
    
    属性:
        upper_trigram (str): 上卦（外卦）
        lower_trigram (str): 下卦（内卦）  
        name (str): 卦名
        text (str): 卦辞
        explanation (str): 卦象解释
        yao_list (list): 六爻列表
    """
    
    def __init__(self, upper_trigram, lower_trigram, yao_list=None):
        """
        初始化卦象
        
        Args:
            upper_trigram (str): 上卦名称
            lower_trigram (str): 下卦名称  
            yao_list (list, optional): 六爻列表
        """
        self.upper_trigram = upper_trigram
        self.lower_trigram = lower_trigram
        self.yao_list = yao_list or []
        
        # 生成卦象标识
        self.key = self._generate_key()
        
        # 查找卦象信息
        hexagram_info = HEXAGRAMS_64.get(self.key, {})
        self.name = hexagram_info.get("name", "未知卦象")
        self.text = hexagram_info.get("text", "")
        self.explanation = hexagram_info.get("explanation", "")
    
    def _generate_key(self):
        """生成卦象索引键"""
        if self.upper_trigram == self.lower_trigram:
            # 同卦情况：乾乾 -> 乾乾
            return self.upper_trigram + self.lower_trigram
        else:
            # 异卦情况：乾坤 -> 乾坤
            return self.upper_trigram + self.lower_trigram
    
    @classmethod
    def from_yao_list(cls, yao_list):
        """
        从爻列表创建卦象
        
        Args:
            yao_list (list): 六个爻的列表，从下到上
            
        Returns:
            Hexagram: 卦象对象
        """
        if len(yao_list) != 6:
            raise ValueError(f"必须提供6个爻，实际提供了{len(yao_list)}个")
        
        # 下卦（前三爻）和上卦（后三爻）
        lower_pattern = [yao.binary_value for yao in yao_list[:3]]
        upper_pattern = [yao.binary_value for yao in yao_list[3:]]
        
        # 查找对应的八卦
        lower_trigram = cls._find_trigram(lower_pattern)
        upper_trigram = cls._find_trigram(upper_pattern)
        
        return cls(upper_trigram, lower_trigram, yao_list)
    
    @staticmethod
    def _find_trigram(pattern):
        """根据爻模式查找八卦名称"""
        pattern_key = ''.join(map(str, pattern))
        
        for trigram_name, trigram_pattern in BAGUA_MAP.items():
            if ''.join(map(str, trigram_pattern)) == pattern_key:
                return trigram_name
        
        return "未知"
    
    @property
    def full_name(self):
        """完整卦名（包含上下卦）"""
        if self.upper_trigram == self.lower_trigram:
            return f"{self.upper_trigram}为{TRIGRAM_NATURE.get(self.upper_trigram, '')}"
        else:
            upper_nature = TRIGRAM_NATURE.get(self.upper_trigram, self.upper_trigram)
            lower_nature = TRIGRAM_NATURE.get(self.lower_trigram, self.lower_trigram) 
            return f"{upper_nature}{lower_nature}{self.name.split('为')[-1] if '为' in self.name else self.name}"
    
    def get_dynamic_yao(self):
        """获取动爻列表"""
        return [yao for yao in self.yao_list if yao.is_dynamic]
    
    def transform(self):
        """变卦 - 将动爻变为相反的静爻"""
        if not self.yao_list:
            return self
            
        new_yao_list = [yao.transform() for yao in self.yao_list]
        return self.from_yao_list(new_yao_list)
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "name": self.name,
            "text": self.text,
            "explanation": self.explanation,
            "upper_trigram": self.upper_trigram,
            "lower_trigram": self.lower_trigram,
            "key": self.key,
            "yao_list": [yao.to_dict() for yao in self.yao_list] if self.yao_list else []
        }
    
    def __str__(self):
        """字符串表示"""
        return f"{self.name}（{self.upper_trigram}上{self.lower_trigram}下）"
    
    def __repr__(self):
        """调试表示"""
        return f"Hexagram(name='{self.name}', upper='{self.upper_trigram}', lower='{self.lower_trigram}')"


# 八卦对应的自然属性
TRIGRAM_NATURE = {
    "乾": "天",
    "坤": "地", 
    "震": "雷",
    "巽": "风",
    "坎": "水",
    "离": "火",
    "艮": "山",
    "兑": "泽"
}