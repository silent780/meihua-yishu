# 梅花易数占卜系统

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-red.svg)](https://fastapi.tiangolo.com)

基于传统梅花易数理论，结合现代Web技术打造的智能占卜系统。

## 🌟 特色功能

- **多种取卦方式**: 支持随机、时间、数字、测字、事件、哈希等6种取卦方法
- **完整卦象解读**: 提供64卦完整信息，包括卦名、卦辞、爻辞和详细解释
- **RESTful API**: 基于FastAPI的现代化API接口
- **历史记录**: 自动保存占卜记录，支持历史查询
- **统计分析**: 提供占卜统计和趋势分析
- **响应式界面**: 美观的Web界面，支持移动端访问

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/your-username/meihua-yishu.git
cd meihua-yishu
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动服务**
```bash
# 开发模式
python run.py --mode dev

# 生产模式
python run.py --mode prod

# 功能测试
python run.py --mode test
```

4. **访问应用**
- Web界面: http://localhost:8000
- API文档: http://localhost:8000/docs
- ReDoc文档: http://localhost:8000/redoc

## 📖 API使用说明

### 占卜接口

**POST /divination**

```json
{
  "method": "random",
  "params": {}
}
```

支持的占卜方法：
- `random`: 随机取卦（无需参数）
- `time`: 时间取卦（无需参数）
- `number`: 数字取卦（需要参数 `{"number": 12345}`）
- `character`: 测字取卦（需要参数 `{"character": "福"}`）
- `event`: 事件取卦（需要参数 `{"event": "今天下雨了"}`）
- `hash`: 哈希取卦（需要参数 `{"text": "任意文本"}`）

### 历史记录接口

**POST /history**

```json
{
  "days": 7
}
```

### 统计信息接口

**GET /stats**

获取占卜统计信息，包括方法分布、日期分布等。

## 🏗️ 项目结构

```
meihua-yishu/
├── src/
│   └── meihua/
│       ├── __init__.py          # 包初始化
│       ├── yao.py              # 爻的定义
│       ├── bagua.py            # 八卦和64卦
│       ├── core.py             # 核心计算
│       ├── divination.py       # 占卜解释
│       └── divination_methods.py # 取卦方法
├── services/
│   └── divination_service.py    # 占卜服务层
├── static/                      # 静态文件
├── logs/                        # 日志文件
├── divination_results/          # 占卜结果存储
├── main.py                      # FastAPI应用
├── config.py                    # 配置文件
├── run.py                       # 启动脚本
├── requirements.txt             # 依赖包
└── README.md                    # 项目说明
```

## 🔧 配置说明

编辑 `config.py` 文件可以修改系统配置：

- **API_HOST**: API服务监听地址
- **API_PORT**: API服务端口
- **RESULTS_DIR**: 占卜结果存储目录
- **MAX_HISTORY_DAYS**: 历史记录保存天数
- **LOG_LEVEL**: 日志级别

## 📱 使用示例

### Python客户端示例

```python
import requests

# 进行随机占卜
response = requests.post("http://localhost:8000/divination", json={
    "method": "random"
})
result = response.json()
print(f"卦象: {result['data']['hexagram']['name']}")

# 进行数字占卜
response = requests.post("http://localhost:8000/divination", json={
    "method": "number",
    "params": {"number": 12345}
})
result = response.json()
print(f"卦象: {result['data']['hexagram']['name']}")
```

### curl示例

```bash
# 随机占卜
curl -X POST "http://localhost:8000/divination" \
     -H "Content-Type: application/json" \
     -d '{"method": "random"}'

# 测字占卜
curl -X POST "http://localhost:8000/divination" \
     -H "Content-Type: application/json" \
     -d '{"method": "character", "params": {"character": "福"}}'
```

## 🚀 部署到服务器

### 使用Gunicorn部署

```bash
# 安装gunicorn
pip install gunicorn

# 启动服务
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### 使用Docker部署

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### 使用Nginx反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🔒 安全建议

1. **生产环境配置**
   - 修改 `config.py` 中的 `SECRET_KEY`
   - 设置合适的CORS策略
   - 启用HTTPS

2. **API限流**
   - 考虑添加请求限流中间件
   - 实现用户认证和权限控制

3. **数据安全**
   - 定期备份占卜数据
   - 设置合理的日志轮转策略

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目基于MIT许可证开源 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- 项目主页: https://github.com/your-username/meihua-yishu
- 问题反馈: https://github.com/your-username/meihua-yishu/issues

## 🙏 致谢

- 感谢传统梅花易数理论的古代智慧
- 感谢FastAPI框架的优秀设计
- 感谢所有贡献者的辛勤工作