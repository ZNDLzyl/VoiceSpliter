# -*-coding:utf-8-*-
from time import ctime, sleep
import threading
import pygame
import time
import os
from VoiceHandler import VoiceSegment


def loop():
    soundPath = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource\englishTest'
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


def main():
    print('start at', ctime())
    t = threading.Thread(target=loop)
    t.start()
    print('DONE AT:', ctime())


if __name__ == '__main__':
    main()
