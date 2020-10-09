import os

import pygame
from PyQt5 import QtWidgets

from UI.PlaySoundForm import Ui_PlaySoundForm


class PlaySoundWin(QtWidgets.QMainWindow):
    def __init__(self, dir_path):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_PlaySoundForm()
        self.ui.setupUi(self)
        self.dirPath = dir_path

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.preVoiceButton.clicked.connect(self.pre_voice)
        self.ui.playVoiceButton.clicked.connect(self.play_voice)
        self.ui.pauseVoiceButton.clicked.connect(self.pause_voice)
        self.ui.nextVoiceButton.clicked.connect(self.next_voice)
        self.ui.repeateVoiceButton.clicked.connect(self.repeate_voice)

        # 打开播放器
        self.curIndex = 1
        self.finalIndex, self.fileExtension = self.get_final_index()
        self.ispause = False
        pygame.mixer.init()

    def __del__(self):
        print('deleteplaysoundform')

    def play_voice_at_beginning(self):
        curPath = os.path.join(self.dirPath, '{}{}'.format(self.curIndex, self.fileExtension))
        pygame.mixer.music.load(curPath)
        pygame.mixer.music.play(0)
        self.ispause = False

    def pre_voice(self):
        if self.curIndex > 1:
            self.curIndex -= 1
        else:
            self.curIndex = self.finalIndex
        self.play_voice_at_beginning()
        print('pre_voice')

    def play_voice(self):
        if not self.ispause:
            self.play_voice_at_beginning()
        else:
            pygame.mixer.music.unpause()
            self.ispause = False

        print('play_voice')

    def pause_voice(self):
        pygame.mixer.music.pause()
        self.ispause = True
        print('pause_voice')

    def next_voice(self):
        if self.curIndex < self.finalIndex:
            self.curIndex += 1
        else:
            self.curIndex = 1
        self.play_voice_at_beginning()
        print('next_voice')

    def repeate_voice(self):
        self.play_voice_at_beginning()
        print('repeate_voice')

    def get_final_index(self):
        maxIndex = 0
        fileExtension = ''

        # 获取目录中所有文件名
        filelist = os.listdir(self.dirPath)  # 默认所有都是文件
        for fileName in filelist:
            # 去掉文件名后缀
            filename, extension = os.path.splitext(fileName)
            # 文件名转为数字 取最大的一个
            if maxIndex < int(filename):
                maxIndex = int(filename)
                fileExtension = extension
        return maxIndex, fileExtension
