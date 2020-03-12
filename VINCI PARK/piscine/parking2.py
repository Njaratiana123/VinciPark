# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parcking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import serial
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread


class SerialThread(QThread):
    def __init__(self, ui):
        QThread.__init__(self)
        self.variable = 1
        self.variable2 = 1
        self.process = None
        self.ser = serial.Serial('COM4', baudrate=115200, timeout=1)

    def run(self):
        while True:
            self.process = self.ser.readline().decode('utf-8')
            print(self.process[6] + self.process[24])
            self.variable = int(self.process[6])
            self.variable2 = int(self.process[24])
            if self.variable2 == 1:
                print("mete")
                if self.variable == 1:
                    ui.voiture1.setVisible(True)
                else:
                    ui.voiture1.setVisible(False)
            if self.variable2 == 2:
                print("mete")
                if self.variable == 1:
                    ui.voiture2.setVisible(True)
                else:
                    ui.voiture2.setVisible(False)
            if self.variable2 == 3:
                print("mete")
                if self.variable == 1:
                    ui.voiture3.setVisible(True)
                else:
                    ui.voiture3.setVisible(False)


class Ui_VinciPark(object):
    def __init__(self, parent=None):
        self.serialThread = SerialThread(self)

    def setupUi(self, VinciPark):
        VinciPark.setObjectName("VinciPark")
        VinciPark.setEnabled(True)
        VinciPark.resize(1170, 584)
        self.fondacceuil = QtWidgets.QLabel(VinciPark)
        self.fondacceuil.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.fondacceuil.setText("")
        self.fondacceuil.setPixmap(QtGui.QPixmap(":/newPrefix/parking-427955_1920.jpg"))
        self.fondacceuil.setScaledContents(True)
        self.fondacceuil.setObjectName("fondacceuil")
        self.parklogo = QtWidgets.QLabel(VinciPark)
        self.parklogo.setGeometry(QtCore.QRect(10, 10, 181, 241))
        self.parklogo.setText("")
        self.parklogo.setPixmap(QtGui.QPixmap(":/newPrefix/vinci.jpg"))
        self.parklogo.setScaledContents(True)
        self.parklogo.setObjectName("parklogo")
        self.pushButton = QtWidgets.QPushButton(VinciPark)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(20, 460, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.fondstart = QtWidgets.QLabel(VinciPark)
        self.fondstart.setGeometry(QtCore.QRect(10, 460, 171, 61))
        self.fondstart.setText("")
        self.fondstart.setPixmap(QtGui.QPixmap(":/newPrefix/expences-button-png-hi.png"))
        self.fondstart.setScaledContents(True)
        self.fondstart.setObjectName("fondstart")
        self.parking = QtWidgets.QFrame(VinciPark)
        self.parking.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.parking.setStyleSheet("")
        self.parking.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parking.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parking.setObjectName("parking")
        self.fondparking = QtWidgets.QLabel(self.parking)
        self.fondparking.setEnabled(True)
        self.fondparking.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.fondparking.setStyleSheet("")
        self.fondparking.setText("")
        self.fondparking.setPixmap(QtGui.QPixmap(":/newPrefix/de.jpg"))
        self.fondparking.setScaledContents(True)
        self.fondparking.setObjectName("fondparking")
        self.voiture1 = QtWidgets.QLabel(self.parking)
        self.voiture1.setEnabled(True)
        self.voiture1.setGeometry(QtCore.QRect(120, 50, 241, 411))
        self.voiture1.setText("")
        self.voiture1.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.voiture1.setScaledContents(True)
        self.voiture1.setObjectName("voiture1")
        self.voiture2 = QtWidgets.QLabel(self.parking)
        self.voiture2.setGeometry(QtCore.QRect(480, 50, 241, 411))
        self.voiture2.setStyleSheet("")
        self.voiture2.setText("")
        self.voiture2.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.voiture2.setScaledContents(True)
        self.voiture2.setObjectName("voiture2")
        self.voiture3 = QtWidgets.QLabel(self.parking)
        self.voiture3.setEnabled(True)
        self.voiture3.setGeometry(QtCore.QRect(820, 50, 241, 411))
        self.voiture3.setText("")
        self.voiture3.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.voiture3.setScaledContents(True)
        self.voiture3.setObjectName("voiture3")
        self.fondparking.raise_()
        self.voiture1.raise_()
        self.voiture3.raise_()
        self.voiture2.raise_()
        self.fondacceuil.raise_()
        self.parklogo.raise_()
        self.fondstart.raise_()
        self.pushButton.raise_()
        self.parking.raise_()
        self.parklogo.setBuddy(self.parklogo)

        self.retranslateUi(VinciPark)
        QtCore.QMetaObject.connectSlotsByName(VinciPark)

        # Code
        self.parking.setVisible(False)
        self.voiture1.setVisible(False)
        self.voiture2.setVisible(False)
        self.voiture3.setVisible(False)
        # Event Listener
        self.pushButton.clicked.connect(self.start)

    # Fonction
    def start(self):
        self.fondstart.setVisible(False)
        self.fondacceuil.setVisible(False)
        self.parklogo.setVisible(False)
        self.pushButton.setVisible(False)
        self.parking.setVisible(True)
        self.serialThread.start()

    def voiture1(self):
        self.voiture1.setVisible(True)

    def voiture2(self):
        self.voiture2.setVisible(True)

    def voiture3(self):
        self.voiture3.setVisible(True)

    def retranslateUi(self, VinciPark):
        _translate = QtCore.QCoreApplication.translate
        VinciPark.setWindowTitle(_translate("VinciPark", "VinciPark"))
        self.pushButton.setText(_translate("VinciPark", "START"))


import sary_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    VinciPark = QtWidgets.QDialog()
    ui = Ui_VinciPark()
    ui.setupUi(VinciPark)
    VinciPark.show()
    sys.exit(app.exec_())
