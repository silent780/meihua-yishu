"""
梅花易数占卜系统服务层
"""
import os
import sys
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# print(root_path)
sys.path.insert(0, root_path)

import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
from pathlib import Path

from src.meihua import (
    Yao, Hexagram, calculate_hexagram, 
    Divination, DivinationMethods
)
from config import RESULTS_DIR, MAX_HISTORY_DAYS


class DivinationService:
    """占卜服务类"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_directories()
    
    def setup_directories(self):
        """创建必要的目录"""
        results_path = Path(RESULTS_DIR)
        results_path.mkdir(exist_ok=True)
        
        logs_path = Path("logs")
        logs_path.mkdir(exist_ok=True)
    
    def perform_divination(
        self, 
        method: str = "random", 
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        执行占卜
        
        :param method: 占卜方法
        :param params: 占卜参数
        :return: 占卜结果
        """
        try:
            # 输入验证
            if not self._validate_method(method):
                raise ValueError(f"不支持的占卜方法: {method}")
            
            # 获取爻列表
            yao_list = self._get_yao_list(method, params or {})
            
            # 计算卦象
            hexagram = calculate_hexagram(yao_list)
            
            # 生成结果
            result = self._format_result(hexagram, yao_list, method, params)
            
            # 记录历史
            self._save_result(result, method)
            
            self.logger.info(f"成功执行占卜 - 方法: {method}, 卦象: {hexagram.name}")
            return result
            
        except Exception as e:
            self.logger.error(f"占卜执行失败: {str(e)}")
            raise
    
    def _validate_method(self, method: str) -> bool:
        """验证占卜方法"""
        from config import SUPPORTED_METHODS
        return method in SUPPORTED_METHODS
    
    def _get_yao_list(self, method: str, params: Dict[str, Any]) -> List[Yao]:
        """根据方法获取爻列表"""
        try:
            if method == "random":
                return [Yao.random() for _ in range(6)]
            elif method == "time":
                return DivinationMethods.time_based_divination()
            elif method == "number":
                number = params.get("number")
                if number is None:
                    raise ValueError("数字取卦需要提供number参数")
                return DivinationMethods.number_based_divination(int(number))
            elif method == "character":
                character = params.get("character")
                if not character:
                    raise ValueError("测字取卦需要提供character参数")
                return DivinationMethods.character_based_divination(str(character))
            elif method == "event":
                event = params.get("event")
                if not event:
                    raise ValueError("事件取卦需要提供event参数")
                return DivinationMethods.event_based_divination(str(event))
            elif method == "hash":
                text = params.get("text")
                if not text:
                    raise ValueError("哈希取卦需要提供text参数")
                return DivinationMethods.hash_based_divination(str(text))
            else:
                raise ValueError(f"未实现的占卜方法: {method}")
                
        except Exception as e:
            self.logger.error(f"生成爻列表失败 - 方法: {method}, 错误: {str(e)}")
            raise
    
    def _format_result(
        self, 
        hexagram: Hexagram, 
        yao_list: List[Yao], 
        method: str, 
        params: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """格式化占卜结果"""
        yao_positions = ["初爻", "二爻", "三爻", "四爻", "五爻", "上爻"]
        
        yao_details = []
        for i, yao in enumerate(yao_list):
            yao_type = "阳爻" if yao.value == Yao.YANG else "阴爻"
            state = "动爻" if yao.state == Yao.DYNAMIC else "静爻"
            yao_details.append({
                "position": yao_positions[i],
                "symbol": str(yao),
                "type": yao_type,
                "state": state,
                "value": yao.value,
                "is_dynamic": yao.state == Yao.DYNAMIC
            })
        
        return {
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "params": params,
            "hexagram": {
                "name": hexagram.name,
                "text": hexagram.text,
                "explanation": hexagram.explanation,
                "upper_trigram": hexagram.upper,
                "lower_trigram": hexagram.lower
            },
            "yao_list": yao_details,
            "interpretation": Divination.interpret(hexagram),
            "success": True
        }
    
    def _save_result(self, result: Dict[str, Any], method: str):
        """保存占卜结果到文件"""
        try:
            # 创建日期目录
            current_date = datetime.now().strftime("%Y-%m-%d")
            date_dir = Path(RESULTS_DIR) / current_date
            date_dir.mkdir(exist_ok=True)
            
            # 生成文件名
            timestamp = datetime.now().strftime("%H-%M-%S")
            filename = f"{timestamp}_{method}.json"
            filepath = date_dir / filename
            
            # 保存为JSON
            import json
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            self.logger.debug(f"占卜结果已保存: {filepath}")
            
        except Exception as e:
            self.logger.warning(f"保存占卜结果失败: {str(e)}")
    
    def get_history(self, days: int = 7) -> List[Dict[str, Any]]:
        """获取历史占卜记录"""
        try:
            history = []
            results_path = Path(RESULTS_DIR)
            
            # 遍历最近几天的目录
            from datetime import timedelta
            current_date = datetime.now().date()
            
            for i in range(days):
                target_date = current_date - timedelta(days=i)
                date_str = target_date.strftime("%Y-%m-%d")
                date_dir = results_path / date_str
                
                if date_dir.exists():
                    # 读取该日期的所有占卜记录
                    for file_path in date_dir.glob("*.json"):
                        try:
                            import json
                            with open(file_path, "r", encoding="utf-8") as f:
                                result = json.load(f)
                                history.append(result)
                        except Exception as e:
                            self.logger.warning(f"读取历史记录失败: {file_path}, 错误: {str(e)}")
            
            # 按时间倒序排列
            history.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
            return history
            
        except Exception as e:
            self.logger.error(f"获取历史记录失败: {str(e)}")
            return []
    
    def cleanup_old_results(self):
        """清理过期的占卜结果"""
        try:
            results_path = Path(RESULTS_DIR)
            current_date = datetime.now().date()
            
            for date_dir in results_path.iterdir():
                if date_dir.is_dir():
                    try:
                        dir_date = datetime.strptime(date_dir.name, "%Y-%m-%d").date()
                        days_diff = (current_date - dir_date).days
                        
                        if days_diff > MAX_HISTORY_DAYS:
                            import shutil
                            shutil.rmtree(date_dir)
                            self.logger.info(f"已清理过期目录: {date_dir}")
                    except ValueError:
                        # 忽略非日期格式的目录
                        pass
                        
        except Exception as e:
            self.logger.error(f"清理过期结果失败: {str(e)}")


# 全局服务实例
divination_service = DivinationService()

if __name__ == "__main__":
    # 测试占卜服务
    service = DivinationService()
    result = service.perform_divination(method="random")
    import json
    print(json.dumps(result, ensure_ascii=False, indent=2))