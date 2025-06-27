import os
import openpyxl
from config import config

def write_to_file(file_path: str, content: str) -> dict:
    """写入文件（多层校验）"""
    if not config.WRITE_ENABLED:
        return {"success": False, "message": "写入功能未启用"}

    abs_path = os.path.abspath(file_path)
    if not config.is_path_allowed(abs_path, config.ALLOWED_WRITE_DIR):
        return {"success": False, "message": "路径越权访问"}

    try:
        # 创建父目录（自动校验路径合法性）
        parent_dir = os.path.dirname(abs_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
            # 二次校验创建的目录是否合法
            if not config.is_path_allowed(parent_dir, config.ALLOWED_WRITE_DIR):
                raise PermissionError("父目录越权")
        
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return {"success": True, "message": "文件写入成功"}
    except Exception as e:
        return {"success": False, "message": f"写入失败: {str(e)}"}
    

def write_to_excel(file_path: str, data: list, sheet_name: str = "Sheet1") -> dict:
    """写入Excel文件（多层校验）"""
    if not config.WRITE_ENABLED:
        return {"success": False, "message": "写入功能未启用"}

    abs_path = os.path.abspath(file_path)
    if not config.is_path_allowed(abs_path, config.ALLOWED_WRITE_DIR):
        return {"success": False, "message": "路径越权访问"
                }
    try:
        # 创建父目录（自动校验路径合法性）
        parent_dir = os.path.dirname(abs_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
            # 二次校验创建的目录是否合法
            if not config.is_path_allowed(parent_dir, config.ALLOWED_WRITE_DIR):
                raise PermissionError("父目录越权")

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = sheet_name

        for row_data in data:
            sheet.append(row_data)

        workbook.save(abs_path)
        return {"success": True, "message": "Excel文件写入成功"}
    except Exception as e:
        return {"success": False, "message": f"写入Excel文件失败: {str(e)}"}
    