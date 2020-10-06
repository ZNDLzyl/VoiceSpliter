from PyQt5 import QtWidgets

from UI.EnglishCarefullListener import Ui_MainWindow


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addVoiceButton.clicked.connect(self.addVoice)
        # 给button 的 点击动作绑定一个事件处理函数

    def addVoice(self):
        #  此处编写具体的业务逻辑
        print("")
