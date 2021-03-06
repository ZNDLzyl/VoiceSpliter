import os
import tkinter.filedialog
from tkinter import *

from PyQt5 import QtWidgets
import shutil
from UI.EnglishCarefullListener import Ui_MainWindow
from UI.PlaySoundFormH import PlaySoundWin
from VoiceHandler.VoiceSegment import VoiceSegment


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rootPath = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource'

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.addVoiceButton.clicked.connect(self.add_voice)
        self.ui.delVoiceButton.clicked.connect(self.del_voice)
        self.ui.playVoiceButton.clicked.connect(self.play_voice)

        # 显示播放列表
        self.show_sound_list(self.rootPath)

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
        self.ui.soundVoiceList.clear()

        # 在列表中列出所有听力材料的名字（文件夹名称）
        items = os.listdir(file_dir)
        for item in items:
            self.ui.soundVoiceList.addItem(item)

    def del_voice(self):
        # 读取被选中的文件夹位置
        dirnames = self.ui.soundVoiceList.selectedItems()
        for dirname in dirnames:
            dirpath = os.path.join(self.rootPath, dirname.text())

            # 删除文件夹
            if os.path.exists(dirpath):
                shutil.rmtree(dirpath)

            # 重新加载播放列表
            self.show_sound_list(self.rootPath)

    def play_voice(self):
        # 读取被选中的文件夹位置
        dirnames = self.ui.soundVoiceList.selectedItems()
        if len(dirnames) == 0:
            return
        dirpath = os.path.join(self.rootPath, dirnames[0].text())

        # 新开一个窗口
        self.form2 = PlaySoundWin(dirpath)
        self.form2.show()
