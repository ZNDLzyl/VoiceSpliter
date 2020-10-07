from PyQt5 import QtWidgets
from UI.PlaySoundForm import Ui_PlaySoundForm

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_PlaySoundForm()
        self.ui.setupUi(self)
        self.rootPath = r'D:\Code\PycharmProjects\VoiceSpliter\SoundSource'

        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.preVoiceButton.clicked.connect(self.pre_voice)
        self.ui.playVoiceButton.clicked.connect(self.play_voice)
        self.ui.pauseVoiceButton.clicked.connect(self.pause_voice)
        self.ui.nextVoiceButton.clicked.connect(self.next_voice)
        self.ui.repeateVoiceButton.clicked.connect(self.repeate_voice)

    def pre_voice(self):
        print('pre_voice')

    def play_voice(self):
        print('')

    def pause_voice(self):
        print('')

    def next_voice(self):
        print('')

    def repeate_voice(self):
        print('')