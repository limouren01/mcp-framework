#导入设置
from typing import Dict, Union
from config import config
# 导入提示函数
from prompts.organize_files import organize_files_prompt


def register_prompt_plugins(mcp):
    """
    实际执行提示插件注册逻辑。
    """
    @mcp.prompt()
    def greeting_prompt(name: str) -> str:
        """
        生成个性化的问候语。
        
        参数:
            name (str): 用户的名字。
            
        返回:
            str: 个性化问候语。
        """
        return f"你好，{name}！欢迎来到我们的服务。请问有什么可以帮助您的吗？"

