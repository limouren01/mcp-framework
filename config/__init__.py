#config/__init__.py
import os
from pathlib import Path
from .cli_config import load_cli_config
from .env_config import load_env_config

DEFAULT_CONFIG = {
    "DB_HOST": "localhost",
    "DB_USER": "root",
    "DB_PASSWORD": "",
    "DB_NAME": "",
    "DB_PORT": 3306,
    "MCP_ALLOWWRITE": "false",
    "MCP_ROOTDIR": "",
}

# 加载配置
cli_config = load_cli_config()
env_config = load_env_config()

# 合并配置，优先级：CLI > ENV > DEFAULTS
config_dict = {}

all_keys = set(cli_config.keys()) | set(env_config.keys()) | set(DEFAULT_CONFIG.keys())

for key in all_keys:
    if key in cli_config:
        config_dict[key] = cli_config[key]
    elif key in env_config:
        config_dict[key] = env_config[key]
    else:
        config_dict[key] = DEFAULT_CONFIG.get(key)
config_dict["ALLOWED_READ_DIR"] = config_dict.get("MCP_ROOTDIR")
config_dict["ALLOWED_WRITE_DIR"] = config_dict.get("MCP_ROOTDIR")
config_dict["WRITE_ENABLED"] = config_dict.get("MCP_ALLOWWRITE", "false").lower() == "true"

def is_path_allowed(target_path: str, allowed_dir: str) -> bool:
    """检查目标路径是否在允许的目录范围内"""
    if not allowed_dir:
        return False
    
    # 解析为绝对路径
    target = Path(os.path.abspath(target_path)).resolve()
    allowed = Path(os.path.abspath(allowed_dir)).resolve()
    
    # 检查目标是否在允许目录内
    try:
        target.relative_to(allowed)
        return True
    except ValueError:
        return False

# 将配置转为属性访问方式（可选）
class Config:
    def __init__(self):
        self.is_path_allowed = is_path_allowed
    def __getattr__(self, item):
        return config_dict.get(item)

    def get(self, item, default=None):
        return config_dict.get(item, default)

    def __repr__(self):
        return repr(config_dict)

# 实例化单例
config = Config()