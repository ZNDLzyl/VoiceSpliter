#  a demo to test the QT

from PyQt5 import QtWidgets
import sys
from UI.EnglishCarefullListenerH import query_window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())
