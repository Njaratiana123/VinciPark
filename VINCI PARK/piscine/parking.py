# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parcking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VinciPark(object):
    def setupUi(self, VinciPark):
        VinciPark.setObjectName("VinciPark")
        VinciPark.setEnabled(True)
        VinciPark.resize(1170, 584)
        self.label_2 = QtWidgets.QLabel(VinciPark)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/parking-427955_1920.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(VinciPark)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/vinci.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(VinciPark)
        self.label_3.setGeometry(QtCore.QRect(10, 460, 171, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/expences-button-png-hi.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.parking = QtWidgets.QFrame(VinciPark)
        self.parking.setGeometry(QtCore.QRect(0, 0, 941, 591))
        self.parking.setStyleSheet("")
        self.parking.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parking.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parking.setObjectName("parking")
        self.label_4 = QtWidgets.QLabel(self.parking)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 941, 591))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/de.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.parking)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(80, 50, 241, 411))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.parking)
        self.label_6.setGeometry(QtCore.QRect(360, 50, 241, 411))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.parking)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(630, 50, 241, 411))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/voiture.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.statistic = QtWidgets.QFrame(VinciPark)
        self.statistic.setGeometry(QtCore.QRect(940, -20, 231, 611))
        self.statistic.setStyleSheet("background-color: rgb(190, 255, 225);")
        self.statistic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statistic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statistic.setObjectName("statistic")
        self.label_8 = QtWidgets.QLabel(self.statistic)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.statistic)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton.raise_()

        # Code debut
        self.statistic.setVisible(False)
        self.parking.setVisible(False)

        # Event Listener
        self.pushButton.clicked.connect(self.start)

    # Fonction
    def start(self):
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.pushButton.setVisible(False)
        self.parking.setVisible(True)

        self.retranslateUi(VinciPark)
        QtCore.QMetaObject.connectSlotsByName(VinciPark)

    def retranslateUi(self, VinciPark):
        _translate = QtCore.QCoreApplication.translate
        VinciPark.setWindowTitle(_translate("VinciPark", "VinciPark"))
        self.pushButton.setText(_translate("VinciPark", "START"))
        self.label_8.setText(_translate("VinciPark", "Place libre : 3"))
        self.label_9.setText(_translate("VinciPark", "Place occupée : 0"))
import sary_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VinciPark = QtWidgets.QDialog()
    ui = Ui_VinciPark()
    ui.setupUi(VinciPark)
    VinciPark.show()
    sys.exit(app.exec_())
