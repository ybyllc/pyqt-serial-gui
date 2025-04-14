
# PyQt 串口调试助手

一个基于 PyQt6 的串口调试工具，支持命令快捷发送、语法高亮显示和配置管理。

### 环境安装（确保已安装python）
```bash
pip install PyQt6 pyserial pygments
```

### 运行程序
```bash
python pyqt_serial.py  # 运行上位机示例
python pyqt_serial2.py # 运行上位机示例2（完全体）
python pyqt_logo.py    # 查看qt自带logo
```

## 🖼️ 界面预览

 pyqt_serial（默认配置）
 
 ![样例1](https://github.com/user-attachments/assets/3a8379c2-3023-4ebf-be42-eb35bf4bb3c9) 
 
 pyqt_serial2：
 
 ![样例2](https://github.com/user-attachments/assets/2e7b23a2-27e9-4987-bb95-2db7c35966af)

## ✨ 功能特性

- **串口通信**：支持常用波特率设置
- **快捷命令**：快捷按钮+命令列表快速发送
- **语法高亮**：终端输出内容彩色显示
- **配置管理**：支持保存常用配置
- **自动登录**：一键发送登录凭证

## 🛠️ 开发指南

### 自定义命令
修改 `BUTTON_CONFIG` 和 `LIST_CONFIG` 默认按键配置：

```python
# 下侧按钮
BUTTON_CONFIG = [
    {"text": "admin登录", "send": ["admin", "1234"]},
    # 更多按钮...
]

# 列表按钮
LIST_CONFIG = [
    {"text": "查看系统信息", "send": "tcapi show sys"},
    # 更多按钮...
]
```

## 💰参考教程
- [pyqt菜鸟教程](https://www.w3ccoo.com/pyqt/)
- DeepSeek
- Copilot里的Claude 3.5

## 😃示例表情
🚀🎯✨🌟📂📄📁📝🛠🔧⚙️🔨🔗📚📖📦🚨⚠️❌🛑✅✔️🎉🏁🔍🐛🔎💡📊📈📉🧮👥🤝👨‍💻👩‍💻📅⏰⌛⏳🔒🔐🔑🛡️💬📢📣📩🌐📡🖥️💻🔗🔄⏫⏬🎨🖌️🎨🖼️📱📲📶📡📜📃📖📑🎮🕹️🎲🎰🌱🌍🌿🌳🎁🎊🎈📌📍🔖🗂️📏📐⚖️📋📷🎥📹📼⌨️🖱️🏷️✉️🔓🔩⛓️🧰🔦🕯️🔌🔋🧯🛢️💰💎⏲️🎀🎗️🏆🥇
