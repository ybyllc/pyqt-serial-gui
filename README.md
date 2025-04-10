
# PyQt 串口调试助手

一个基于 PyQt6 的串口调试工具，支持命令快捷发送、语法高亮显示和配置管理。

## ✨ 功能特性

- **串口通信**：支持常用波特率设置
- **快捷命令**：快捷按钮+命令列表快速发送
- **语法高亮**：终端输出内容彩色显示
- **配置管理**：支持保存常用配置
- **自动登录**：一键发送登录凭证

## 🚀 快速开始

### 环境安装
```bash
pip install PyQt6 pyserial pygments
```

### 运行程序
```bash
python pyqt_serial.py
```

## 🖼️ 界面预览

 ![样例1](https://github.com/user-attachments/assets/3a8379c2-3023-4ebf-be42-eb35bf4bb3c9) 
 样例1
 ![样例2](https://github.com/user-attachments/assets/78eb6fe1-7b55-4004-8539-a771ac52cfdb) 
 样例2

## 🛠️ 开发指南

### 自定义命令
修改 `BUTTON_CONFIG` 和 `LIST_CONFIG` 变量：

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
