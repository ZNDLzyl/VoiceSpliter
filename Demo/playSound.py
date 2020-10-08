from pydub import AudioSegment
from pydub.playback import play
import pygame
import time
import os
import pydub
from VoiceHandler import VoiceSegment

# need to pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
# download from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

soundPath = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource\englishTest'
# song = AudioSegment.from_file(soundPath, format="mp3")
# play(song)

# test pygame 暂停 播放 停止功能


# # pygame.init()
# pygame.mixer.init()
# # pygame.display.set_mode([300,300])
# pygame.mixer.music.load(soundPath)
# # pygame.mixer.music.set_volume(100)
# print(pygame.mixer.music.get_pos())
# pygame.mixer.music.play()
# print(pygame.mixer.music.get_endevent())
# time.sleep(5)
# pygame.mixer.music.pause()
# time.sleep(2)
# pygame.mixer.music.unpause()
# time.sleep(5)
# pygame.mixer.music.stop()
# # pygame.mixer.music.set_endevent(111)
# print(pygame.mixer.music.get_endevent())
# print(pygame.mixer.music.get_pos())

pygame.mixer.init()
index = 0
while True:
    index += 1
    curpath = os.path.join(soundPath, '{}.{}'.format(index, 'wav'))
    sound, audiotype = VoiceSegment.read_wave(curpath)
    sleeptime = sound.duration_seconds

    pygame.mixer.music.load(curpath)
    pygame.mixer.music.play(0)
    time.sleep(sleeptime)
