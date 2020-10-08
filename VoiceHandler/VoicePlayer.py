# 处理播放程序的基本功能
import pygame
import os
from VoiceHandler import VoiceSegment
import time


class VoicePlayer:
    def __init__(self, dir_path):
        self.dirPath = dir_path
        self.curIndex = 1
        self.finalIndex, self.fileExtension = self.get_final_index()
        pygame.mixer.init()

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

    def play_voice(self):
        # 播放音频直到finalIndex
        while self.curIndex <= self.finalIndex:
            curPath = os.path.join(self.dirPath, '{}{}'.format(self.curIndex, self.fileExtension))
            sound, audiotype = VoiceSegment.read_wave(curPath)
            sleeptime = sound.duration_seconds

            pygame.mixer.music.load(curPath)
            pygame.mixer.music.play(0)
            time.sleep(sleeptime)
            self.curIndex += 1
