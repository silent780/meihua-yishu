# 梅花易数占卜系统配置文件

# API配置
API_HOST = "0.0.0.0"
API_PORT = 8000
API_DEBUG = False

# 应用配置
APP_NAME = "梅花易数占卜系统"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "基于传统梅花易数的现代化占卜系统"

# 文件存储配置
RESULTS_DIR = "divination_results"
MAX_HISTORY_DAYS = 30  # 历史记录保存天数

# 占卜配置
DEFAULT_DIVINATION_METHOD = "random"
SUPPORTED_METHODS = [
    "random",      # 随机取卦
    "time",        # 时间取卦
    "number",      # 数字取卦
    "character",   # 测字取卦
    "event",       # 事件取卦
    "hash"         # 哈希取卦
]

# 日志配置
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "logs/meihua.log"

# 数据库配置（可选，用于持久化）
DATABASE_URL = "sqlite:///./meihua.db"

# 安全配置
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30