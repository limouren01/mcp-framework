# prompts/organize_files.py

def organize_files_prompt(
    source_dir: str = ".",
    target_dir: str = "organized",
    file_type: str = ".md"
) -> str:
    """
    提示用户确认整理文件操作。
    
    参数:
        source_dir (str): 要扫描的源目录路径。
        target_dir (str): 要移动到的目标目录路径。
        file_type (str): 要筛选的文件扩展名（如 .md）。
        
    返回:
        str: 用户确认后返回的操作说明。
    """
    return (
        f"即将执行以下操作：\n"
        f"1. 扫描目录：{source_dir}\n"
        f"2. 筛选文件类型：{file_type}\n"
        f"3. 将这些文件移动到目标目录：{target_dir}\n"
        f"请确认是否继续此操作。\n"
    )