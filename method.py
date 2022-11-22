# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt, QObject, QEvent
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QFormLayout, QGridLayout
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser
# 使用调色板等
from PyQt5.QtGui import QIcon, QDrag, QColor
# 系统操作
import sys


############################################### 面向对象 #############################################################

# 继承新类
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NewTitle')
        self.resize(500, 500)
        self.move(400, 200)
        self.setup_ui()

    def setup_ui(self):
        # 控件也可以作为一个容器(承载其他的控件)
        label = QLabel(self)
        label.setText('NewText')
        label.move(200, 200)