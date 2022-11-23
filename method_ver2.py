# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt, QObject, QEvent
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QFormLayout, QGridLayout
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser
from PyQt5.QtWidgets import QCheckBox, QFrame, QAbstractScrollArea, QLayout, QBoxLayout, QFormLayout, QGridLayout, QStackedLayout
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

        # 添加三个控件
        self.line_01 = QLineEdit(self)
        self.line_02 = QLineEdit(self)
        self.line_02.setEchoMode()
        self.btn = QPushButton(self)
        self.btn.setText('text')

        # 添加文本框提示
        self.line_01.setPlaceholderText("path")
        self.line_02.setPlaceholderText("path")

        self.btn.clicked.connect(self.func)

        # 添加布局管理器
        # 1、创建一个布局管理器对象
        layout = QBoxLayout()
        # 2、直接把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)
        # 3、把需要布局的子控件添加到布局管理器中
        layout.addWidget(label)
        layout.addWidget()

        layout.setSpacing(10) # 间距



    def func(self):
        # 输入框内容
        content = self.line_01.text()
        content_02 = self.line_02.text()

        if content != None:
            pass

