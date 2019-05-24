import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QFormLayout, QLabel, QTextEdit, QListView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from random import randint
from src.dbConnector.dbConnector import *

# #如果写了这句话并将执行的语句放到这个判断语句的后面，那么只有在程序本身被执行的时候才能运行这个判断语句下面的语句。否则程序被作为模块导入的时候就会执行。
# if __name__ == '__main__':
#     #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
#     app = QApplication(sys.argv)
#     #QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
#     w = QWidget()
#     #resize()方法调整窗口的大小。这离是250px宽150px高
#     w.resize(250, 150)
#     #move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#     w.move(300, 300)
#     #设置窗口的标题
#     w.setWindowTitle('FileSearcher')
#     #显示在屏幕上
#     w.show()
#
#     #系统exit()方法确保应用程序干净的退出
#     #的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
#     sys.exit(app.exec_())
# class Ico(QWidget):
class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('FileSearcher')

        self.search = QPushButton('Search', self)
        self.search.setGeometry(115, 150, 70, 30)
        self.search.setToolTip("<b>Click the button to search the file</b>")
        #self.search.clicked.connect(self.showResult)

        # self.text = QLineEdit("Enter the file's name here", self)
        # #将默认字符串全选，便于输入文件名
        # self.text.selectAll()
        # #让焦点置于文本栏
        # self.text.setFocus()
        # self.text.setGeometry(80, 50, 150, 30)

        self.formlayout = QFormLayout()
        searchLabel = QLabel("File Name")
        searchLineEdit = QLineEdit("")
        searchLineEdit.setFocus()
        searchLineEdit.setPlaceholderText("Enter the file's name here")
        searchLineEdit.setClearButtonEnabled(True)

        self.formlayout.addRow(searchLabel, searchLineEdit)
        self.setLayout(self.formlayout)

        # # 水平布局，添加一个拉伸因子和按钮
        # hbox_search = QHBoxLayout()
        # # addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。
        # hbox_search.addStretch(1)
        # hbox_search.addWidget(self.search)
        # hbox_search.addStretch(3)  # 增加伸缩量
        #
        # hbox_click = QHBoxLayout()
        # hbox_click.addStretch(1)
        # hbox_click.addWidget(self.text)
        # hbox_click.addStretch(3)  # 增加伸缩量
        #
        # # 水平布局放置在垂直布局中。垂直框中的拉伸因子将按钮的水平框推到窗口的底部。
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox_click)
        # vbox.addStretch(6)  # 增加伸缩量
        # vbox.addLayout(hbox_search)
        #
        # # 设置窗口的主要布局
        # self.setLayout(vbox)
        self.show()

    # def showResult(self, file_name):
    #     showLabel = QLabel("Location")
    #     showResult = QListView()
    #     resultList = launch.search_file(self, file_name)
    #     self.formlayout.addRow(showLabel, showResult)

    # def showMessage(self):
    #     #     address = self.text.text()
    #     #     #about弹出一个对话框
    #     #     QMessageBox.about(self, 'result', address)
    #     #     self.text.setFocus()
    #     #     # self.text.clear()

    def closeEvent(self, event):
        #QMessageBox.question, critical, warining, information 代表四个不同的图标
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    launch = dbConnector('youggls.top', 'youggls', 'lpylpy328', 'file_system')
    app = QApplication(sys.argv)
    #图标显示
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'dva_testIcon.ico')
    app.setWindowIcon(QIcon(path))
    #launch.walkpath();
    ex = Ico()
    sys.exit(app.exec_())
