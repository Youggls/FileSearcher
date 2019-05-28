import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from src.dbConnector.dbConnector import *
from src.dbInterface.dbInterface import *

if __name__ == '__main__':
    launch = dbConnector('127.0.0.1', 'Raymond777', 'Ytk981213', 'test')
    launch.walk_path()
    app = QApplication(sys.argv)
    #图标显示
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'dva_testIcon.ico')
    app.setWindowIcon(QIcon(path))
    #ex = Ico()
    sys.exit(app.exec_())
