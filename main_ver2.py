# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt, QObject, QEvent
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QFormLayout, QGridLayout
from PyQt5.QtWidgets import QComboBox, QLabel, QLineEdit, QPushButton, QTextEdit, QTextBrowser, QMenu, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QCheckBox, QFrame, QAbstractScrollArea, QLayout, QBoxLayout, QFormLayout, QGridLayout, QStackedLayout
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

################################################## 控件类对象 ##########################################################
# 2.2 设置控件

window.setWindowTitle('NewTitle')
window.resize(500, 500)
window.move(400, 200)


# 控件也可以作为一个容器(承载其他的控件)
# 标签控件
label = QLabel(window)
label.setText('NewText')
label.move(200, 200)


# 按钮
btn = QPushButton('button', window)
btn.setText('按钮')
# btn.setIcon()
# btn.setIconSize()
# btn.pressed.connect()
# btn.clicked.connect()

tb = Qt.ToolButtonStyle()
menu = QMenu(btn)

rb = QRadioButton('01', window)
rb.move(150, 200)
# rb.toggled.connect()
rb_02 = QRadioButton('02', window)
rb_02.move(150, 100)
# rb_02.toggled.connect()

# 按钮组
group = QButtonGroup(window)
group.addButton(rb)
group.addButton(rb_02)
group.checkedButton() # 获取按钮
# group.removeButton() # 移除按钮
# group.setId()
# group.setExclusive()
# signal
# group.buttonToggled.connect() 
# group.buttonPressed.connect()
# group.buttonClicked.conncet()
# group.buttonReleased.connect()

# 选择按钮
cb = QCheckBox('name', window)
# cb.setIcon()
# cb.setIconSize()
# cb.setTristate(True)
# cb.setChecked(True)
# cb.setCheckable()
# cb.checkState(Qt.Checked)
# cb.toggled.connect()


# 输入控件
# 单行文本控制器
line = QLineEdit('name', window)
# line.setText('')
# line.insert() # 光标处的内容
# line.text() # 输入内容
# line.displayText() # 用户看到的内容
line_2 = QLineEdit('name2', window)

# 例子
def copy_text():
    # 1、获取文本框内容
    content = line.text()
    # 2、把上面的内容设置到文本框2里面
    line_2.setText(content)
    # line_2.insert(content)
    line_2.setText('') # 清空
    
btn.clicked.connect(copy_text)

line.setEchoMode()


# 边框样式
frame = QFrame(window)
frame.resize(100, 100)
frame.move(100, 100)

# 滚动
# scroll = QAbstractScrollArea(Window)


# 文本  
text = QTextEdit(window)


# 组合框
combox = QComboBox(window)
# combox.addAction()
combox.addItem('123')
combox.addItems('1', '2', '3')
combox.insertItem()
combox.setItem()
combox.removeItem()


# 布局管理器
# 1、创建布局对象
# 2、设置布局对象参数
# 3、设置给需要布局了控件的父控件
# 4、将布局控件内部的子控件添加到布局管理器中，自动进行布局
layout = QLayout(window) # 基类
box = QBoxLayout(window) # 基类
form = QFormLayout(window)
grid = QGridLayout(window)
stack = QStackedLayout(window)






################################################## 控件类对象 ##########################################################

# 2.3 展示控件
window.show()


# 3、应用程序的执行，进入到消息循环
sys.exit(app.exec_())





