#!/usr/bin/env python
"""
简单的测试脚本 - 验证基本功能
"""
import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_imports():
    """测试所有模块是否能正常导入"""
    try:
        print("🔍 测试模块导入...")
        
        # 测试核心模块
        from src.meihua.yao import Yao
        from src.meihua.bagua import Hexagram
        from src.meihua.core import calculate_hexagram
        from src.meihua.divination import Divination
        from src.meihua.divination_methods import DivinationMethods
        print("✅ 核心模块导入成功")
        
        # 测试服务层
        from services.divination_service import divination_service
        print("✅ 服务层导入成功")
        
        # 测试应用
        from app import app
        print("✅ FastAPI应用导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False

def test_basic_functionality():
    """测试基本功能"""
    try:
        print("\n🧪 测试基本功能...")
        
        # 测试Yao类
        from src.meihua.yao import Yao
        yao = Yao(1, 0)  # 阳爻，静爻
        print(f"✅ 爻创建成功: {yao}")
        
        # 测试Hexagram类
        from src.meihua.bagua import Hexagram
        hexagram = Hexagram("乾", "乾")
        print(f"✅ 卦象创建成功: {hexagram.name}")
        
        # 测试占卜服务
        from services.divination_service import divination_service
        result = divination_service.perform_divination("random")
        print(f"✅ 占卜服务正常: {result['hexagram']['name']}")
        
        return True
    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api():
    """测试API功能"""
    try:
        print("\n🌐 测试API功能...")
        
        from fastapi.testclient import TestClient
        from app import app
        
        client = TestClient(app)
        
        # 测试健康检查
        response = client.get("/health")
        if response.status_code == 200:
            print("✅ 健康检查API正常")
        else:
            print(f"❌ 健康检查失败: {response.status_code}")
            return False
        
        # 测试主页
        response = client.get("/")
        if response.status_code == 200 and "梅花易数" in response.text:
            print("✅ 主页API正常")
        else:
            print(f"❌ 主页访问失败: {response.status_code}")
            return False
        
        # 测试占卜API
        response = client.post("/api/divination", json={"method": "random"})
        if response.status_code == 200:
            data = response.json()
            if "hexagram" in data and "yao_list" in data:
                print("✅ 占卜API正常")
            else:
                print(f"❌ 占卜API响应格式错误: {data}")
                return False
        else:
            print(f"❌ 占卜API失败: {response.status_code}")
            return False
        
        return True
    except Exception as e:
        print(f"❌ API测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("🧪 开始基本功能测试...")
    print("=" * 50)
    
    success_count = 0
    total_tests = 3
    
    # 测试导入
    if test_imports():
        success_count += 1
    
    # 测试基本功能
    if test_basic_functionality():
        success_count += 1
    
    # 测试API
    if test_api():
        success_count += 1
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {success_count}/{total_tests} 通过")
    
    if success_count == total_tests:
        print("🎉 所有基本测试通过！")
        print("💡 现在可以运行完整的pytest测试: pytest tests/ -v")
        return 0
    else:
        print("❌ 部分测试失败，请检查错误信息")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)