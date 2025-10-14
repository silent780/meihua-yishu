"""
梅花易数占卜系统 - FastAPI主应用
"""
import os
import sys
import uvicorn
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
import logging
from datetime import datetime

# 添加项目根目录到Python路径
root_path = Path(__file__).parent
sys.path.insert(0, str(root_path))

from services.divination_service import divination_service

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title="梅花易数占卜系统",
    description="基于传统梅花易数的现代化占卜系统",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 创建静态文件和模板目录
static_dir = root_path / "static"
templates_dir = root_path / "templates"
static_dir.mkdir(exist_ok=True)
templates_dir.mkdir(exist_ok=True)

# 挂载静态文件
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 模板引擎
if templates_dir.exists():
    templates = Jinja2Templates(directory=templates_dir)

# 请求模型
class DivinationRequest(BaseModel):
    method: str = "random"
    params: Optional[Dict[str, Any]] = None

class HistoryRequest(BaseModel):
    days: int = 7

# API路由
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """主页"""
    return HTMLResponse(content=get_index_html(), status_code=200)

@app.post("/api/divination")
async def perform_divination(request: DivinationRequest):
    """执行占卜"""
    try:
        result = divination_service.perform_divination(
            method=request.method,
            params=request.params
        )
        return JSONResponse(content=result)
    except Exception as e:
        logger.error(f"占卜失败: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/history")
async def get_history(request: HistoryRequest):
    """获取历史记录"""
    try:
        history = divination_service.get_history(days=request.days)
        return JSONResponse(content={"history": history, "count": len(history)})
    except Exception as e:
        logger.error(f"获取历史记录失败: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/methods")
async def get_supported_methods():
    """获取支持的占卜方法"""
    methods = {
        "random": {"name": "随机取卦", "description": "传统铜钱法随机取卦", "params": []},
        "time": {"name": "时间取卦", "description": "基于当前时间取卦", "params": []},
        "number": {"name": "数字取卦", "description": "根据数字生成卦象", "params": [{"name": "number", "type": "int", "required": True}]},
        "character": {"name": "测字取卦", "description": "基于汉字笔画取卦", "params": [{"name": "character", "type": "string", "required": True}]},
        "event": {"name": "事件取卦", "description": "基于事件描述取卦", "params": [{"name": "event", "type": "string", "required": True}]},
        "hash": {"name": "哈希取卦", "description": "基于文本哈希取卦", "params": [{"name": "text", "type": "string", "required": True}]}
    }
    return JSONResponse(content=methods)

@app.get("/api/stats")
async def get_statistics():
    """获取统计信息"""
    try:
        history = divination_service.get_history(days=30)
        
        # 统计各种方法的使用次数
        method_stats = {}
        hexagram_stats = {}
        
        for record in history:
            method = record.get("method", "unknown")
            hexagram_name = record.get("hexagram", {}).get("name", "unknown")
            
            method_stats[method] = method_stats.get(method, 0) + 1
            hexagram_stats[hexagram_name] = hexagram_stats.get(hexagram_name, 0) + 1
        
        return JSONResponse(content={
            "total_divinations": len(history),
            "method_distribution": method_stats,
            "hexagram_distribution": dict(list(hexagram_stats.items())[:10]),  # 前10个最常见的卦象
            "last_30_days": len(history)
        })
        
    except Exception as e:
        logger.error(f"获取统计信息失败: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

def get_index_html():
    """获取主页HTML"""
    return """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>梅花易数占卜系统</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            width: 90%;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            color: #666;
            font-size: 1.1em;
        }
        
        .divination-form {
            margin-bottom: 30px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            color: #333;
            font-weight: bold;
        }
        
        select, input, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        select:focus, input:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            font-size: 18px;
            cursor: pointer;
            transition: transform 0.3s;
            width: 100%;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .result {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            display: none;
        }
        
        .hexagram {
            text-align: center;
            margin-bottom: 20px;
        }
        
        .hexagram h2 {
            color: #333;
            font-size: 2em;
            margin-bottom: 10px;
        }
        
        .hexagram p {
            color: #666;
            font-size: 1.1em;
        }
        
        .yao-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 10px;
            margin: 20px 0;
        }
        
        .yao-item {
            text-align: center;
            padding: 10px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .interpretation {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        .loading {
            display: none;
            text-align: center;
            color: #667eea;
        }
        
        .params-section {
            display: none;
        }
        
        .history-section {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        
        .history-item {
            background: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌸 梅花易数占卜系统</h1>
            <p>传统易学智慧与现代技术的完美结合</p>
        </div>
        
        <form class="divination-form" id="divinationForm">
            <div class="form-group">
                <label for="method">选择占卜方法：</label>
                <select id="method" name="method" onchange="toggleParams()">
                    <option value="random">随机取卦（传统铜钱法）</option>
                    <option value="time">时间取卦（基于当前时间）</option>
                    <option value="number">数字取卦（根据数字生成）</option>
                    <option value="character">测字取卦（汉字笔画分析）</option>
                    <option value="event">事件取卦（五行属性判断）</option>
                    <option value="hash">哈希取卦（文本哈希算法）</option>
                </select>
            </div>
            
            <div id="numberParams" class="params-section">
                <div class="form-group">
                    <label for="number">请输入数字：</label>
                    <input type="number" id="number" name="number" placeholder="输入任意数字">
                </div>
            </div>
            
            <div id="characterParams" class="params-section">
                <div class="form-group">
                    <label for="character">请输入汉字：</label>
                    <input type="text" id="character" name="character" placeholder="输入一个汉字" maxlength="1">
                </div>
            </div>
            
            <div id="eventParams" class="params-section">
                <div class="form-group">
                    <label for="event">请描述事件：</label>
                    <textarea id="event" name="event" rows="3" placeholder="描述您想要占卜的事件或情况"></textarea>
                </div>
            </div>
            
            <div id="hashParams" class="params-section">
                <div class="form-group">
                    <label for="text">请输入文本：</label>
                    <textarea id="text" name="text" rows="3" placeholder="输入任意文本内容"></textarea>
                </div>
            </div>
            
            <button type="submit" class="btn">开始占卜</button>
        </form>
        
        <div class="loading" id="loading">
            <p>🔮 正在为您占卜，请稍候...</p>
        </div>
        
        <div class="result" id="result">
            <div class="hexagram" id="hexagram">
                <!-- 卦象结果 -->
            </div>
            
            <div class="yao-list" id="yaoList">
                <!-- 六爻详情 -->
            </div>
            
            <div class="interpretation" id="interpretation">
                <!-- 卦象解释 -->
            </div>
        </div>
        
        <div class="history-section">
            <h3>📜 最近占卜记录</h3>
            <button type="button" class="btn" onclick="loadHistory()" style="width: auto; padding: 10px 20px; font-size: 14px; margin-bottom: 15px;">加载历史记录</button>
            <div id="historyList">
                <!-- 历史记录 -->
            </div>
        </div>
    </div>

    <script>
        // 切换参数输入区域
        function toggleParams() {
            const method = document.getElementById('method').value;
            const paramSections = document.querySelectorAll('.params-section');
            
            // 隐藏所有参数区域
            paramSections.forEach(section => {
                section.style.display = 'none';
            });
            
            // 显示对应的参数区域
            if (method === 'number') {
                document.getElementById('numberParams').style.display = 'block';
            } else if (method === 'character') {
                document.getElementById('characterParams').style.display = 'block';
            } else if (method === 'event') {
                document.getElementById('eventParams').style.display = 'block';
            } else if (method === 'hash') {
                document.getElementById('hashParams').style.display = 'block';
            }
        }
        
        // 提交占卜表单
        document.getElementById('divinationForm').onsubmit = async function(e) {
            e.preventDefault();
            
            const method = document.getElementById('method').value;
            let params = {};
            
            // 根据方法收集参数
            if (method === 'number') {
                const number = document.getElementById('number').value;
                if (!number) {
                    alert('请输入数字');
                    return;
                }
                params.number = parseInt(number);
            } else if (method === 'character') {
                const character = document.getElementById('character').value;
                if (!character) {
                    alert('请输入汉字');
                    return;
                }
                params.character = character;
            } else if (method === 'event') {
                const event = document.getElementById('event').value;
                if (!event) {
                    alert('请描述事件');
                    return;
                }
                params.event = event;
            } else if (method === 'hash') {
                const text = document.getElementById('text').value;
                if (!text) {
                    alert('请输入文本');
                    return;
                }
                params.text = text;
            }
            
            // 显示加载状态
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            
            try {
                const response = await fetch('/api/divination', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        method: method,
                        params: Object.keys(params).length > 0 ? params : null
                    })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    displayResult(data);
                } else {
                    alert('占卜失败: ' + data.detail);
                }
            } catch (error) {
                alert('网络错误: ' + error.message);
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        };
        
        // 显示占卜结果
        function displayResult(data) {
            const hexagramDiv = document.getElementById('hexagram');
            const yaoListDiv = document.getElementById('yaoList');
            const interpretationDiv = document.getElementById('interpretation');
            
            // 显示卦象
            hexagramDiv.innerHTML = `
                <h2>${data.hexagram.name}</h2>
                <p>${data.hexagram.text}</p>
            `;
            
            // 显示六爻
            yaoListDiv.innerHTML = data.yao_list.map(yao => `
                <div class="yao-item">
                    <div style="font-weight: bold; color: ${yao.is_dynamic ? '#e74c3c' : '#333'};">
                        ${yao.position}
                    </div>
                    <div style="font-size: 24px; margin: 5px 0;">${yao.symbol}</div>
                    <div style="font-size: 12px; color: #666;">
                        ${yao.type} (${yao.state})
                    </div>
                </div>
            `).join('');
            
            // 显示解释
            interpretationDiv.innerHTML = `
                <h3>💫 卦象解释</h3>
                <p>${data.hexagram.explanation}</p>
                <br>
                <h3>🔮 详细解读</h3>
                <p>${data.interpretation}</p>
            `;
            
            document.getElementById('result').style.display = 'block';
        }
        
        // 加载历史记录
        async function loadHistory() {
            try {
                const response = await fetch('/api/history', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({days: 7})
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    const historyListDiv = document.getElementById('historyList');
                    
                    if (data.history.length === 0) {
                        historyListDiv.innerHTML = '<p style="color: #666;">暂无历史记录</p>';
                        return;
                    }
                    
                    historyListDiv.innerHTML = data.history.slice(0, 5).map(record => `
                        <div class="history-item">
                            <div style="font-weight: bold; color: #333;">
                                ${record.hexagram.name} - ${record.method}
                            </div>
                            <div style="font-size: 12px; color: #666; margin-top: 5px;">
                                ${new Date(record.timestamp).toLocaleString('zh-CN')}
                            </div>
                            <div style="margin-top: 8px; font-size: 14px;">
                                ${record.hexagram.text}
                            </div>
                        </div>
                    `).join('');
                } else {
                    alert('获取历史记录失败');
                }
            } catch (error) {
                alert('网络错误: ' + error.message);
            }
        }
        
        // 页面加载时初始化
        document.addEventListener('DOMContentLoaded', function() {
            toggleParams();
        });
    </script>
</body>
</html>
    """

def main():
    """主启动函数"""
    port = 4949  # 换个端口避免冲突
    print("🌸 启动梅花易数占卜系统...")
    print(f"📍 访问地址: http://localhost:{port}")  
    print(f"📚 API文档: http://localhost:{port}/docs")
    print("⏹️  按 Ctrl+C 停止服务")
    print("-" * 50)
    
    try:
        uvicorn.run(
            app,  # 直接传递app对象，不使用字符串
            host="0.0.0.0",
            port=port,
            reload=False,  # 禁用reload避免警告
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 服务已停止")
    except Exception as e:
        logger.error(f"启动失败: {e}")

if __name__ == "__main__":
    main()