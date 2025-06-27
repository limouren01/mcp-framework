# 🧩 MCP 文件管理系统框架

> A lightweight and modular framework for building MCP-based file management systems.

---

## 📌 项目简介

这是一个基于 MCP协议构建的文件管理系统的轻量级框架。  
本框架旨在提供标准化的模块结构、灵活的配置系统以及可扩展的功能注册机制，便于开发者快速搭建符合自身需求的 MCP 工具服务。

---

## 🧱 模块概览

| 模块 | 描述 |
|------|------|
| `config/` | 配置管理模块，支持命令行参数、环境变量及默认值 |
| `register/` | MCP 功能注册模块，用于声明 prompts、resources、tools |
| `prompts/` | 存放 prompt 相关实现逻辑 |
| `resources/` | 存放资源类功能实现 |
| `tools/` | 存放工具类功能实现（如增删改查、爬虫、消息发送） |
| `main.py` | 程序入口，负责初始化 MCP 实例并注册功能 |
| `.env.example` | 环境变量配置模板文件 |
| `requirements.txt` | 项目依赖列表 |

---

## ⚙️ 配置模块（`config/`）

### 结构说明：

```
config/
├── cli_config.py     # 命令行参数解析
├── env_config.py     # 环境变量加载
└── __init__.py       # 配置合并与封装
```

### 特性说明：

- **多层级配置优先级**（从高到低）：
  1. 命令行参数（CLI）
  2. 环境变量（`.env` 文件）
  3. 默认配置（硬编码在 `__init__.py` 中）

- **使用方式**：
  ```python
  from config import config

  db_host = config.DB_HOST
  mcp_rootdir = config.MCP_ROOTDIR
  ```

### 扩展建议：

- 可通过修改 `cli_config.py` 添加版本控制开关（如 `--version=basic`），用于区分普通版与会员版功能；
- 认证逻辑由开发者自定义实现，本框架只提供思路

---

## 🔧 注册模块（`register/`）

### 功能说明：

用于将 `prompts`, `resources`, `tools` 三类功能注册为 MCP 兼容接口，使模型能够识别并调用这些功能。

### 结构说明：

```
plugins/
├── prompt_register   # Prompt 类功能注册
├── resource_register # Resource 类功能注册
├── tool_register     # Tool 类功能注册
└── register_all_plugins.py      # 统一注册入口
```

---

## 💡 功能实现模块（`prompts/`, `resources/`, `tools/`）

### 当前结构示例：

```
tools/
└── add   # 示例工具模块
```

- 每个子模块应实现具体功能逻辑；
- 对应的注册模块负责将其暴露给 MCP；
- 开发者可根据需求自行扩展其他功能模块。

---

## 📁 环境配置文件（`.env.example`）

### 使用方法：

1. 复制 `.env.example` 为 `.env`
2. 根据需要修改配置项，例如数据库连接信息、MCP 路径等

```bash
cp .env.example .env
```

### 示例内容：

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=passwd
DB_NAME=programs
DB_PORT=3306

MCP_ALLOWWRITE=false
MCP_ROOTDIR=/path/to/rootdir
```

---

## 🚀 主程序入口（`main.py`）

### 主要职责：

- 加载配置；
- 创建 MCP 服务实例；
- 注册所有可用功能模块；
- 启动服务监听。(将stdio改成sse即可)

---

## 📦 依赖管理（`requirements.txt`）

运行前请确保已安装所有依赖：

```bash
pip install -r requirements.txt
```

---

## 🛠️ 开发建议

- **模块可扩展性强**：你可以根据实际需求，在 `utils/`, `resources/`, `prompts/` 下添加新的功能模块（例如我在自己项目中在工具模块中新增了一个爬虫模块）；
- **认证机制灵活**：可在 CLI 参数中加入权限判断字段（如 `--version=premium`），然后在主程序中根据此字段启用高级功能；
- **配置集中管理**：推荐始终通过 `config.config.XXX` 的方式访问配置，避免重复导入 `.env` 或 `argparse`。

---

## 🌟 总结

这是一个结构清晰、模块化强、易于扩展的 MCP 文件管理框架原型。无论你是想开发一个简单的本地工具，还是构建一个完整的生产级服务，都可以在此基础上进行定制和拓展。
