from PyQt5 import QtWidgets
from UI.PlaySoundForm import Ui_PlaySoundForm
from VoiceHandler.VoicePlayer import VoicePlayer


class PlaySoundWin(QtWidgets.QMainWindow):
    def __init__(self, dir_path):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_PlaySoundForm()
        self.ui.setupUi(self)
        self.dirPath = dir_path
        self.vp = VoicePlayer(dir_path)

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.preVoiceButton.clicked.connect(self.pre_voice)
        self.ui.playVoiceButton.clicked.connect(self.play_voice)
        self.ui.pauseVoiceButton.clicked.connect(self.pause_voice)
        self.ui.nextVoiceButton.clicked.connect(self.next_voice)
        self.ui.repeateVoiceButton.clicked.connect(self.repeate_voice)

    def pre_voice(self):
        print('pre_voice')
        print(self.dirPath)

    def play_voice(self):
        print('play_voice')

    def pause_voice(self):
        print('pause_voice')

    def next_voice(self):
        print('next_voice')

    def repeate_voice(self):
        print('repeate_voice')
