import wave
import numpy
import pylab as pl
from numpy import *

# 该程序未实现分割功能，实现代码见VoiceSegASR.py
# 打开wav文件
f = wave.open(r"D:\Code\TimeManager\Test\englishTest.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# print(nchannels, sampwidth, framerate, nframes)
str_data = f.readframes(nframes)
f.close()

# 将波形数据转换成数组
# 需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = numpy.fromstring(str_data, dtype=numpy.short)
wave_data.shape = -1, 2
wave_data2 = wave_data.T[0]  # 此数据即0通道为能量数据
l = len(wave_data2)


# sec = 0.05  #定义单位时间，也是预计停顿间隔时间
# emax= 100   #定义判定能量

def point(sec, emax):
    intl = l % int(sec * 44100)
    wave_data1 = delete(wave_data2, arange(l - intl, l + 1), 0)  # 删除掉后面的数据
    wave_data1.shape = -1, int(sec * 44100)  # 形成数据矩阵，列数即每个时间间隔内的数据
    wave_data1 = abs(wave_data1)
    # times = numpy.arange(0, nframes) * (1.0 / framerate)
    enemax = amax(wave_data1, axis=1)  # 寻找到每个时间间隔内最大的能量值
    eneave = sum(wave_data1, axis=1) / len(wave_data1)  # 计算每个时间间隔内平均的能量值
    idx = list(where(enemax - eneave < emax)[0])
    i = 1
    wr = [[0]]
    j = 0
    for i in range(len(idx)):  # 如果实际停顿时间远大于预估停顿时间则进行筛选
        if (int(idx[i]) - int(idx[i - 1])) < 1.5 / sec:  # 相邻
            wr[j].extend([idx[i]])
        else:
            wr.append([idx[i]])
            j = j + 1
    idx = []
    for i in range(len(wr)):
        idx.append(wr[i][int(len(wr[i]) / 2)])

    dataload = array(idx) * sec
    dataload = dataload[dataload > 33]
    return dataload


a = 0.01
pl.subplot(111)
for emax in range(300, 1100, 100):
    lll = []
    num = []
    for seca in range(1, 20):
        datamax = point(float(seca * a), int(emax))
        lll.append(len(datamax))
        num.append(len(where(datamax < 80)[0]))
    secv = arange(1, 20) * a
    print(emax)
    pl.plot(secv, lll, label=str(emax))
pl.legend(loc='upper left')
pl.grid()
pl.show()

# pip install -i http://mirrors.aliyun.com/pypi/simple/ pygame --trusted-host mirrors.aliyun.com
from numpy import *
import pygame
import time

# file=input("请输入分句记录点文件放入本程序目录，并输入文件名\n")
file = r'data1.txt'
f = open(file)
times = list()
for line in f.readlines():
    inearr = line.strip()
    times.append(inearr)
file = r'test1.mp3'

i = 0
print()
while i != len(times) - 1:
    print('这是第 %s 段音频,共 %s 段音频。' % ((i + 1), (len(times) - 1)))
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play(0, float(times[i]))
    time.sleep(float(times[i + 1]) - float(times[i]))
    pygame.mixer.music.stop()
    str = input('键入1进行下一句，其它则重复本句\n')
    if str == '1':
        print('读取下一句')
        i += 1
    else:
        i = i
print('播放结束')
