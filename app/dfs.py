class FileSearch:
    def __init__(self, file_system):
        self.file_system = file_system  # 模擬檔案系統，字典形式

    def dfs_search(self, current_dir, target_file):
        # 將模擬的文件系統轉換為堆棧處理
        stack = [(current_dir, self.file_system[current_dir])]

        while stack:
            dir_name, dir_content = stack.pop()

            # 如果目錄是文件列表，直接檢查文件是否存在
            if isinstance(dir_content, list):
                if target_file in dir_content:
                    return f"檔案 {target_file} 已找到"
            
            # 如果目錄是嵌套結構，將其加入堆棧
            elif isinstance(dir_content, dict):
                for sub_dir in dir_content:
                    stack.append((sub_dir, dir_content[sub_dir]))
        
        return f"檔案 {target_file} 不存在"
