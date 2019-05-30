from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import * 
from src.dbConnector.dbConnector import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, sip, QtGui

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
        self.__read_config()

        self.launch = dbConnector(self.__data['db_host_name'], self.__data['db_usr_name'], self.__data['db_usr_pwd'], self.__data['db_schema'])
        temp = self.__data['Re_walk']
        if self.__data['Re_walk']:
            self.launch.init_database()
            self.launch.walk_path()
        self.setGeometry(325, 140, 800, 600)
        self.center()
        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowTitle('FileSearcher')

        self.label = QLabel(self)
        self.label.setFixedWidth(200)
        self.label.setFixedHeight(60)
        self.head = QPixmap('image.png').scaled(self.label.width(), self.label.height())
        self.label.setPixmap(self.head)
        #self.label.move(400, 200)
        # self.setWindowIcon(QIcon(QPixmap(path)))

        self.search = QPushButton('Search', self)
        #self.search.setGeometry(115, 150, 70, 30)
        self.search.setToolTip("<b>Click the button to search the file</b>")
        # self.search.setStyleSheet('''
        #     QPushButton{
        #         border:black;
        #         color:black;
        #         font-size:14px;
        #         height:40px;
        #         padding-left:10px;
        #         padding-right:10px;
        #         border-radius:11px;
        #     }
        #     QPushButton:hover{
        #         color:black;
        #         border:1px solid #F3F3F5;
        #         border-radius:11px;
        #         background:LightGray;
        #     }
        # ''')

        # self.text = QLineEdit("Enter the file's name here", self)
        # #将默认字符串全选，便于输入文件名
        # self.text.selectAll()
        # #让焦点置于文本栏
        # self.text.setFocus()
        # self.text.setGeometry(80, 50, 150, 30)

        self.formlayout = QFormLayout()
        self.searchLabel = QLabel("File Name:")
        self.searchLabel.setObjectName('searchLabel')
        self.searchLineEdit = QLineEdit(self)
        #self.searchLineEdit.setFocus()
        self.searchLineEdit.setPlaceholderText(" Enter the file's name here.")
        self.searchLineEdit.setClearButtonEnabled(True)
        self.searchLineEdit.setMinimumSize(300, 25)
        self.searchLineEdit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:11px;
                    padding:2px 4px;
            }''')

        self.searchLineEdit.returnPressed.connect(lambda:self.showResult(self.searchLineEdit.text()))
        self.count = 0

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
        self.hbox_search = QHBoxLayout()
        # addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。
        self.hbox_search.addStretch(1)
        self.hbox_search.addWidget(self.searchLabel)
        self.hbox_search.addStretch(1)
        self.hbox_search.addWidget(self.searchLineEdit)
        self.hbox_search.addStretch(1)
        self.hbox_search.addWidget(self.search)
        self.hbox_search.addStretch(1)  # 增加伸缩量

        self.result = QVBoxLayout()
        self.test = QHBoxLayout()
        self.test.addWidget(self.label)
        self.T = QVBoxLayout()

        self.result.addLayout(self.hbox_search)
        self.T.addLayout(self.test)
        self.T.setSpacing(10)
        self.T.addLayout(self.result)
        #self.result.addStretch(6)  # 增加伸缩量
        # self.result.addWidget(self.tableView)
        #self.setLayout(self.result)
        # hbox_click = QHBoxLayout()
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
        self.setLayout(self.T)
        self.show()
    def openDir(self, row):
        print(self.model.item(row, 1))

    def showResult(self, file_name):
        # if self.test:
        #     self.result.removeWidget(self.test)
        #     sip.delete(self.test)
        if file_name !="":
            #self.setLayout(self.result)
            QApplication.processEvents()
            #self.show()
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

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getName()
            #value = QStandardItem('%s' %temp_info.getName())
                value = QStandardItem(temp_info.getName())
                self.model.setItem(i, 0, value)
                self.model.item(i, 0)
                self.model.item(i, 0).setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Black))
            #self.tableWidget.setItem(i, 0, QTableWidgetItem(value))  # 设置i行0列的内容为Value
            # self.tableWidget.setColumnWidth(j, 80)  # 设置j列的宽度
            # self.tableWidget.setRowHeight(i, 50)  # 设置i行的高度

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getPath()
                value = QStandardItem(temp_info.getPath())
                self.model.setItem(i, 1, value)
                self.model.item(i, 1).setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Black))
            #self.tableWidget.setItem(i, 1, QTableWidgetItem(value))  # 设置i行1列的内容为Value

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getSize()
                if temp_info.getIsFolder():
                    value = QStandardItem("-")
                    self.model.setItem(i, 2, value)
                    self.model.item(i,2).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.model.item(i, 2).setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Black))
                else:
                    value = QStandardItem(temp_info.getSize())
                    self.model.setItem(i, 2, value)
                    self.model.item(i, 2).setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Black))

            #self.tableWidget.setItem(i, 2, QTableWidgetItem(value))  # 设置i行2列的内容为Value

            for i in range(self.num):
                temp_info = temp_list[i]
                self.launch.setFileFullPath(temp_info)
            #value = temp_info.getModifyTime()
                value = QStandardItem(temp_info.getModifyTime())
                self.model.setItem(i, 3, value)
                self.model.item(i, 3).setFont(QtGui.QFont("Monaco", 10, QtGui.QFont.Black))

            #self.tableWidget.setItem(i, 3, QTableWidgetItem(value))  # 设置i行3列的内容为Value
            if self.model.item(0, 1) == None:
                reply = QMessageBox.warning(self, '确认', '没有相关文件，需要再次搜索吗？', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.searchLineEdit.setText("")
                    if self.count != 0:
                        self.count = 1
                    else:
                        self.count = 0;
                else:
                    self.searchLineEdit.setText("")
                    if self.count != 0:
                        self.count = 1
                    else:
                        self.count = 0
                    self.close()
            elif self.count == 0:
                self.count = 3
            if self.count != 0:
                if self.count == 2 or self.count == 1:
                    self.result.removeWidget(self.tableView)
                    sip.delete(self.tableView)
                    self.result.removeWidget(self.showLine)
                    sip.delete(self.showLine)
                    self.result.removeWidget(self.showLabel)
                    sip.delete(self.showLabel)
                    # QApplication.processEvents()
                self.tableView = QTableView()
                self.tableView.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
                self.tableView.setMouseTracking(True)
                self.count += 1
                self.resultLabel = QLabel("Result")
                self.model.sort(0, QtCore.Qt.AscendingOrder)
                self.tableView.setModel(self.model)
                # self.index = self.model.index(self.tableView.currentIndex().row(), self.tableView.currentIndex().column())
                # data = self.model.data(index)
                # self.tableView.clicked.connect(self.getCurrentIndex(self.index))  # 将click信号与getCurrentIndex函数绑定

                # self.tableView.setToolTip("test")

                # print(self.model.item(row, 1))
                self.tableView.doubleClicked.connect(self.openDir)
                self.tableView.clicked.connect(self.toolTip)
                # self.tableView.setToolTip(self.cell_value)
                # temp_widget = self.tableView.indexWidget(list[0], list[1])
                # temp_widget
                # self.tableView.clicked.connect(self.openDir(row))
                # 水平方向标签拓展剩下的窗口部分，填满表格
                #     self.tableView.horizontalHeader().setStretchLastSection(True)
                self.tableView.horizontalHeader().resizeSection(1, 380)
                self.tableView.horizontalHeader().resizeSection(0, 160)
                # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
                # self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
                self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
                self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
                self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
                # self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
                # self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
                # 水平方向，表格大小拓展到适当的尺寸
                # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                # 设置只有行选中, 整行选中
                self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
                # self.tableView.resizeColumnsToContents()  # 设置列宽高按照内容自适应
                # self.tableView.resizeRowsToContents()  # 设置行宽和高按照内容自适应
                self.result.addWidget(self.tableView)

                self.showLabel = QLabel("Result")
                self.showLine = QLineEdit(self)
                self.showLine.setStyleSheet(
                    '''QLineEdit{
                            border:1px solid gray;
                            width:300px;
                            border-radius:11px;
                            padding:2px 4px;
                    }''')
                self.showLine.setReadOnly(True)
                self.showLine.setPlaceholderText(" Here is the clicked result.")
                self.showLine.setMinimumSize(650, 25)

                hbox_show = QHBoxLayout()
                # addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。
                hbox_show.addStretch(2)
                hbox_show.addWidget(self.showLabel)
                hbox_show.addStretch(1)
                hbox_show.addWidget(self.showLine)
                hbox_show.addStretch(2)
                self.result.addLayout(hbox_show)
                self.count = 2

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
    def openDir(self, signal):
        row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED
        #column = signal.column()  # RETRIEVES COLUMN OF CELL THAT WAS DOUBLE CLICKED
        #cell_dict = self.model.itemData(signal)  # RETURNS DICT VALUE OF SIGNAL
        #cell_value = cell_dict.get(0)  # RETRIEVE VALUE FROM DICT

        index = signal.sibling(row, 1)
        index_dict = self.model.itemData(index)
        path = index_dict.get(0)
        if self.__data['System_type'] == 'MacOS':
            os.system("open \"{}{}".format(path, '\"'))
        elif self.__data['System_type'] == 'Windows':
            os.system("explorer \"{}{}".format(path, '\"'))
        # print(
        #     'Row {}, Column {} clicked - value: {}\nColumn 1 contents: {}'.format(row, column, cell_value, index_value))

    # def openDir(self, signal):
    #     row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED
    #     column = signal.column()  # RETRIEVES COLUMN OF CELL THAT WAS DOUBLE CLICKED
    #     cell_dict = self.model.itemData(signal)  # RETURNS DICT VALUE OF SIGNAL
    #     cell_value = cell_dict.get(0)  # RETRIEVE VALUE FROM DICT
    #
    #     index = signal.sibling(row, 1)
    #     index_dict = self.model.itemData(index)
    #     index_value = index_dict.get(0)
    #     print(
    #         'Row {}, Column {} clicked - value: {}\nColumn 1 contents: {}'.format(row, column, cell_value, index_value))

    def toolTip(self, signal):
        row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED
        column = signal.column()  # RETRIEVES COLUMN OF CELL THAT WAS DOUBLE CLICKED
        cell_dict = self.model.itemData(signal)  # RETURNS DICT VALUE OF SIGNAL
        cell_value = cell_dict.get(0)  # RETRIEVE VALUE FROM DICT
        self.showLine.setText(cell_value)
        # list = []
        # list.append(row)
        # list.append(column)
        # list.append(cell_value)
        # return list

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        #QMessageBox.question, critical, warining, information 代表四个不同的图标
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __read_config(self):
        config_dir = './bin/config.json'
        with open(config_dir, encoding='utf8') as f:
            self.__data = json.load(f)