# ui/text_ui.py
from i18n import _
from tools import SystemTools, NetworkTools, SecurityTools, FileTools

class TextUI:
    def __init__(self):
        self.system_tools = SystemTools()
        self.network_tools = NetworkTools()
        self.security_tools = SecurityTools()
        self.file_tools = FileTools()

    def show_menu(self):
        """显示主菜单"""
        print("\n" + "=" * 30)
        print(_(" Python全能工具箱 "))
        print("=" * 30)
        print(_("1. 系统信息"))
        print(_("2. 网络工具"))
        print(_("3. 安全工具"))
        print(_("4. 文件工具"))
        print(_("0. 退出"))

    def run(self):
        """运行主循环"""
        while True:
            self.show_menu()
            choice = input(_("请选择操作："))

            if choice == '0':
                print(_("感谢使用，再见！"))
                break
            elif choice == '1':
                self.show_system_info()
            elif choice == '2':
                self.show_network_tools()
            elif choice == '3':
                self.show_security_tools()
            elif choice == '4':
                self.show_file_tools()
            else:
                print(_("无效选择，请重新输入！"))

    def show_system_info(self):
        """显示系统信息"""
        info = self.system_tools.get_system_info()
        print("\n系统信息：")
        for key, value in info.items():
            print(f"{key}: {value}")

    def show_network_tools(self):
        """显示网络工具菜单"""
        print("\n网络工具：")
        print("1. 端口扫描")
        print("2. 网站信息查询")
        choice = input(_("请选择操作："))
        if choice == '1':
            host = input("请输入要扫描的主机：")
            start_port = int(input("请输入起始端口："))
            end_port = int(input("请输入结束端口："))
            result = self.network_tools.port_scan(host, start_port, end_port)
            print(f"开放端口：{result['open_ports']}")
        elif choice == '2':
            url = input("请输入网站URL：")
            info = self.network_tools.website_info(url)
            print("\n网站信息：")
            for key, value in info.items():
                print(f"{key}: {value}")

    def show_security_tools(self):
        """显示安全工具菜单"""
        print("\n安全工具：")
        print("1. 生成随机密码")
        print("2. 检查密码强度")
        choice = input(_("请选择操作："))
        if choice == '1':
            length = int(input("请输入密码长度："))
            password = self.security_tools.generate_password(length)
            print(f"生成的密码：{password}")
        elif choice == '2':
            password = input("请输入要检查的密码：")
            strength = self.security_tools.password_strength(password)
            print(f"密码强度：{strength['strength']}")

    def show_file_tools(self):
        """显示文件工具菜单"""
        print("\n文件工具：")
        print("1. 搜索文件")
        print("2. 计算文件夹大小")
        choice = input(_("请选择操作："))
        if choice == '1':
            directory = input("请输入要搜索的目录：")
            pattern = input("请输入文件名模式：")
            files = self.file_tools.search_files(directory, pattern)
            print("\n找到的文件：")
            for file in files:
                print(file)
        elif choice == '2':
            path = input("请输入文件夹路径：")
            size = self.file_tools.calculate_folder_size(path)
            print(f"文件夹大小：{size / 1024 / 1024:.2f} MB")