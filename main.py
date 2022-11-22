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

################################################## 面向过程 ##########################################################

# 1、创建一个应用程序对象
app = QApplication(sys.argv)


# 2、控件操作
# 创建控件，设置控件(大小、位置，样式...)，事件，信号的处理

# 2.1 创建控件
window = QWidget() # 窗口
# window = QPushButton() # 按钮
# window = QLabel() # 标签


# 2.2 设置控件

window.setWindowTitle('NewTitle')
window.resize(500, 500)
window.move(400, 200)


# 控件也可以作为一个容器(承载其他的控件)
label = QLabel(window)
label.setText('NewText')
label.move(200, 200)


# 2.3 展示控件
window.show()


# 3、应用程序的执行，进入到消息循环
sys.exit(app.exec_())





