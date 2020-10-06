from PyQt5 import QtWidgets

from UI.EnglishCarefullListener import Ui_MainWindow
from tkinter import *
import tkinter.filedialog


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.addVoiceButton.clicked.connect(self.addVoice)

    def addVoice(self):
        #  弹出弹窗选择文件内容（可以批量）
        root = Tk()
        root.withdraw()  # 将Tkinter.Tk()实例隐藏
        filenames = tkinter.filedialog.askopenfilenames()
        root.destroy()

        #  拆分选择的文件音频到指定文件夹
        if len(filenames) is not 0:
            for filename in filenames:
                print(filename)
        #  在音频列表中展示音频项
