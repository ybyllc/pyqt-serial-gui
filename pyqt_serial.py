# 自动安装所需的python库
import sys
import importlib.util
import subprocess
required_packages = ['PyQt6', 'pyserial', 'pygments'] # 需要安装的库列表
for package in required_packages:
    try:
        importlib.util.find_spec(package)
    except ImportError:
        print(f"未安装 {package}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package]) # pip安装库
        print(f"{package} 安装成功!")

# 导入库
import serial
import serial.tools.list_ports
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLabel, QComboBox, QPushButton, QTextEdit,QListWidget,QListWidgetItem
                            ,QLineEdit)
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt6 import QtGui


from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name
import subprocess
import sys

# 按钮样式
BUTTON_STYLE = """
    QPushButton {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 5px 15px;
        min-width: 60px;
        min-height: 25px;
    }
    QPushButton:hover {
        background-color: #e0e0e0;
    }
    QPushButton:pressed {
        background-color: #d0d0d0;
    }
"""

# 自定义按钮配置
# "标题"，"发送内容" 
BUTTON_CONFIG = [
    {"text": "admin登录", "send": ["admin", "1234"]},
    {"text": "su登录", "send": ["su admin", "admin"]},
    {"text": "3", "send": ""},
    {"text": "4", "send": ""}
]

# 列表配置
LIST_CONFIG = [
    {"text": "查看版本", "send": "cat /etc/deviceParaStatic.conf"},
    {"text": "查看CPU", "send": "cat /proc/cpuinfo"},
    {"text": "查看内存", "send": "free -m"},
    {"text": "查看磁盘", "send": "df -h"},
    {"text": "查看进程", "send": "top -n 1"},
    {"text": "查看网络", "send": "ifconfig"},
    {"text": "重启设备", "send": "reboot"},
    {"text": "查看日志", "send": "dmesg -c"},
    {"text": "Ping测试", "send": "ping 8.8.8.8 -c 4"}
    

]

# 串口调试器窗口
class SerialReceiver(QWidget):
    def __init__(self):
        super().__init__()
        self.ser = None
        # 语法高亮的主题
        self.highlight_style = get_style_by_name('xcode')  # 或者 'friendly', 'default', 'xcode', 'vs', 'tango', 'monokai' , 'pastie' 等，参考https://pygments.org/styles/
        self.initUI()



    # 刷新界面
    def initUI(self):
        # 创建布局
        main_layout = QVBoxLayout()
        config_layout = QHBoxLayout()
        
        # 连接状态指示灯
        self.status_light = QLabel()
        self.status_light.setFixedSize(10, 10)
        self.status_light.setStyleSheet("background-color: gray; border-radius: 5px;")
        config_layout.addWidget(self.status_light)

        # 串口选择下拉框
        self.port_combobox = QComboBox()
        self.refresh_ports()
        self.port_combobox.currentTextChanged.connect(self.on_port_changed)
        config_layout.addWidget(QLabel("串口:"))
        config_layout.addWidget(self.port_combobox)

        # 波特率选择下拉框
        self.baudrate_combobox = QComboBox()
        self.baudrate_combobox.addItems(['9600', '19200', '38400', '57600', '115200'])
        self.baudrate_combobox.setCurrentText('115200')
        config_layout.addWidget(QLabel("波特率:"))
        config_layout.addWidget(self.baudrate_combobox)

        # 刷新串口按钮
        self.refresh_button = QPushButton("刷新")
        self.refresh_button.setStyleSheet(BUTTON_STYLE)
        self.refresh_button.clicked.connect(self.refresh_ports)
        config_layout.addWidget(self.refresh_button)

        # 开关串口按钮
        self.open_close_button = QPushButton("打开")
        self.open_close_button.setStyleSheet(BUTTON_STYLE)
        self.open_close_button.clicked.connect(self.toggle_serial)
        config_layout.addWidget(self.open_close_button)

        # 串口文本显示框
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setMinimumSize(600, 400)  # 文本框 默认大小
        # 启用html富文本
        self.text_edit.setAcceptRichText(True)

        
        # 发送区域布局
        send_layout = QHBoxLayout()
        # 发送文本框
        self.send_text = QLineEdit()
        self.send_text.setPlaceholderText("输入要发送的内容")
        self.send_text.returnPressed.connect(self.send_data)  # 回车键 绑定"发送"事件
        send_button = QPushButton("发送")
        send_button.setStyleSheet(BUTTON_STYLE)
        send_button.clicked.connect(self.send_data)
        
        send_layout.addWidget(self.send_text)
        send_layout.addWidget(send_button)
        
        # 自定义按钮
        grid_layout = QGridLayout()
        for i, config in enumerate(BUTTON_CONFIG):
            btn = QPushButton(config["text"])  # 按钮的标题
            btn.clicked.connect(lambda checked, x=config["send"]: self.send_custom_data(x))
            btn.setStyleSheet(BUTTON_STYLE)
            grid_layout.addWidget(btn, i // 4, i % 4)  # 每行4个按钮
            
        # 添加布局
        # 主布局改为水平布局
        main_layout = QHBoxLayout()
        
        # 左侧布局（原来的垂直布局）
        left_layout = QVBoxLayout()
        left_layout.addLayout(config_layout)
        left_layout.addWidget(self.text_edit)
        left_layout.addLayout(send_layout)
        left_layout.addLayout(grid_layout)

    
        # 右侧部分
        right_layout = QHBoxLayout()

        # 列表布局
        list_widget = QListWidget()
        for item in LIST_CONFIG:
            list_item = QListWidgetItem(item["text"])
            list_item.setData(Qt.ItemDataRole.UserRole, item["send"])
            list_widget.addItem(list_item)
        list_widget.itemClicked.connect(self.on_list_item_clicked)
        list_widget.setStyleSheet("""
            QListWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:hover {
                background-color: #e0e0e0;
            }
        """)
        list_widget.setMinimumSize(130, 0)  # 列表 默认大小

        # 将列表添加到右侧布局
        right_layout.addWidget(list_widget)

        # 将左右布局添加到主布局
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('串口调试助手')
        self.setGeometry(100, 100, 700, 500) # 默认窗口大小

    def refresh_ports(self):
        """串口刷新"""
        self.port_combobox.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.port_combobox.addItem(port.device)
    
    def on_port_changed(self, port):
        """处理串口选择变更"""
        # 如果当前有打开的串口，先关闭
        if self.ser and self.ser.is_open:
            try:
                self.ser.close()
                self.ser = None
                self.open_close_button.setText("打开")
                self.status_light.setStyleSheet("background-color: gray; border-radius: 5px;")
                self.text_edit.append("串口已关闭")
            except Exception as e:
                self.text_edit.append(f"关闭串口时出错: {e}")
                self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")
            finally:
                self.ser = None

    def toggle_serial(self):
        """开关串口"""
        if self.ser is None or not self.ser.is_open:
            try:
                port = self.port_combobox.currentText()
                baudrate = int(self.baudrate_combobox.currentText())
                self.ser = serial.Serial(port, baudrate=baudrate, timeout=1)
                self.open_close_button.setText("关闭")
                self.status_light.setStyleSheet("background-color: green; border-radius: 5px;")
                self.receive_data()
            except serial.SerialException as e:
                self.text_edit.append(f"打开失败,可能已被其他应用占用: {e}")
                self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")
        else:
            self.ser.close()
            self.open_close_button.setText("打开")
            self.status_light.setStyleSheet("background-color: gray; border-radius: 5px;")

    def receive_data(self):
        """显示收到的数据"""
        while self.ser and self.ser.is_open:
            try:
                if self.ser.in_waiting:
                    data = self.ser.readline().decode('utf-8').strip()
                    # 字体格式：应用语法高亮
                    highlighted_data = self.highlight_text(data)
                    self.text_edit.append(highlighted_data)
                    # 滚动到底部
                    cursor = self.text_edit.textCursor()
                    cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                    self.text_edit.setTextCursor(cursor)
                QApplication.processEvents()
            except Exception as e:
                error_html = f'<span style="color:red">接收数据出错: {e}</span>'
                self.text_edit.append(error_html)
                self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")
                break

    def send_data(self):
        """发送数据到串口"""
        if self.ser and self.ser.is_open:
            try:
                data = (self.send_text.text() + '\n').encode('utf-8')
                self.ser.write(data)

                # 字体风格：使用HTML格式设置绿色文本
                self.text_edit.append(f'<span style="color:green">发送: {self.send_text.text()}</span>')
                self.send_text.clear()
            except Exception as e:
                self.text_edit.append(f"发送失败: {e}")
                self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")
        else:
            self.text_edit.append("错误: 串口未连接")
            self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")

    def closeEvent(self, event):
        """重写关闭事件，确保关闭串口"""
        if self.ser and self.ser.is_open:
            self.ser.close()
        event.accept()

    def send_custom_data(self, data):
        """发送自定义数据到串口，支持多行数据"""
        if not self.ser or not self.ser.is_open:
            self.text_edit.append("错误: 串口未连接")
            self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")
            return

        try:
            if isinstance(data, list):
                # 多行时间隔100ms发送
                for i, line in enumerate(data):
                    QTimer.singleShot(i * 100, lambda l=line: 
                        self.ser.write(f"{l}\n".encode('utf-8')) if self.ser and self.ser.is_open else None)
                    QTimer.singleShot(i * 100, lambda l=line:
                        self.text_edit.append(f'<span style="color:green">发送: {l}</span>'))
            else:
                # 单行数据，直接发送
                self.ser.write(f"{data}\n".encode('utf-8'))
                self.text_edit.append(f'<span style="color:green">发送: {data}</span>')
        except Exception as e:
            self.text_edit.append(f"发送失败: {e}")
            self.status_light.setStyleSheet("background-color: red; border-radius: 5px;")

    def on_list_item_clicked(self, item):
        """处理列表项点击事件"""
        send_data = item.data(Qt.ItemDataRole.UserRole)
        self.send_custom_data(send_data)



    def highlight_text(self, text):
        """使用pygments高亮文本"""
        try:
            # 使用bash语法高亮
            lexer = get_lexer_by_name("bash")
            # 使用HTML格式输出
            formatter = HtmlFormatter(style=self.highlight_style, noclasses=True)
            return highlight(text, lexer, formatter)
        except Exception as e:
            print(f"高亮失败: {e}")
            return text  # 返回原始文本
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    receiver = SerialReceiver()
    receiver.show()
    sys.exit(app.exec())
