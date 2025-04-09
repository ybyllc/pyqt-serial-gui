import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import QT_VERSION_STR
from PyQt6.QtCore import PYQT_VERSION_STR


if __name__ == '__main__':
    print(QT_VERSION_STR)
    print(PYQT_VERSION_STR)
    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    # 创建一个窗口对象
    window = QWidget()

    # 设置窗口的标题
    window.setWindowTitle('My First PyQt6 App')

    # 设置窗口的大小
    window.setGeometry(100, 100, 300, 200)

    main_layout = QVBoxLayout()
    main_layout.addWidget(QLabel("这是一个PyQt6应用程序"))

    # 将布局设置到窗口上
    window.setLayout(main_layout)

    # 显示窗口
    window.show()

    # 进入应用程序的主循环
    sys.exit(app.exec())