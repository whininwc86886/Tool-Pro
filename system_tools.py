# tools/system_tools.py
import platform
import psutil
import socket
from datetime import datetime
from typing import Dict

class SystemTools:
    @staticmethod
    def get_system_info() -> dict:
        """获取系统信息"""
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        return {
            '操作系统': platform.system(),
            '主机名': platform.node(),
            '系统版本': platform.release(),
            '处理器': platform.processor(),
            '物理核心数': psutil.cpu_count(logical=False),
            '逻辑核心数': psutil.cpu_count(logical=True),
            '内存总量': f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
            '可用内存': f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
            '启动时间': boot_time.strftime("%Y-%m-%d %H:%M:%S"),
            '运行时间': str(datetime.now() - boot_time),
            'IP地址': socket.gethostbyname(socket.gethostname())
        }