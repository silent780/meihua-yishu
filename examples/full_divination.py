
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 
print(root_path)
sys.path.insert(0, root_path)
from src.meihua.core import calculate_hexagram
from src.meihua.bagua import Hexagram
from src.meihua.yao import Yao
from src.meihua.divination import Divination

def full_divination():
    # 进行完整的占卜过程
    print("开始完整占卜...")

    # 随机生成六个爻
    yao_list = [Yao.random() for _ in range(6)]
    
    # 计算卦象
    hexagram = calculate_hexagram(yao_list)
    
    # 输出卦象
    print("卦象:", hexagram.name)
    print("卦辞:", hexagram.text)
    
    # 进行占卜解析
    divination_result = Divination.interpret(hexagram)
    
    # 输出占卜结果
    print("占卜结果:", divination_result)

if __name__ == "__main__":
    full_divination()