# plugins/register_all_plugins.py

from .prompt_register.prompts_register_plugin import register_prompt_plugins as register_prompts
from .resource_register.resources_register_plugin import register_resource_plugins as register_resources
from .tool_register.tools_register_plugin import register_tool_plugins as register_tools

def register_all_plugins(mcp):
    """
    统一注册所有插件到 MCP 系统中。
    """
    register_resources(mcp)
    register_prompts(mcp)
    register_tools(mcp)