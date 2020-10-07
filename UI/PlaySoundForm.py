# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlaySoundForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlaySoundForm(object):
    def setupUi(self, PlaySoundForm):
        PlaySoundForm.setObjectName("PlaySoundForm")
        PlaySoundForm.resize(463, 74)
        self.preVoiceButton = QtWidgets.QPushButton(PlaySoundForm)
        self.preVoiceButton.setGeometry(QtCore.QRect(10, 20, 75, 31))
        self.preVoiceButton.setObjectName("preVoiceButton")
        self.playVoiceButton = QtWidgets.QPushButton(PlaySoundForm)
        self.playVoiceButton.setGeometry(QtCore.QRect(100, 20, 75, 31))
        self.playVoiceButton.setObjectName("playVoiceButton")
        self.pauseVoiceButton = QtWidgets.QPushButton(PlaySoundForm)
        self.pauseVoiceButton.setGeometry(QtCore.QRect(190, 20, 75, 31))
        self.pauseVoiceButton.setObjectName("pauseVoiceButton")
        self.nextVoiceButton = QtWidgets.QPushButton(PlaySoundForm)
        self.nextVoiceButton.setGeometry(QtCore.QRect(280, 20, 75, 31))
        self.nextVoiceButton.setObjectName("nextVoiceButton")
        self.repeateVoiceButton = QtWidgets.QPushButton(PlaySoundForm)
        self.repeateVoiceButton.setGeometry(QtCore.QRect(370, 20, 75, 31))
        self.repeateVoiceButton.setObjectName("repeateVoiceButton")

        self.retranslateUi(PlaySoundForm)
        QtCore.QMetaObject.connectSlotsByName(PlaySoundForm)

    def retranslateUi(self, PlaySoundForm):
        _translate = QtCore.QCoreApplication.translate
        PlaySoundForm.setWindowTitle(_translate("PlaySoundForm", "播放"))
        self.preVoiceButton.setText(_translate("PlaySoundForm", "上一句"))
        self.playVoiceButton.setText(_translate("PlaySoundForm", "播放"))
        self.pauseVoiceButton.setText(_translate("PlaySoundForm", "暂停"))
        self.nextVoiceButton.setText(_translate("PlaySoundForm", "下一句"))
        self.repeateVoiceButton.setText(_translate("PlaySoundForm", "重复"))

