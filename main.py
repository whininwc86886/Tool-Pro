# -*- coding: utf-8 -*-
import os
import sys
from colorama import init, Fore, Style

# 初始化颜色支持
init(autoreset=True)

def show_fancy_title():
    """用符号装饰显示汉字标题"""
    title = f"""
    {Fore.CYAN}
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║  ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗   ║
    ║  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ╚██╗██╔╝   ║
    ║     ██║   ██║   ██║██║   ██║██║      ╚███╔╝    ║
    ║     ██║   ██║   ██║██║   ██║██║      ██╔██╗    ║
    ║     ██║   ╚██████╔╝╚██████╔╝███████╗██╔╝ ██╗   ║
    ║     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ║
    ║                                                ║
    ║           {Fore.YELLOW}Tool Pro 专 业 版{Fore.CYAN}                  ║
    ╚════════════════════════════════════════════════╝
    {Style.RESET_ALL}
    """
    print(title)

def main():
    # 检查是否在CMD中运行
    if sys.stdout.encoding.lower() != 'utf-8':
        os.system('chcp 65001 > nul')
    
    # 显示标题
    show_fancy_title()

    # 等待用户按下回车键
    input("请按下回车键继续...")

    # 进入主菜单
    from ui.text_ui import TextUI
    ui = TextUI()
    ui.run()

if __name__ == "__main__":
    main()