"""
爻 - 易经基础单位
代表阴爻和阳爻，以及动爻和静爻
"""

class Yao:
    """
    爻类 - 易经的基本单位
    
    属性:
        value (int): 爻值 (0=阴, 1=阳, 2=老阴, 3=老阳)
        is_dynamic (bool): 是否为动爻
        type (str): 爻的类型 ("阴爻" 或 "阳爻")
        state (str): 爻的状态 ("静" 或 "动")
        symbol (str): 爻的符号表示
    """
    
    YAO_SYMBOLS = {
        0: "- -",    # 阴爻（静）
        1: "---",    # 阳爻（静）
        2: "- -",    # 阴爻（动）
        3: "---"     # 阳爻（动）
    }
    
    def __init__(self, value):
        """
        初始化爻
        
        Args:
            value (int): 爻值 0-3
                0: 静阴爻
                1: 静阳爻  
                2: 动阴爻（老阴）
                3: 动阳爻（老阳）
        """
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError(f"爻值必须是0-3之间的整数，得到: {value}")
        
        self.value = value
        self.is_dynamic = value in (2, 3)  # 2和3是动爻
        
        # 确定阴阳性质（2老阴变阳，3老阳变阴）
        if value in (0, 2):  # 阴爻
            self.type = "阴爻"
            self.symbol = self.YAO_SYMBOLS[value]
            self.position_value = 0
        else:  # 阳爻
            self.type = "阳爻" 
            self.symbol = self.YAO_SYMBOLS[value]
            self.position_value = 1
    
    @property
    def state(self):
        """获取爻的状态"""
        return "动" if self.is_dynamic else "静"
    
    @property 
    def binary_value(self):
        """获取二进制值用于计算卦象"""
        return self.position_value
    
    def transform(self):
        """变爻 - 动爻会变为相反的静爻"""
        if not self.is_dynamic:
            return self
        
        # 老阴变阳爻，老阳变阴爻
        new_value = 1 if self.value == 2 else 0
        return Yao(new_value)
    
    def __str__(self):
        """字符串表示"""
        state_str = "（动）" if self.is_dynamic else ""
        return f"{self.type}{state_str}: {self.symbol}"
    
    def __repr__(self):
        """调试表示"""
        return f"Yao(value={self.value}, type='{self.type}', dynamic={self.is_dynamic})"
    
    def __eq__(self, other):
        """相等比较"""
        return isinstance(other, Yao) and self.value == other.value
    
    def __hash__(self):
        """哈希值"""
        return hash(self.value)
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            "value": self.value,
            "type": self.type,
            "state": self.state,
            "symbol": self.symbol,
            "is_dynamic": self.is_dynamic,
            "binary_value": self.binary_value
        }