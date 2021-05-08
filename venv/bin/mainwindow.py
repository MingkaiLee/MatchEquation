# Create the Mainwindow
"""
主界面类，利用PyQt5完成
Last edited: 19. 10. 18
"""
import sys
import copy
from PyQt5.QtWidgets import (QMainWindow,
                             QToolBar,
                             QLabel,
                             QTextBrowser,
                             QLCDNumber,
                             QPushButton,
                             QMessageBox,
                             QAction,
                             qApp,
                             QWidget,
                             QApplication)
from PyQt5.QtGui import QIcon, QFont, QBrush, QPalette, QPixmap
from PyQt5.QtCore import QRect, pyqtSlot, Qt, pyqtSignal, QCoreApplication
from PyQt5.Qt import QLineEdit, QPalette

from Funclab import *
from Funclab_pro import *
from matchequation import MatchEquation

from libwindow import LibraryWindow
from infowindow import HelpWindow


class MainWindow(QMainWindow):
    # 求解完成信号
    done1Signal = pyqtSignal(str)
    done2Signal = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        # 移动两根火柴和移动一根火柴的按钮
        self.twobtn = QPushButton(self)
        self.onebtn = QPushButton(self)
        # 文本输入框以及提示字符，接受输入的等式
        self.tip1 = QLabel(self)
        self.facin1 = QLineEdit(self)
        self.opin = QLineEdit(self)
        self.tipop = QLabel(self)
        self.facin2 = QLineEdit(self)
        self.tip2 = QLabel(self)
        self.ansin = QLineEdit(self)
        self.equaop = QLabel(self)
        self.tipans = QLabel(self)
        self.toolbar = QToolBar()
        # 数码管显示，由于算符无法使用故使用QLabel代替
        self.lcd1 = QLCDNumber(self)
        self.lcd2 = QLCDNumber(self)
        self.lcd3 = QLCDNumber(self)
        self.lcd1.setDigitCount(2)
        self.lcd2.setDigitCount(2)
        self.lcd3.setDigitCount(2)
        self.lcd1.setMode(QLCDNumber.Dec)
        self.lcd2.setMode(QLCDNumber.Dec)
        self.lcd3.setMode(QLCDNumber.Dec)
        self.lcd1.setSegmentStyle(QLCDNumber.Flat)
        self.lcd1.setStyleSheet("border: 2px solid black; color: green; background: silver;")
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd2.setStyleSheet("border: 2px solid black; color: green; background: silver;")
        self.lcd3.setSegmentStyle(QLCDNumber.Flat)
        self.lcd3.setStyleSheet("border: 2px solid black; color: green; background: silver;")
        self.lcdop = QLabel(self)
        self.lcdeq = QLabel(self)
        # 上翻，下翻展示
        self.last = QPushButton(self)
        self.next = QPushButton(self)
        # 提示信息，提示是否有解，有解还将显示难度系数
        self.tips = QTextBrowser(self)
        # 程序名及版本号
        self.version = 'SmartMatch_v1.1.18'
        # 帮助子窗口
        self.help = HelpWindow()
        # 等式库子窗口
        self.lib = LibraryWindow()
        # 移动一根所有变化的状态空间
        self.closed1 = []
        # 移动两根所有变化的状态空间
        self.closed2 = []
        # 等式列表
        self.showlist = []
        # 是否可保存
        self.allowed = 0
        # 等式列表中当前的等式序号
        self.now = 0
        # 输入为等式的标记
        self.initeq = 0
        # 状态栏
        self.status = self.statusBar()
        self.init_ui()

    def init_ui(self):
        # 两个列表存放搜索结果

        # 默认使用了我的桌面分辨率大小的标准尺寸
        width = 1440
        height = 900
        x = width / 4
        y = height / 4
        w = width / 2
        h = height / 2

        # 创建全屏主窗口
        self.setGeometry(x, y, w, h)
        self.setWindowTitle(self.version)
        self.setWindowIcon(QIcon("../images/icon.jpg"))

        #设置主窗口背景
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('../images/background.png')))
        self.setPalette(palette)

        # 进入后的提示信息
        self.status.showMessage("欢迎")

        # 创建工具栏
        self.addToolBar(self.toolbar)

        self.facin1.move(w / 6, h / 4)
        self.facin1.resize(w / 12, h / 12)
        self.facin1.setMaxLength(2)
        self.facin1.setFont(QFont('Roman times', 20, QFont.DemiBold))
        self.facin1.setAlignment(Qt.AlignCenter)

        self.tip1.move(w / 6, h / 6)
        self.tip1.resize(w / 12, h / 12)
        self.tip1.setText('Number1:')
        self.tip1.setFont(QFont('Roman times', 12, QFont.DemiBold))
        self.tip1.setAlignment(Qt.AlignCenter)

        self.opin.move(w/3, h / 4)
        self.opin.resize(w / 24, h / 12)
        self.opin.setMaxLength(1)
        self.opin.setFont(QFont('Roman times', 20, QFont.DemiBold))
        self.opin.setAlignment(Qt.AlignCenter)

        self.tipop.move(5*w/16, h / 6)
        self.tipop.resize(w / 12, h / 12)
        self.tipop.setText('Operator:')
        self.tipop.setFont(QFont('Roman times', 12, QFont.DemiBold))
        self.tipop.setAlignment(Qt.AlignCenter)

        self.facin2.move(11*w/24, h / 4)
        self.facin2.resize(w / 12, h / 12)
        self.facin2.setMaxLength(2)
        self.facin2.setFont(QFont('Roman times', 20, QFont.DemiBold))
        self.facin2.setAlignment(Qt.AlignCenter)

        self.tip2.move(11*w/24, h / 6)
        self.tip2.resize(w / 12, h / 12)
        self.tip2.setText('Number2:')
        self.tip2.setFont(QFont('Roman times', 12, QFont.DemiBold))
        self.tip2.setAlignment(Qt.AlignCenter)

        self.equaop.move(5*w/8, h / 4)
        self.equaop.resize(w / 24, h / 12)
        self.equaop.setText('=')
        self.equaop.setFont(QFont('Roman time2', 20, QFont.DemiBold))
        self.equaop.setAlignment(Qt.AlignCenter)

        self.ansin.move(3*w/4, h / 4)
        self.ansin.resize(w / 12, h / 12)
        self.ansin.setMaxLength(2)
        self.ansin.setFont(QFont('Roman times', 20, QFont.DemiBold))
        self.ansin.setAlignment(Qt.AlignCenter)

        self.tipans.move(3*w/4, h / 6)
        self.tipans.resize(w / 12, h / 12)
        self.tipans.setText('Answer:')
        self.tipans.setFont(QFont('Roman times', 12, QFont.DemiBold))
        self.tipans.setAlignment(Qt.AlignCenter)

        # 移动一根火柴按钮
        self.onebtn.move(w / 3, 3 * h / 8)
        self.onebtn.resize(w / 3, h / 16)
        self.onebtn.setText('搜索只移动一根火柴的结果')
        self.onebtn.setStatusTip('开始搜索只移动一根火柴的所有结果')
        self.onebtn.clicked.connect(lambda: self.startSearch(1))

        # 移动两根火柴按钮
        self.twobtn.move(w / 3, 7 * h / 16)
        self.twobtn.resize(w / 3, h / 16)
        self.twobtn.setText('搜索只移动两根火柴的结果')
        self.twobtn.setStatusTip('开始搜索只移动两根火柴的所有结果')
        self.twobtn.clicked.connect(lambda: self.startSearch(2))

        # LCD显示摆放
        self.lcd1.move(w/6, 7*h/12)
        self.lcd1.resize(w/12, h/8)
        self.lcd2.move(11*w/24, 7*h/12)
        self.lcd2.resize(w/12, h/8)
        self.lcd3.move(3*w/4, 7*h/12)
        self.lcd3.resize(w/12, h/8)
        self.lcdeq.move(5*w/8, 7*h/12)
        self.lcdeq.resize(w/24, h/8)
        self.lcdeq.setText('=')
        self.lcdeq.setStyleSheet("font:30pt;border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);"
                                 "background:silver;color: green;")
        self.lcdeq.setAlignment(Qt.AlignCenter)
        self.lcdop.move(w/3, 7*h/12)
        self.lcdop.resize(w/24, h/8)
        self.lcdop.setStyleSheet("font:30pt;border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);"
                                 "background:silver;color: green;")
        self.lcdop.setAlignment(Qt.AlignCenter)

        # 状态信息显示
        self.tips.move(w/6, 3*h/4)
        self.tips.resize(2*w/3, h/10)
        self.tips.setStyleSheet("background:white;font:12pt")

        # 上翻下翻
        self.last.move(w/4, 17*h/20)
        self.last.resize(w/8, h/18)
        self.last.setText('上一个')
        self.last.setStatusTip('查看上一个可行解')
        self.last.clicked.connect(lambda: self.changeShow(1))
        self.next.move(5*w/8, 17*h/20)
        self.next.resize(w/8, h/18)
        self.next.setText('下一个')
        self.next.setStatusTip('查看下一个可行解')
        self.next.clicked.connect(lambda: self.changeShow(2))

        # 退出动作
        exitAct = QAction(QIcon('../images/exit.png'), '&Exit', self)
        # mac系统下的快捷键
        exitAct.setShortcut('command+Q')
        exitAct.setStatusTip('退出')
        exitAct.setToolTip('快捷键:command+Q')
        exitAct.triggered.connect(lambda: self.sureClose())

        # 移动一根火柴动作
        start1Act = QAction(QIcon('../images/start1.png'), '&Start1', self)
        start1Act.setShortcut('command+W')
        start1Act.setToolTip('快捷键:command+W')
        start1Act.setStatusTip('开始搜索只移动一根火柴的所有结果')
        start1Act.triggered.connect(lambda: self.startSearch(1))

        # 移动两根火柴动作
        start2Act = QAction(QIcon('../images/start2.png'), '&Start2', self)
        start2Act.setShortcut('command+E')
        start2Act.setToolTip('快捷键:command+E')
        start2Act.setStatusTip('开始搜索只移动两根火柴的所有结果')
        start2Act.triggered.connect(lambda: self.startSearch(2))

        # 从库中选择等式动作
        openLib = QAction(QIcon('../images/lib.png'), '&Library', self)
        openLib.setShortcut('command+R')
        openLib.setToolTip('快捷键:command+R')
        openLib.setStatusTip('打开已有等式库')
        openLib.triggered.connect(lambda: self.openLibrary())

        # 打开帮助和信息界面
        openHelp = QAction(QIcon('../images/help.png'), '&Help', self)
        openHelp.setShortcut('command+A')
        openHelp.setToolTip('快捷键:command+A')
        openHelp.setStatusTip('打开帮助界面')
        openHelp.triggered.connect(lambda: self.openHelp())

        # 保存可解等式动作
        saveEquation = QAction(QIcon('../images/save.png'), '&Save', self)
        saveEquation.setShortcut('command+S')
        saveEquation.setToolTip('快捷键:command+S')
        saveEquation.setShortcut('保存可解的等式')
        saveEquation.setStatusTip('保存当前的可解等式')
        saveEquation.triggered.connect(lambda: self.saveEquation())

        # 清除输入和工作区动作
        clearAll = QAction(QIcon('../images/clear.png'), 'Clear', self)
        clearAll.setShortcut('command+C')
        clearAll.setToolTip('快捷键:command+C')
        clearAll.setShortcut('清除输入及变量')
        clearAll.setStatusTip('清除输入及变量')
        clearAll.triggered.connect(lambda: self.clearAction())

        self.toolbar.addAction(start1Act)
        self.toolbar.addAction(start2Act)
        self.toolbar.addAction(clearAll)
        self.toolbar.addAction(openLib)
        self.toolbar.addAction(saveEquation)
        self.toolbar.addAction(openHelp)
        self.toolbar.addAction(exitAct)

        # 信号和槽连接
        self.done1Signal.connect(self.getDone1)
        self.done2Signal.connect(self.getDone2)

    # 主功能函数，移动一根或两根全搜索
    def startSearch(self, num):
        self.varClear()
        self.lcdClear()
        common = '请确保{}方格内输入{}。'
        if self.facin1.text() == '':
            warn = QMessageBox.about(self, '错误提示', common.format('Number1', '数字'))
            self.status.showMessage('空输入错误')
        elif self.facin2.text() == '':
            warn = QMessageBox.about(self, '错误提示', common.format('Number2', '数字'))
            self.status.showMessage('空输入错误')
        elif self.ansin.text() == '':
            warn = QMessageBox.about(self, '错误提示', common.format('Answer', '数字'))
            self.status.showMessage('空输入错误')
        elif self.opin.text() == '':
            warn = QMessageBox.about(self, '错误提示', common.format('Operator', '"+", "-"或"*"号'))
            self.status.showMessage('空输入错误')
        else:
            try:
                fac1 = str(self.facin1.text())
                for x in range(0, len(fac1)):
                    int(fac1[x])
                fac2 = str(self.facin2.text())
                for x in range(0, len(fac2)):
                    int(fac2[x])
                ans = str(self.ansin.text())
                for x in range(0, len(ans)):
                    int(ans[x])
            except ValueError:
                warn = QMessageBox.about(self, '类型错误', common.format('Number1, Nubmber2和Answer', '仅为阿拉伯数字'))
                self.status.showMessage('输入类型错误')
            else:
                fac1 = str(self.facin1.text())
                fac2 = str(self.facin2.text())
                op = str(self.opin.text())
                ans = str(self.ansin.text())
                if not(op == '+' or op == '-' or op == '*'):
                    warn = QMessageBox.about(self, '类型错误', common.format('Operator', '"+", "-"或"*"号'))
                    self.status.showMessage('输入类型错误')
                else:
                    base = MatchEquation(fac1, fac2, ans, op)
                    if num == 1:
                        self.closed1 = onePerop(base)
                        self.done1Signal.emit('Done')
                    elif num == 2:
                        self.closed2 = twoPerop(base)
                        self.done2Signal.emit('Done')
                    self.status.showMessage('完成')

    # 打开等式库子窗口，接收选择等式
    def openLibrary(self):
        self.lib.show()
        self.lib.equationSignal.connect(self.getLibequation)

    # 打开帮助界面子窗口
    def openHelp(self):
        self.help.show()

    # 接收等式库子窗口的信号
    def getLibequation(self, connect):
        temp = ''
        for x in range(0, len(connect)):
            if connect[x] == '+' or connect[x] == '-' or connect[x] == '*':
                self.opin.setText(connect[x])
                self.facin1.setText(temp)
                temp = ''
            elif connect[x] == '=':
                self.facin2.setText(temp)
                temp = ''
            else:
                temp = temp + connect[x]
        self.ansin.setText(temp)

    # 接受对移动一根火柴问题求解完成的信号
    def getDone1(self, connect):
        ansNum = 0
        for equation in self.closed1:
            if equation.equal == True:
                ansNum = ansNum + 1
                self.showlist.append(equation)
        if ansNum == 0 or (ansNum == 1 and self.closed1[0] == self.showlist[0]):
            self.tips.setText('很抱歉，该等式通过移动一根火柴无解。')
        elif ansNum > 1 and self.closed1[0] == self.showlist[0]:
            self.allowed = 1
            self.initeq = 1
            self.now = self.now + 1
            info1 = '该问题是将等式变为新的等式问题, 有{}种新等式'
            info2 = '该问题的难度系数为{:.2f}'
            self.tips.setText(info1.format(ansNum - 1) + '<br>' + info2.format(len(self.closed1) / (ansNum - 1)))
            self.lcd1.display(self.showlist[self.now].factor1.tostr())
            self.lcd2.display(self.showlist[self.now].factor2.tostr())
            self.lcd3.display(self.showlist[self.now].answer.tostr())
            self.lcdop.setText(self.showlist[self.now].operator.tostr())
        else:
            self.allowed = 1
            info1 = '通过移动一根火柴使等式成立，有{}种可行的解法'
            info2 = '该问题的难度系数为{:.2f}'
            self.tips.setText(info1.format(ansNum)+'<br>'+info2.format(len(self.closed1) / ansNum))
            self.lcd1.display(self.showlist[self.now].factor1.tostr())
            self.lcd2.display(self.showlist[self.now].factor2.tostr())
            self.lcd3.display(self.showlist[self.now].answer.tostr())
            self.lcdop.setText(self.showlist[self.now].operator.tostr())

    # 接受对移动两根火柴问题求解完成的信号
    def getDone2(self, connect):
        ansNum = 0
        for equation in self.closed2:
            if equation.equal == True:
                ansNum = ansNum + 1
                self.showlist.append(equation)
        if ansNum == 0 or (ansNum == 1 and self.closed2[0] == self.showlist[0]):
            self.tips.setText('很抱歉，该等式通过移动两根火柴无解。')
        elif ansNum > 1 and self.closed2[0] == self.showlist[0]:
            self.allowed = 2
            self.initeq = 1
            self.now = self.now + 1
            info1 = '该问题是将等式变为新的等式问题, 有{}种新等式'
            info2 = '该问题的难度系数为{:.2f}'
            self.tips.setText(info1.format(ansNum - 1) + '<br>' + info2.format(len(self.closed2) / (ansNum - 1)))
            self.lcd1.display(self.showlist[self.now].factor1.tostr())
            self.lcd2.display(self.showlist[self.now].factor2.tostr())
            self.lcd3.display(self.showlist[self.now].answer.tostr())
            self.lcdop.setText(self.showlist[self.now].operator.tostr())
        else:
            self.allowed = 2
            info1 = '通过移动两根火柴使等式成立，有{}种可行的解法'
            info2 = '该问题的难度系数为{:.2f}'
            self.tips.setText(info1.format(ansNum) + '<br>' + info2.format(len(self.closed2)/ansNum))
            self.lcd1.display(self.showlist[self.now].factor1.tostr())
            self.lcd2.display(self.showlist[self.now].factor2.tostr())
            self.lcd3.display(self.showlist[self.now].answer.tostr())
            self.lcdop.setText(self.showlist[self.now].operator.tostr())

    # 接受上下翻信号
    def changeShow(self, flag):
        if flag == 1:
            if self.now == 0 or (self.initeq == 1 and self.now == 1):
                self.status.showMessage('已经是第一个结果')
            else:
                self.now = self.now - 1
        elif flag == 2:
            if self.now + 1 == len(self.showlist):
                self.status.showMessage('已经是最后一个结果')
            else:
                self.now = self.now + 1
        if len(self.showlist) > 0:
            self.lcd1.display(self.showlist[self.now].factor1.tostr())
            self.lcd2.display(self.showlist[self.now].factor2.tostr())
            self.lcd3.display(self.showlist[self.now].answer.tostr())
            self.lcdop.setText(self.showlist[self.now].operator.tostr())
        else:
            self.status.showMessage('您还未输入并求解问题')

    # 保存可行等式
    def saveEquation(self):
        if len(self.showlist) > 0:
            aim = ''
            eq = ''
            flag = 0
            if self.allowed == 1:
                aim = (self.closed1[0].factor1.tostr() + ';' +
                        self.closed1[0].factor2.tostr() + ';' +
                        self.closed1[0].answer.tostr() + ';' +
                        self.closed1[0].operator.tostr() + ';\n')
                eq = (self.closed1[0].factor1.tostr() +
                      self.closed1[0].operator.tostr() +
                      self.closed1[0].factor2.tostr() +
                      '=' +
                      self.closed1[0].answer.tostr())
            elif self.allowed == 2:
                aim = (self.closed2[0].factor1.tostr() + ';' +
                       self.closed2[0].factor2.tostr() + ';' +
                       self.closed2[0].answer.tostr() + ';' +
                       self.closed2[0].operator.tostr() + ';\n')
                eq = (self.closed2[0].factor1.tostr() +
                      self.closed2[0].operator.tostr() +
                      self.closed2[0].factor2.tostr() +
                      '=' +
                      self.closed2[0].answer.tostr())
            else:
                warn = QMessageBox.about(self, '无法保存', '抱歉，不可解等式无法保存!')
                flag = 1
            lib = open('../data/library.txt', 'r+')
            equations = lib.readlines()
            for equation in equations:
                if aim == equation:
                    warn = QMessageBox.about(self, '当前等式已存在', '感谢您的贡献！但您要添加的等式已在库中。')
                    flag = 1
                    break
            if flag == 0:
                lib.writelines(aim)
                # 刷新等式库
                self.lib.combobox.addItem(eq)
            lib.close()
        else:
            warn = QMessageBox.about(self, '无法保存', '抱歉，未被求解并证明可解的等式无法保存!')

    # 清空lcd显示
    def lcdClear(self):
        self.lcd1.display('')
        self.lcd2.display('')
        self.lcd3.display('')
        self.lcdop.setText('')
        self.tips.setText('')

    # 清空所有需保存的变量
    def varClear(self):
        self.closed1.clear()
        self.closed2.clear()
        self.showlist.clear()
        self.now = 0
        self.allowed = 0
        self.initeq = 0

    # 清除输入及变量
    def clearAction(self):
        self.facin1.clear()
        self.facin2.clear()
        self.opin.clear()
        self.ansin.clear()
        self.lcdClear()
        self.varClear()

    # 重写关闭函数
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '退出程序',
                                     "确认要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


    # 关闭窗口确认
    def sureClose(self):
        reply = QMessageBox.question(self, '退出程序',
                                     "确认要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            qApp.quit()
