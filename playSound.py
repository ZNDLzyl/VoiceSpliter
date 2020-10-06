from pydub import AudioSegment
from pydub.playback import play

# need to pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
# download from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

soundPath = r'D:\Code\PycharmProjects\VoiceSpliter\Test\englishTest.wav'
song = AudioSegment.from_wav(soundPath)
play(song)
