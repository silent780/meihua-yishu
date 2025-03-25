import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 
print(root_path)
sys.path.insert(0, root_path)

from src.meihua.core import calculate_hexagram
from src.meihua.bagua import get_hexagram_name
from src.meihua.divination import perform_divination

def basic_usage_example():
    # 进行一次简单的占卜
    hexagram = calculate_hexagram()
    hexagram_name = get_hexagram_name(hexagram)
    
    print(f"得到的卦象: {hexagram_name}")
    
    divination_result = perform_divination(hexagram)
    print("占卜结果:")
    print(divination_result)

if __name__ == "__main__":
    basic_usage_example()