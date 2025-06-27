#导入设置
from typing import Dict, Union
from config import  config
# 导入工具函数
from utils.add.write_to_file import write_to_file, write_to_excel

def register_tool_plugins(mcp): 
    @mcp.tool()
    def _write_to_file(file_path: str, content: str) -> Dict[str, Union[bool, str]]:
        """写入内容到文件（双重路径校验）
        各个参数的意义：
        file_path: 文件路径，包含文件名和扩展名，例如 "data.txt"。
        content: 要写入文件的内容，为字符串类型。
        """
        return write_to_file(file_path, content)
    
    @mcp.tool()
    def _write_to_excel(file_path: str, data: list, sheet_name: str = "Sheet1") -> Dict[str, Union[bool, str]]:
        """写入数据到Excel文件（双重路径校验）
        各个参数的意义：
        file_path: Excel文件路径，包含文件名和扩展名，例如 "data.xlsx"。
        data: 要写入Excel文件的数据，为二维列表，每个子列表表示一行数据。
        sheet_name: Excel工作表名称，默认为 "Sheet1"。
        写入excel文件优先使用该工具，注意，该工具无法覆盖原文件，只能生成新的excel"""
        return write_to_excel(file_path, data, sheet_name)

