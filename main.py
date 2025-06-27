import os
from mcp.server.fastmcp import FastMCP

# ========================
# 从 config 模块导入最终配置
# ========================
from config import config

# =======================
# 导入插件注册模块
# =======================
from plugins.register_all_plugins import register_all_plugins

# =====================
# MCP实例创建
# =====================
mcp = FastMCP()
# ====================
# 插件注册
# ====================
register_all_plugins(mcp)


# ========================
# 主程序入口
# ========================
if __name__ == "__main__":
    # 打印配置信息（验证用）
    print(f"[INFO] 写入功能已 {'启用' if config.WRITE_ENABLED else '禁用'}")
    print(f"[INFO] 允许读/写真实路径: {config.ALLOWED_WRITE_DIR}")
    # 切换默认工作目录到 rootdir (ALLOWED_WRITE_DIR)
    try:
        os.chdir(config.ALLOWED_WRITE_DIR)
        print(f"[INFO] 已切换默认工作目录至: {os.getcwd()}")
    except Exception as e:
        print(f"[ERROR] 无法切换工作目录至 {config.ALLOWED_WRITE_DIR}: {str(e)}")
        exit(1)
    print(f"[INFO] 启动 MCP 服务器...")
    try:
        mcp.run(transport='stdio')
        # mcp.run(transport='sse')
    except Exception as e:
        print(f"[ERROR] 启动失败: {str(e)}")