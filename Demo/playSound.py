from pydub import AudioSegment
from pydub.playback import play
import pygame
import time

# need to pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
# download from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

soundPath = r'D:\Code\PycharmProjects\VoiceSpliter\Test\afghan-woman-earns-top-marks-on-national-exams.mp3'
# song = AudioSegment.from_file(soundPath, format="mp3")
# play(song)

# test pygame 暂停 播放 停止功能
# pygame.init()
pygame.mixer.init()
# pygame.display.set_mode([300,300])
pygame.mixer.music.load(soundPath)
# pygame.mixer.music.set_volume(100)
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.pause()
time.sleep(2)
pygame.mixer.music.unpause()
time.sleep(5)
pygame.mixer.music.stop()
