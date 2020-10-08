# 处理播放程序的基本功能
import pygame
import os


class VoicePlayer:
    def __init__(self, dir_path):
        self.dirPath = dir_path
        self.curIndex = 1
        self.finalIndex = self.get_final_index()
        print(self.finalIndex)

    def get_final_index(self):
        maxIndex = 0

        # 获取目录中所有文件名
        filelist = os.listdir(self.dirPath)    # 默认所有都是文件
        for fileName in filelist:
            # 去掉文件名后缀
            filename, _ = os.path.splitext(fileName)
            # 转为数字取最大的一个
            if maxIndex < int(filename):
                maxIndex = int(filename)
        return maxIndex
