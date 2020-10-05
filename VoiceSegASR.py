#!/usr/bin/env python3
# encoding: utf-8
'''
@file: audio_breakage.py
@time: 2020/5/10 0010 15:18
@author: Jack
@contact: jack18588951684@163.com
'''
# silence_thresh是认定小于-50dBFS以下的为silence，发现小于-50dBFS部分超过 600毫秒，就进行拆分

import os
import shutil

from pydub import AudioSegment
from pydub.silence import split_on_silence

init_id = 0
root = r'D:\Code\PycharmProjects\VoiceSpliter\Test'
file_lst = []
audiopath_lst = []
voiceLen = 7  # 句子不能短于的时间长度（s）
minSilenceLen = 200  # 发现小于音量超过的时间间隔（ms）
silenceThresh = -40  # 发现小于的音量（BFS）


# 加载数据
def search_audio(file_dir):
    """
    递归查找音频文件
    :param file_dir:
    :return:
    """
    items = os.listdir(file_dir)
    items = [os.path.join(file_dir, item) for item in items]
    for item in items:
        if not os.path.isdir(item):
            file_lst.append(item)


search_audio(root)

for file in file_lst:
    if len(file.split('.')) == 2:
        audiopath_lst.append(file)


def read_wave(path):
    format_type = path.split(".")[-1]
    if format_type in ["wav", "WAV"]:
        wav_audio = AudioSegment.from_file(path, format="wav")
    elif format_type == "mp3":
        wav_audio = AudioSegment.from_file(path, format="mp3")
    elif format_type == "m4a":
        wav_audio = AudioSegment.from_file(path, format="mp4")

    return wav_audio, format_type


for i, audiopath in enumerate(audiopath_lst):
    audiopath = os.path.join(root, audiopath)
    print(audiopath)

    # 读入音频

    sound, audiotype = read_wave(audiopath)

    # 切割
    print('开始切割')
    chunks = split_on_silence(sound, min_silence_len=minSilenceLen, silence_thresh=silenceThresh)
    filepath, tempfilename = os.path.split(audiopath)
    filename, extension = os.path.splitext(tempfilename)

    chunks_path = filepath + '\\chunks\\'
    if not os.path.exists(chunks_path):
        os.mkdir(chunks_path)
    # 清空选择的文件夹
    chunks_path = chunks_path + '\\' + filename + '\\'
    if os.path.exists(chunks_path):
        shutil.rmtree(chunks_path)
        os.mkdir(chunks_path)
    else:
        os.mkdir(chunks_path)

    print('开始保存音频片段')
    totalSec = 0  # 对于小于特定秒数的音频进行合并
    index = 0  # 第几段音频
    for j in range(len(chunks)):
        new = chunks[j]
        totalSec = new.duration_seconds
        if totalSec > voiceLen:
            index += 1
            save_name = chunks_path + '{}.{}'.format(index, audiotype)
            new.export(save_name, format=audiotype)
            totalSec = 0
            print('{}\t{}\t{}'.format(i + init_id, index, new.duration_seconds))
        elif totalSec <= voiceLen:
            # 如果音频小于7000ms 那么把它和后面一个音频进行合并
            if j < len(chunks) - 1:
                chunks[j + 1] = new + chunks[j + 1]
            # 如果后面没有音频了，那么直接输出这个音频
            else:
                index += 1
                save_name = chunks_path + '{}.{}'.format(index, audiotype)
                new.export(save_name, format=audiotype)
                totalSec = 0
                print('{}\t{}\t{}'.format(i + init_id, index, new.duration_seconds))

    print('保存完毕')
