# ui/gui.py
from tkinter import Tk, Frame, Label, Button
from i18n import _
from tools.file_tools import FileTools

def launch_gui():
    """启动图形用户界面"""
    root = Tk()
    root.title(_("工具箱"))
    root.geometry("400x300")

    main_frame = Frame(root)
    main_frame.pack(expand=True, fill='both')

    Label(main_frame, text=_("欢迎使用工具箱")).pack(pady=20)
    
    Button(main_frame, text=_("系统信息"), command=lambda: print("显示系统信息")).pack()
    Button(main_frame, text=_("网络工具"), command=lambda: print("打开网络工具")).pack()
    Button(main_frame, text=_("退出"), command=root.quit).pack()

    root.mainloop()