# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnglishCarefullListener.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.soundVoiceList = QtWidgets.QListWidget(self.centralwidget)
        self.soundVoiceList.setGeometry(QtCore.QRect(10, 10, 431, 401))
        self.soundVoiceList.setObjectName("soundVoiceList")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 430, 551, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.addVoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.addVoiceButton.setGeometry(QtCore.QRect(450, 10, 111, 41))
        self.addVoiceButton.setObjectName("addVoiceButton")
        self.delVoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.delVoiceButton.setGeometry(QtCore.QRect(450, 60, 111, 41))
        self.delVoiceButton.setObjectName("delVoiceButton")
        self.playVoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.playVoiceButton.setGeometry(QtCore.QRect(450, 110, 111, 41))
        self.playVoiceButton.setObjectName("playVoiceButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "英语听力精听"))
        self.addVoiceButton.setText(_translate("MainWindow", "新增音频"))
        self.delVoiceButton.setText(_translate("MainWindow", "删除音频"))
        self.playVoiceButton.setText(_translate("MainWindow", "播放音频"))

