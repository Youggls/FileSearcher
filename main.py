import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication
from src.dbConnector.dbConnector import *

a = dbConnector('youggls.top', 'youggls', 'lpylpy328', 'file_system')

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

class Ico(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()

   def initUI(self):

       self.setGeometry(300, 300, 300, 220)
       self.setWindowTitle('FileSearcher')

       qbtn = QPushButton('exit', self)
       qbtn.clicked.connect(QCoreApplication.instance().quit)
       qbtn.resize(70,30)
       qbtn.move(50, 50)

       self.show()

if __name__ == '__main__':

   app = QApplication(sys.argv)
   #图标显示
   path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'dva_testIcon.ico')
   app.setWindowIcon(QIcon(QPixmap(path)))

   ex = Ico()
   sys.exit(app.exec_())
