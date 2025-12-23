"""
梅花易数占卜系统 - 核心包
Plum Blossom Numerology Divination System

一个基于传统梅花易数理论的现代化占卜系统
"""

__version__ = "1.0.0"
__author__ = "silent780"
__description__ = "梅花易数占卜系统"

# 核心导入
from .core.yao import Yao
from .core.hexagram import Hexagram
from .core.calculator import HexagramCalculator
from .methods.divination_engine import DivinationEngine
from .utils.interpreter import Interpreter

# 便捷接口
def quick_divination(method="random", **params):
    """快速占卜接口"""
    engine = DivinationEngine()
    return engine.divine(method, **params)

def interpret_hexagram(hexagram):
    """解释卦象"""
    interpreter = Interpreter()
    return interpreter.interpret(hexagram)

# 导出的公共接口
__all__ = [
    "Yao",
    "Hexagram", 
    "HexagramCalculator",
    "DivinationEngine",
    "Interpreter",
    "quick_divination",
    "interpret_hexagram"
]