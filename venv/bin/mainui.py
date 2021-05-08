"""
程序入口
"""
# Libs:
import sys
from PyQt5.QtWidgets import QApplication

# My classes:
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
