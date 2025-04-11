# 自动安装所需的python库
import sys
import importlib.util
import subprocess
required_packages = ['PyQt6'] # 需要安装的库列表
for package in required_packages:
    try:
        importlib.util.find_spec(package)
    except ImportError:
        print(f"未安装 {package}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package]) # pip安装库
        print(f"{package} 安装成功!")


# 导入库
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# QtWidgets用来创建界面


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 创建一个窗口对象
    window = QWidget()

    # 设置窗口的标题
    window.setWindowTitle('My First PyQt6 App')
    # 设置窗口的大小
    window.setGeometry(100, 100, 300, 200)


    # 添加元素的布局
    main_layout = QVBoxLayout()  # 垂直排列布局
    label = QLabel("这是一个PyQt6应用程序")
    main_layout.addWidget(label)

    # 将布局设置到窗口上
    window.setLayout(main_layout)


    # 显示窗口
    window.show()

    # 进入应用程序的主循环, 保持窗口存活
    sys.exit(app.exec())