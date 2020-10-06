import os
import shutil

from pydub import AudioSegment
from pydub.silence import split_on_silence


class VoiceSegment:
    root = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource'
    audiopath_lst = []
    voiceLen = 7  # 句子不能短于的时间长度（s）
    minSilenceLen = 200  # 发现小于音量超过的时间间隔（ms）
    silenceThresh = -40  # 发现小于的音量（BFS）

    #  读取文件
    def read_wave(self, path):
        format_type = path.split(".")[-1]
        if format_type in ["wav", "WAV"]:
            wav_audio = AudioSegment.from_file(path, format="wav")
        elif format_type == "mp3":
            wav_audio = AudioSegment.from_file(path, format="mp3")
        elif format_type == "m4a":
            wav_audio = AudioSegment.from_file(path, format="mp4")
        else:
            wav_audio = None

        return wav_audio, format_type

    #  对给定path的文件进行拆分
    def split_voice(self, audiopath):

        # 音频文件基本信息
        filepath, tempfilename = os.path.split(audiopath)
        filename, extension = os.path.splitext(tempfilename)

        # 读入音频
        print('开始读入音频', tempfilename)
        sound, audiotype = self.read_wave(audiopath)
        if not sound:
            print('您选择的文件不能被识别！请选择程序可以识别的音频文件！')
            return

        # 切割
        print('开始切割')
        chunks = split_on_silence(sound, min_silence_len=self.minSilenceLen, silence_thresh=self.silenceThresh)

        chunks_path = self.root + '\\'
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
            if totalSec > self.voiceLen:
                index += 1
                save_name = chunks_path + '{}.{}'.format(index, audiotype)
                new.export(save_name, format=audiotype)
                totalSec = 0
                # print('{}\t{}\t{}'.format(i + init_id, index, new.duration_seconds))
            elif totalSec <= self.voiceLen:
                # 如果音频小于7000ms 那么把它和后面一个音频进行合并
                if j < len(chunks) - 1:
                    chunks[j + 1] = new + chunks[j + 1]
                # 如果后面没有音频了，那么直接输出这个音频
                else:
                    index += 1
                    save_name = chunks_path + '{}.{}'.format(index, audiotype)
                    new.export(save_name, format=audiotype)
                    totalSec = 0
                    # print('{}\t{}\t{}'.format(i + init_id, index, new.duration_seconds))

        print('保存完毕')
