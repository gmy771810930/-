import os
import ctypes
from tkinter import Tk, filedialog

os.name = 'nt'

# 设置控制台标题
print(os.system('title "软件文件夹图标创建器"'))

# 打开文件选择对话框
print(f"请选择exe文件")
root = Tk()
root.withdraw()  # 隐藏窗口
exe_file_path = filedialog.askopenfilename(title="选择exe文件", filetypes=[("执行文件", ".exe")])

# 检测是否打开exe文件，防止desktop.ini被误修改
if not exe_file_path:
    print(f"未选中exe文件，程序退出")
    exit()

# 取出文件路径和名称
exe_file = os.path.basename(exe_file_path)
exe_dir = os.path.dirname(exe_file_path)

# 选择图标编号
#exe_icon_number = input("请输入图标编号（默认为0）：")
#if not exe_icon_number:  # 如果输入值为空，则设置为“0”
exe_icon_number = "0"
#elif exe_icon_number.isdigit():  # 如果输入值是数字，则保持原样
#    pass
#else:
#    print("错误：您输入的不是数字！")

# 打印exe文件路径和名称
print(f"已选择exe文件：")
print(f"文件名称：{exe_file} ")
print(f"图标编号：{exe_icon_number} ")
print(f"文件路径：{exe_dir}")

# desktop.ini文件名称
desktop_ini_file_name = "desktop.ini"
desktop_ini_file = os.path.join(exe_dir, desktop_ini_file_name)
print(f"正在生成配置文件信息：")
print(f"文件名称：{desktop_ini_file_name}")
print(f"文件目录：{exe_dir}")
print(f"文件名称和目录：{desktop_ini_file}")

# 生成并写入desktop.ini文件
print(f"正在生成并写入配置文件...")
with open(desktop_ini_file, 'w') as f:
    f.write(f"[.ShellClassInfo]\n")
    f.write(f"IconResource={exe_file},{exe_icon_number}\n")        #不带文件夹位置
    f.write(f"[ViewState]\n")
    f.write(f"Mode=\n")
    f.write(f"Vid=\n")
    f.write(f"FolderType=Generic\n")
    print(f"文件写入完成")

# 将desktop.ini文件设置为隐藏
print(f"正在将desktop.ini文件设置为隐藏")
os.system('attrib +h "{}"'.format(desktop_ini_file))

#退出
print(f"完成，程序退出")
exit()
