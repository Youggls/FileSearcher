from src.dbInterface.dbInterface import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #图标显示
    # path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'DVA.ico')
    # app.setWindowIcon(QIcon(QPixmap(path)))
    # path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'DVA.icns')
    # app.setWindowIcon(QIcon(QPixmap(path)))
    icon = QtGui.QIcon()
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'Dva.ico')
    icon.addPixmap(QtGui.QPixmap('Dva.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    ex = Ico()
    sys.exit(app.exec_())
