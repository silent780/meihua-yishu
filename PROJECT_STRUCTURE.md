# 📁 项目结构说明

## 🏗️ 整理后的项目结构

```
meihua-yishu/
├── 📄 app.py                    # ✅ 主应用入口 - FastAPI Web服务器
├── 📄 config.py                 # ✅ 配置文件 - 系统配置参数
├── 📄 requirements.txt          # ✅ Python依赖包列表
├── 📄 setup.py                  # ✅ 项目安装配置
├── 📄 启动服务.bat             # ✅ Windows启动脚本
├── 📄 README.md                 # ✅ 项目说明文档
├── 📄 LICENSE                   # ✅ 开源协议
├── 📄 .gitignore                # ✅ Git忽略文件配置
├── 📄 Dockerfile                # ✅ Docker容器化配置
├── 📄 docker-compose.yml        # ✅ Docker Compose配置
├── 📄 nginx.conf                # ✅ Nginx反向代理配置
│
├── 📁 src/meihua/               # ✅ 核心算法包
│   ├── __init__.py              # 包初始化文件
│   ├── yao.py                   # 爻类定义
│   ├── bagua.py                 # 八卦和六十四卦定义
│   ├── core.py                  # 核心计算逻辑
│   ├── divination.py            # 占卜解读逻辑
│   ├── divination_methods.py    # 各种取卦方法
│   ├── utils.py                 # 工具函数
│   └── exp.py                   # 扩展功能
│
├── 📁 services/                 # ✅ 业务服务层
│   ├── __init__.py              # 服务层初始化
│   └── divination_service.py    # 占卜服务实现
│
├── 📁 tests/                    # ✅ 测试代码
│   ├── __init__.py              # 测试包初始化
│   ├── conftest.py              # pytest配置和fixture
│   ├── test_api.py              # API接口测试
│   ├── test_bagua.py            # 八卦功能测试
│   ├── test_core.py             # 核心算法测试
│   ├── test_divination.py       # 占卜功能测试
│   ├── test_divination_methods.py # 取卦方法测试
│   ├── test_service.py          # 服务层测试
│   └── test_yao.py              # 爻功能测试
│
├── 📁 examples/                 # ✅ 使用示例
│   ├── basic_usage.py           # 基础使用示例
│   └── full_divination.py       # 完整占卜示例
│
├── 📁 static/                   # ✅ 静态文件目录
├── 📁 templates/                # ✅ 模板文件目录
├── 📁 logs/                     # ✅ 日志文件目录
└── 📁 divination_results/       # ✅ 占卜结果存储目录

```

## 🗑️ 已删除的重复文件

以下文件因为功能重复或不必要已被删除：

- ❌ `main.py` - 与app.py功能重复的FastAPI应用
- ❌ `run.py` - 重复的启动脚本
- ❌ `server.py` - 重复的服务器启动文件
- ❌ `start_server.py` - 重复的启动文件
- ❌ `src/tests/` - 与根目录tests/重复的测试文件夹
- ❌ `__pycache__/` - Python缓存文件夹

## 📋 核心文件说明

### 🚀 启动入口
- **app.py** - 主要的FastAPI Web应用，包含所有API路由和Web界面

### ⚙️ 配置文件
- **config.py** - 系统配置，包括API设置、文件路径、支持的占卜方法等

### 🧠 核心算法
- **src/meihua/** - 梅花易数核心算法实现
  - `yao.py` - 爻的定义和操作
  - `bagua.py` - 八卦和六十四卦的定义
  - `core.py` - 核心计算逻辑
  - `divination_methods.py` - 六种取卦方法实现

### 🔧 服务层
- **services/divination_service.py** - 占卜业务逻辑服务

### 🧪 测试代码
- **tests/** - 完整的pytest测试套件，覆盖所有功能模块

## 🎯 启动方式

1. **Windows用户**: 双击 `启动服务.bat`
2. **命令行**: `python app.py`
3. **开发模式**: `uvicorn app:app --reload --port 4949`

## 📊 项目特点

✅ **结构清晰** - 单一职责，避免重复  
✅ **易于维护** - 模块化设计，职责分离  
✅ **完整测试** - 全面的测试覆盖  
✅ **部署就绪** - Docker和Nginx配置完整  
✅ **文档完善** - 代码注释和使用示例  

项目现在结构清晰，没有冗余文件，便于维护和部署！🎉