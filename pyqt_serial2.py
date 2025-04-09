import sys
import importlib.util

# 自动安装所需的python库
def install_packages():
    required_packages = ['pyserial', 'PyQt6', 'pygments'] # 所需的python库
    
    for package in required_packages:
        try:
            # 检测库是否已安装
            importlib.util.find_spec(package)
        except ImportError:
            print(f"安装 {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"{package} 安装成功!")

install_packages()

import serial
import serial.tools.list_ports
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLabel, QComboBox, QPushButton, QTextEdit,QListWidget,QListWidgetItem
                            ,QLineEdit, QDialog, QMenu)
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

class ConfigDialog(QDialog):
    def __init__(self, parent=None, title="", command=""):
        super().__init__(parent)
        self.setWindowTitle("添加配置")
        self.setModal(True)
        
        layout = QVBoxLayout()
        
        # 添加类型选择
        self.type_combo = QComboBox()
        self.type_combo.addItems(["自定义按钮", "列表项"])
        layout.addWidget(QLabel("添加到:"))
        layout.addWidget(self.type_combo)
        
        # 标题输入
        self.title_input = QLineEdit()
        self.title_input.setText(title)
        self.title_input.setPlaceholderText("输入标题")
        layout.addWidget(QLabel("标题:"))
        layout.addWidget(self.title_input)
        
        # 命令输入
        self.command_input = QTextEdit()
        self.command_input.setText(command)
        self.command_input.setPlaceholderText("输入命令，每行一条")
        layout.addWidget(QLabel("命令:"))
        layout.addWidget(self.command_input)
        
        # 确定取消按钮
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("确定")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("取消")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)

class SerialReceiver(QWidget):
    def __init__(self):
        super().__init__()
        self.ser = None
        self.highlight_style = get_style_by_name('xcode')
        # 定义内置按钮配置
        self.builtin_configs = [
            {"text": "admin登录", "send": ["admin", "1234"]},
            {"text": "查看wan", "send": "tcapi show waninfo"},
            {"text": "查看GPON", "send": "ponmgr gpon get info"},
            {"text": "查看PON口", "send": "tcapi show xpon"}
        ]
        # 用户自定义按钮配置
        self.button_configs = []
        self.list_configs = LIST_CONFIG.copy()
        self.load_configs()  # 加载保存的配置
        self.initUI()

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
        
        # 自定义按钮区域
        grid_layout = QGridLayout()
        # 先添加内置按钮
        row = 0
        col = 0
        for config in self.builtin_configs:
            btn = QPushButton(config["text"])
            btn.clicked.connect(lambda checked, x=config["send"]: self.send_custom_data(x))
            btn.setStyleSheet(BUTTON_STYLE)
            grid_layout.addWidget(btn, row, col)
            col += 1
            if col >= 4:
                col = 0
                row += 1
                
        # 再添加自定义按钮
        for config in self.button_configs:
            btn = QPushButton(config["text"])
            btn.clicked.connect(lambda checked, x=config["send"]: self.send_custom_data(x))
            btn.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            btn.customContextMenuRequested.connect(lambda pos, b=btn, c=config: self.show_button_context_menu(pos, b, c))
            btn.setStyleSheet(BUTTON_STYLE)
            grid_layout.addWidget(btn, row, col)
            col += 1
            if col >= 4:
                col = 0
                row += 1

        # 右侧部分和列表布局
        right_layout = QVBoxLayout()  # 改为垂直布局

        # 列表布局
        list_widget = QListWidget()
        for item in self.list_configs:
            list_item = QListWidgetItem(item["text"])
            list_item.setData(Qt.ItemDataRole.UserRole, item["send"])
            list_widget.addItem(list_item)
        list_widget.itemClicked.connect(self.on_list_item_clicked)
        list_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        list_widget.customContextMenuRequested.connect(self.show_list_context_menu)
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
        list_widget.setMinimumSize(130, 0)

        # 添加列表和按钮布局
        right_layout.addWidget(list_widget)
        
        # 添加配置按钮放在最下面
        add_config_button = QPushButton("添加配置")
        add_config_button.setStyleSheet(BUTTON_STYLE)
        add_config_button.clicked.connect(self.show_config_dialog)
        right_layout.addWidget(add_config_button)

        # 主布局
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.addLayout(config_layout)
        left_layout.addWidget(self.text_edit)
        left_layout.addLayout(send_layout)
        left_layout.addLayout(grid_layout)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # 移除旧布局
        if self.layout():
            QWidget().setLayout(self.layout())
        
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
        # 如果当前有打开的串口，先关闭它
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

    def show_config_dialog(self, config=None, type_=None):
        """显示配置对话框"""
        dialog = ConfigDialog(self, 
                            title=config["text"] if config else "",
                            command=config["send"] if config else "")
        if config:
            dialog.type_combo.setCurrentText("自定义按钮" if type_=="button" else "列表项")
            dialog.type_combo.setEnabled(False)
            
        if dialog.exec() == QDialog.DialogCode.Accepted:
            title = dialog.title_input.text()
            command = dialog.command_input.toPlainText()
            # 处理多行命令
            command = command.split('\n') if '\n' in command else command.strip()
            new_config = {"text": title, "send": command}
            
            if config:  # 编辑现有配置
                if type_ == "button":
                    index = self.button_configs.index(config)
                    self.button_configs[index] = new_config
                else:
                    index = self.list_configs.index(config)
                    self.list_configs[index] = new_config
            else:  # 添加新配置
                if dialog.type_combo.currentText() == "自定义按钮":
                    self.button_configs.append(new_config)
                else:
                    self.list_configs.append(new_config)
            
            self.save_configs()  # 保存配置
            self.initUI()  # 刷新UI

    def show_button_context_menu(self, pos, button, config):
        """显示按钮右键菜单"""
        if config in self.builtin_configs:  # 内置按钮不显示右键菜单
            return
            
        menu = QMenu(self)
        edit_action = menu.addAction("编辑")
        delete_action = menu.addAction("删除")
        
        action = menu.exec(button.mapToGlobal(pos))
        if action == edit_action:
            self.show_config_dialog(config, "button")
        elif action == delete_action:
            self.button_configs.remove(config)
            self.save_configs()
            self.initUI()

    def show_list_context_menu(self, pos):
        """显示列表右键菜单"""
        item = self.findChild(QListWidget).itemAt(pos)
        if not item:
            return
            
        menu = QMenu(self)
        edit_action = menu.addAction("编辑")
        delete_action = menu.addAction("删除")
        
        config = next((x for x in self.list_configs if x["text"] == item.text()), None)
        if not config:
            return
            
        action = menu.exec(item.listWidget().mapToGlobal(pos))
        if action == edit_action:
            self.show_config_dialog(config, "list")
        elif action == delete_action:
            self.list_configs.remove(config)
            self.save_configs()
            self.initUI()

    def save_configs(self):
        """保存配置到文件"""
        import json
        try:
            with open('serial_configs.json', 'w', encoding='utf-8') as f:
                json.dump({
                    'buttons': self.button_configs,
                    'list': self.list_configs
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.text_edit.append(f"保存配置失败: {e}")

    def load_configs(self):
        """从文件加载配置"""
        import json
        try:
            with open('serial_configs.json', 'r', encoding='utf-8') as f:
                configs = json.load(f)
                self.button_configs = configs.get('buttons', [])
                self.list_configs = configs.get('list', LIST_CONFIG)
        except FileNotFoundError:
            # 如果配置文件不存在，使用默认配置
            self.button_configs = []
            self.list_configs = LIST_CONFIG.copy()
        except Exception as e:
            self.text_edit.append(f"加载配置失败: {e}")
            # 使用默认配置
            self.button_configs = []
            self.list_configs = LIST_CONFIG.copy()

    def refresh_ui(self):
        """刷新UI"""
        self.initUI()
        self.update()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    receiver = SerialReceiver()
    receiver.show()
    sys.exit(app.exec())
