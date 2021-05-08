"""
等式库子窗口的实现
Last edited date: 19. 10. 13
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QComboBox, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal


class LibraryWindow(QWidget):
    equationSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.equations = []
        self.message = QLabel(self)
        self.combobox = QComboBox(self)
        self.ok = QPushButton(self)
        self.init_ui()

    def init_ui(self):
        width = 1440
        height = 900
        x = width / 3
        y = height / 3
        w = width / 3
        h = height / 3
        self.setGeometry(x, y, w, h)
        self.setWindowTitle('Equation Library')
        self.setWindowIcon(QIcon('../images/lib.png'))

        # 设置提示文字
        self.message.move(x / 4, y / 6)
        self.message.resize(x / 2, y / 6)
        self.message.setText('Choose An Equation:')
        self.message.setFont(QFont('Roman Times', 16, QFont.Black))
        self.message.setAlignment(Qt.AlignCenter)

        # 设置下拉列表选择等式，加载表单内容
        self.combobox.move(x / 4, 3 * y / 8)
        self.combobox.resize(x / 2, y / 4)
        self.combobox.setFont(QFont('Roman Times', 18, QFont.DemiBold))
        self.load_equations()

        # 设置Ok按钮，按下后将选择的等式自动填入文本框中
        self.ok.move(3 * x / 8, 2 * y / 3)
        self.ok.resize(x / 4, y / 8)
        self.ok.setText('确认选择')
        self.ok.setFont(QFont('Roman Times', 15, QFont.Bold))
        self.ok.clicked.connect(self.sendLibequation)

    def load_equations(self):
        lib = open('../data/library.txt', 'r')
        self.equations = lib.readlines()
        for equation in self.equations:
            temp = ''
            rank = 1
            fac1 = ''
            fac2 = ''
            ans = ''
            op = ''
            for x in range(0, len(equation)):
                if equation[x] != ';':
                    temp = temp + equation[x]
                elif equation[x] == ';':
                    if rank == 1:
                        fac1 = temp
                        rank = rank + 1
                    elif rank == 2:
                        fac2 = temp
                        rank = rank + 1
                    elif rank == 3:
                        ans = temp
                        rank = rank + 1
                    else:
                        op = temp
                    temp = ''
            complete_equation = fac1 + op + fac2 + '=' + ans
            self.combobox.addItem(complete_equation)
        lib.close()

    # 向主窗口发送选中等式
    def sendLibequation(self):
        equation = self.combobox.currentText()
        self.equationSignal.emit(equation)
        self.close()
