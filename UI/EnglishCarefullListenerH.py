from PyQt5 import QtWidgets

from UI.EnglishCarefullListener import Ui_MainWindow
from tkinter import *
import tkinter.filedialog
from VoiceHandler.VoiceSegment import VoiceSegment
import os


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rootPath = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource'

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.addVoiceButton.clicked.connect(self.add_voice)

    def add_voice(self):
        #  弹出弹窗选择文件内容（可以批量）
        root = Tk()
        root.withdraw()  # 将Tkinter.Tk()实例隐藏
        filenames = tkinter.filedialog.askopenfilenames()
        root.destroy()

        #  拆分选择的文件音频到指定文件夹
        if len(filenames) is not 0:
            for filename in filenames:
                self.ui.plainTextEdit.setReadOnly(True)
                vs = VoiceSegment()

                # 读入音频(需要引入线程否则执行过程不能展示)
                self.ui.plainTextEdit.appendPlainText('正在读入音频{}...'.format(filename))
                audiotype, chunks, chunks_path = vs.split_voice(filename)
                if audiotype is not None and chunks is not None and chunks_path is not None:
                    self.ui.plainTextEdit.appendPlainText('音频{}分割成功'.format(filename))
                else:
                    self.ui.plainTextEdit.appendPlainText('您选择的文件不能被识别！请选择程序可以识别的音频文件！')
                    return

                # 保存音频
                self.ui.plainTextEdit.appendPlainText('开始保存音频片段')
                vs.save_voice(audiotype, chunks, chunks_path)
                self.ui.plainTextEdit.appendPlainText('保存完毕')

        #  在音频列表中展示音频项
        self.show_sound_list(self.rootPath)

    def show_sound_list(self, file_dir):
        # 在列表中列出所有听力材料的名字（文件夹名称）
        items = os.listdir(file_dir)
        for item in items:
            print(item)
            self.ui.soundVoiceList.addItem(item)
