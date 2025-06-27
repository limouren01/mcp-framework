#config/env_config.py
from dotenv import dotenv_values
from typing import Dict
import os

def get_project_root():
    """获取项目根目录"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_env_config(env_file: str = ".env") -> Dict[str, str]:
    """
    加载 .env 文件并支持递归替换占位符，具有更强的鲁棒性和安全性。
    """
    project_root = get_project_root()
    env_path = os.path.join(project_root, env_file)
    env_vars = dotenv_values(env_path)
    #获取env文件路径

    def replace_placeholders(value: str, env_vars: dict, resolved: set = None) -> str:
        if not isinstance(value, str):
            return value

        if resolved is None:
            resolved = set()

        # 检测循环依赖
        unresolved = set()

        while "${" in value:
            start_idx = value.find("${")
            end_idx = value.find("}", start_idx + 2)

            if end_idx == -1:
                raise ValueError(f"未闭合的占位符: {value[start_idx:]}")

            full_placeholder = value[start_idx:end_idx + 1]
            var_name = value[start_idx + 2:end_idx].strip()

            if var_name in unresolved:
                raise ValueError(f"检测到循环依赖: {' -> '.join(resolved)} -> {var_name}")

            if var_name in resolved:
                raise ValueError(f"嵌套循环依赖: {var_name} 已被解析")

            replacement = env_vars.get(var_name)
            if replacement is None:
                replacement = os.getenv(var_name)  # 尝试从系统环境变量获取

            if replacement is None:
                print(f"[WARNING] 未找到变量 '{var_name}'，占位符将保留原样")
                unresolved.add(var_name)
                continue

            value = value.replace(full_placeholder, replacement, 1)
            resolved.add(var_name)

        return value


    if not env_vars:
        raise FileNotFoundError(f"无法读取环境配置文件: {env_file}")

    # Step 2: 去除每个值两边的引号（单引号、双引号）
    cleaned_env_vars = {
        key: value.strip('"').strip("'") if isinstance(value, str) else value
        for key, value in env_vars.items()
    }

    # Step 3: 替换所有占位符（支持递归替换）
    final_env_vars = {}
    for key, value in cleaned_env_vars.items():
        try:
            final_env_vars[key] = replace_placeholders(str(value), cleaned_env_vars)
        except Exception as e:
            raise ValueError(f"在解析变量 [{key}] 时出错: {e}") from e

    return final_env_vars