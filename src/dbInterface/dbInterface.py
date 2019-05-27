from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QFormLayout, QLabel, QTableView, QHeaderView, QAbstractItemView, QToolTip
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor
from PyQt5 import QtCore

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

        self.launch = dbConnector('127.0.0.1', 'Raymond777', 'Ytk981213', 'test')

        self.setGeometry(300, 300, 600, 440)
        self.setWindowTitle('FileSearcher')

        self.search = QPushButton('Search', self)
        #self.search.setGeometry(115, 150, 70, 30)
        self.search.setToolTip("<b>Click the button to search the file</b>")

        # self.text = QLineEdit("Enter the file's name here", self)
        # #将默认字符串全选，便于输入文件名
        # self.text.selectAll()
        # #让焦点置于文本栏
        # self.text.setFocus()
        # self.text.setGeometry(80, 50, 150, 30)

        self.formlayout = QFormLayout()
        self.searchLabel = QLabel("File Name:")
        self.searchLineEdit = QLineEdit(self)
        self.searchLineEdit.setFocus()
        self.searchLineEdit.setPlaceholderText("Enter the file's name here")
        self.searchLineEdit.setClearButtonEnabled(True)
        self.searchLineEdit.setMinimumSize(170, 25)
        self.count = -1

        self.search.clicked.connect(lambda:self.showResult(self.searchLineEdit.text()))

        # # # 水平布局，添加一个拉伸因子和按钮
        # # hbox_search = QHBoxLayout()
        # # # addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。
        # # hbox_search.addStretch(1)
        # # hbox_search.addWidget(self.searchLabel)
        # # hbox_search.addStretch(1)
        # # hbox_search.addWidget(self.searchLineEdit)
        # # hbox_search.addStretch(1)
        # # hbox_search.addWidget(self.search)
        # # hbox_search.addStretch(3)  # 增加伸缩量
        # # self.setLayout(hbox_search)
        # # if(self.searchLineEdit.text() != ""):
        # self.search.clicked.connect(self.showResult(self, self.searchLineEdit.text()))
        # self.formlayout.addRow(searchLabel, self.searchLineEdit)
        #
        # self.setLayout(self.formlayout)

        # 水平布局，添加一个拉伸因子和按钮
        hbox_search = QHBoxLayout()
        # addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。
        hbox_search.addStretch(1)
        hbox_search.addWidget(self.searchLabel)
        hbox_search.addStretch(1)
        hbox_search.addWidget(self.searchLineEdit)
        hbox_search.addStretch(1)
        hbox_search.addWidget(self.search)
        hbox_search.addStretch(1)  # 增加伸缩量


        self.result = QVBoxLayout()
        #self.result.addStretch(1)
        self.result.addLayout(hbox_search)
        #self.result.addStretch(6)  # 增加伸缩量
        # self.result.addWidget(self.tableView)
        self.setLayout(self.result)
        hbox_click = QHBoxLayout()
        # hbox_click.addStretch(1)
        # hbox_click.addWidget(self.resultLabel)
        # hbox_click.addStretch(1)
        # hbox_click.addLayout(result)
        # hbox_click.addStretch(3)  # 增加伸缩量

        #水平布局放置在垂直布局中。垂直框中的拉伸因子将按钮的水平框推到窗口的底部。
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox_search)
        # vbox.addStretch(6)  # 增加伸缩量
        # vbox.addLayout(hbox_click)

        #设置窗口的主要布局
        self.setLayout(self.result)
        self.show()

    def showResult(self, file_name):
        if file_name !="":
            self.count += 1
            if self.count != 0:
                self.result.removeWidget(self.tableView)
                sip.delete(self.tableView)
            self.resultLabel = QLabel("Result")
        # self.resultView = QListView()  # 创建ListView
        # self.resultModel = QStringListModel()  # 创建ListModel
        # temp_list = self.launch.search_file(file_name)
        # self.resultList = []
        # for i in temp_list:
        #     self.launch.setFileFullPath(i)
        #     self.resultList.append(i.getPath())
        # #self.resultList = self.launch.search_file("factory")  # 调用search_file返回result（List类型）
        # self.resultModel.setStringList(self.resultList)  # 将数据设置到Model
        # self.resultView.setModel(self.resultModel)  # 绑定View和Model
        # self.result.addWidget(self.resultView)

            self.num = len(self.launch.search_file(file_name))
        # 设置数据层次结构，num行4列
            self.model = QStandardItemModel(self.num, 4)
        # 设置水平方向四个头标签文本内容
            self.model.setHorizontalHeaderLabels(['Name', 'Path', 'Size', 'ModifyTime'])

        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(self.num)
            temp_list = self.launch.search_file(file_name)
            self.tableView = QTableView()
            self.tableView.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑®
            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getName()
            #value = QStandardItem('%s' %temp_info.getName())
                value = QStandardItem(temp_info.getName())
                self.model.setItem(i, 0, value)

            #self.tableWidget.setItem(i, 0, QTableWidgetItem(value))  # 设置i行0列的内容为Value
            # self.tableWidget.setColumnWidth(j, 80)  # 设置j列的宽度
            # self.tableWidget.setRowHeight(i, 50)  # 设置i行的高度

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getPath()
                value = QStandardItem(temp_info.getPath())
                self.model.setItem(i, 1, value)
            #self.tableWidget.setItem(i, 1, QTableWidgetItem(value))  # 设置i行1列的内容为Value

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getSize()
                if temp_info.getIsFolder():
                    value = QStandardItem("-")
                    self.model.setItem(i, 2, value)
                    self.model.item(i,2).setTextAlignment(QtCore.Qt.AlignCenter)
                else:
                    value = QStandardItem(temp_info.getSize())
                    self.model.setItem(i, 2, value)

            #self.tableWidget.setItem(i, 2, QTableWidgetItem(value))  # 设置i行2列的内容为Value

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getModifyTime()
                value = QStandardItem(temp_info.getModifyTime())
                self.model.setItem(i, 3, value)
            #self.tableWidget.setItem(i, 3, QTableWidgetItem(value))  # 设置i行3列的内容为Value

            self.tableView.setModel(self.model)

        # 水平方向标签拓展剩下的窗口部分，填满表格
        #self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置只有行选中, 整行选中
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        #self.tableView.resizeColumnsToContents()  # 设置列宽高按照内容自适应
        #self.tableView.resizeRowsToContents()  # 设置行宽和高按照内容自适应

            self.result.addWidget(self.tableView)

        # for i in range(self.num):
        #     temp_info = temp_list[i]
        #     self.launch.setFileFullPath(temp_info)
        #     value = temp_info.getName()
        #     self.tableWidget.setItem(i, 0, QTableWidgetItem(value))  # 设置i行0列的内容为Value
        #     # self.tableWidget.setColumnWidth(j, 80)  # 设置j列的宽度
        #     # self.tableWidget.setRowHeight(i, 50)  # 设置i行的高度
        #
        # for i in range(self.num):
        #     temp_info = temp_list[i]
        #     self.launch.setFileFullPath(temp_info)
        #     value = temp_info.getPath()
        #     self.tableWidget.setItem(i, 1, QTableWidgetItem(value))  # 设置i行1列的内容为Value
        #
        # for i in range(self.num):
        #     temp_info = temp_list[i]
        #     self.launch.setFileFullPath(temp_info)
        #     value = temp_info.getSize()
        #     self.tableWidget.setItem(i, 2, QTableWidgetItem(value))  # 设置i行2列的内容为Value
        #
        # for i in range(self.num):
        #     temp_info = temp_list[i]
        #     self.launch.setFileFullPath(temp_info)
        #     value = temp_info.getModifyTime()
        #     self.tableWidget.setItem(i, 3, QTableWidgetItem(value))  # 设置i行3列的内容为Value

        # self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.tableWidget.horizontalHeader().setVisible(True)  # 不隐藏水平表头
        # return self.resultView
        # self.resultView.clicked.connect(self.clickedlist)
        # layout = QVBoxLayout()
        # layout.addWidget(self.resultView)  # 将list view添加到layout
        # self.setLayout(layout)  # 将lay 添加到窗口
        # self.show()

    # def clickedlist(self, qModelIndex):
    #     QMessageBox.information(self, self.resultList[qModelIndex.row()])
    #     print(str(qModelIndex.row()))

    # def showMessage(self):
    #     #     address = self.text.text()
    #     #     #about弹出一个对话框
    #     #     QMessageBox.about(self, 'result', address)
    #     #     self.text.setFocus()
    #     #     # self.text.clear()

    #def openDir(self):


    def closeEvent(self, event):
        #QMessageBox.question, critical, warining, information 代表四个不同的图标
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
