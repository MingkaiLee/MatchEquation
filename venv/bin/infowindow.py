"""
关于本软件信息的子窗口
很高兴完成了从主程序到GUI的设计和编写，特别是UI还要学习PyQt5
本窗口将展示程序的信息和玩法
祝玩得开心！
Last edited date: 19. 10. 14
"""

import sys
from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QAction
from PyQt5.QtGui import QFont, QIcon, QPalette, QPixmap, QBrush, QColor
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.Qt import QPalette


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QTextBrowser(self)
        self.text.setOpenExternalLinks(True)
        self.change = QPushButton(self)
        self.textstate = 1
        self.ok = QPushButton(self)
        self.helpinfo = '<h2><center>游戏说明</center></h2>' \
                        '<hr>' \
                        '<p>1.Number1，Number2和Answer栏目支持2位整数输入，支持形如"07"，"00"形式的输入，但不支持负数。</p>' \
                        '<p>2.Operator栏目支持1位符号输入，仅支持"+"，"-"和"*"。</p>' \
                        '<p>3.工具栏的按钮从左到右依次为"搜索移动1根火柴"，"搜索移动2根火柴"，"清除输入及变量"，"等式库"，"保存' \
                        '当前等式"，"帮助和退出"，鼠标悬停在各按钮上时，主界面左下角的状态栏将描述其功能。</p>' \
                        '<p>4.若输入题目有解，搜索的结果将在主界面下方的数码管显示模块显示，显示模块的下方提示成立的结果和难度系数，' \
                        '如果解的数目超过了1，下方的按钮可以上下翻显示成立等式。</p>' \
                        '<p>5.希望老师及助教学长玩得开心，如有其它疑问可以与我联系，点击本界面左下角按钮，本界面将显示程序信息及' \
                        '本人的联系方式。</p>' \
                        '<br>' \
                        '<hr>' \
                        '<address align = "right">当前版本号:1.1.18</address>' \
                        '<br>'
        self.mineinfo = '<h3><center>关于SmartMatch</center></h3>' \
                        '<hr>' \
                        '<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"SmartMatch"是一款自动解决移动一根或两根火' \
                        '柴棒使火柴棒等式成立的游戏，其开发目的是为了完成作者在2019秋季学期的"人工智能基础"课程的大作业。</p>' \
                        '<address align = "right">' \
                        'Designed and Written by <a href="mailto:lmk17@mails.tsinghua.edu.cn">Li Mingkai</a>' \
                        '<br>' \
                        'Author GitHub:<a href="https://github.com/MingkaiLee">MingkaiLee</a><br>' \
                        'Wechat:lmk852834777<br>' \
                        'GUI Powered by<a href="https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html">' \
                        'PyQt5</a>&<a href="https://www.qt.io/">Qt</a>' \
                        '</address>'
        self.init_ui()

    def init_ui(self):
        width = 1440
        height = 900
        x = width / 3
        y = height / 3
        w = width / 3
        h = height / 3
        self.setGeometry(x, y, w, h)
        self.setWindowTitle('Help & Information')
        self.setWindowIcon(QIcon('../images/help.png'))
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap('../images/background2.jpeg')))
        self.setPalette(palette)

        # 设置文本浏览框
        self.text.move(w/12, h/8)
        self.text.resize(5*w/6, 3*h/4)
        palette2 = QPalette()
        palette2.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.text.setPalette(palette2)
        self.text.setText(self.helpinfo)

        # 切换显示信息功能按钮
        self.change.move(w/6, 9*h/10)
        self.change.resize(w/6, h/10)
        self.change.setText('切换')
        self.change.clicked.connect(lambda: self.changetext())

        # 关闭帮助窗口按钮
        self.ok.move(2*w/3, 9*h/10)
        self.ok.resize(w/6, h/10)
        self.ok.setText('关闭')
        self.ok.clicked.connect(lambda: self.closewindow())


    def changetext(self):
        if self.textstate == 1:
            self.text.setText(self.mineinfo)
            self.textstate = 2
        elif self.textstate == 2:
            self.text.setText(self.helpinfo)
            self.textstate = 1

    def closewindow(self):
        self.close()

