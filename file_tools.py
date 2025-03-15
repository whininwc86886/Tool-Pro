# tools/file_tools.py
import os
from typing import List, Dict

class FileTools:
    @staticmethod
    def search_files(directory: str, pattern: str) -> List[str]:
        """搜索文件"""
        matches = []
        for root, _, files in os.walk(directory):
            for filename in files:
                if pattern in filename:
                    matches.append(os.path.join(root, filename))
        return matches

    @staticmethod
    def calculate_folder_size(path: str) -> int:
        """计算文件夹大小（单位：字节）"""
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    @staticmethod
    def find_duplicate_files(directory: str) -> Dict[str, list]:
        """查找重复文件"""
        hashes = {}
        for root, _, files in os.walk(directory):
            for filename in files:
                path = os.path.join(root, filename)
                file_hash = SecurityTools.file_hash(path)
                if file_hash not in hashes:
                    hashes[file_hash] = []
                hashes[file_hash].append(path)
        return {k: v for k, v in hashes.items() if len(v) > 1}

    @staticmethod
    def batch_rename(directory: str, pattern: str, replacement: str):
        """批量重命名文件"""
        for filename in os.listdir(directory):
            new_name = re.sub(pattern, replacement, filename)
            src = os.path.join(directory, filename)
            dst = os.path.join(directory, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} -> {new_name}")