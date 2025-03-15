import logging
from logging.handlers import TimedRotatingFileHandler
import os
from typing import Optional

def setup_logger(name: str = "toolbox", 
                log_level: int = logging.DEBUG,
                log_dir: str = "logs",
                max_log_days: int = 7) -> logging.Logger:
    """配置日志系统"""
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # 文件日志处理器
    file_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "toolbox.log"),
        when="midnight",
        interval=1,
        backupCount=max_log_days,
        encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    # 控制台日志处理器
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    return logger