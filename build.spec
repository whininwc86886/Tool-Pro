# build.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\NINGMEI\\Desktop\\tool Pro'],  # 修改为你的项目路径
    binaries=[],
    datas=[
        ('languages/*.json', 'languages'),
        ('plugins/*', 'plugins'),
        ('logs', 'logs')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Tool_Pro',  # 生成的 .exe 文件名
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # 如果不需要控制台窗口，设置为 False
    icon='icon.ico',  # 可选：指定图标文件
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Tool_Pro',  # 生成的文件夹名称
)