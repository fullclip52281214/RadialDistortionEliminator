# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BarrelDistortionUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileButton.setGeometry(QtCore.QRect(1340, 20, 75, 41))
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.DisplayFilePath = QtWidgets.QTextEdit(self.centralwidget)
        self.DisplayFilePath.setGeometry(QtCore.QRect(1430, 20, 471, 41))
        self.DisplayFilePath.setObjectName("DisplayFilePath")
        self.ImgDisplay = QtWidgets.QLabel(self.centralwidget)
        self.ImgDisplay.setGeometry(QtCore.QRect(20, 20, 1280, 720))
        self.ImgDisplay.setObjectName("ImgDisplay")
        self.LR2 = QtWidgets.QLabel(self.centralwidget)
        self.LR2.setGeometry(QtCore.QRect(1560, 110, 151, 21))
        self.LR2.setObjectName("LR2")
        self.R2 = QtWidgets.QSlider(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(1340, 140, 561, 31))
        self.R2.setOrientation(QtCore.Qt.Horizontal)
        self.R2.setObjectName("R2")
        self.R4 = QtWidgets.QSlider(self.centralwidget)
        self.R4.setGeometry(QtCore.QRect(1340, 230, 561, 31))
        self.R4.setOrientation(QtCore.Qt.Horizontal)
        self.R4.setObjectName("R4")
        self.LR4 = QtWidgets.QLabel(self.centralwidget)
        self.LR4.setGeometry(QtCore.QRect(1560, 200, 121, 21))
        self.LR4.setObjectName("LR4")
        self.R6 = QtWidgets.QSlider(self.centralwidget)
        self.R6.setGeometry(QtCore.QRect(1340, 320, 561, 31))
        self.R6.setOrientation(QtCore.Qt.Horizontal)
        self.R6.setObjectName("R6")
        self.LR6 = QtWidgets.QLabel(self.centralwidget)
        self.LR6.setGeometry(QtCore.QRect(1560, 300, 101, 16))
        self.LR6.setObjectName("LR6")
        self.Lcentx = QtWidgets.QLabel(self.centralwidget)
        self.Lcentx.setGeometry(QtCore.QRect(1570, 390, 131, 21))
        self.Lcentx.setObjectName("Lcentx")
        self.centx = QtWidgets.QSlider(self.centralwidget)
        self.centx.setGeometry(QtCore.QRect(1340, 410, 561, 31))
        self.centx.setOrientation(QtCore.Qt.Horizontal)
        self.centx.setObjectName("centx")
        self.SaveImg = QtWidgets.QPushButton(self.centralwidget)
        self.SaveImg.setGeometry(QtCore.QRect(1780, 680, 111, 41))
        self.SaveImg.setObjectName("SaveImg")
        self.Lcenty = QtWidgets.QLabel(self.centralwidget)
        self.Lcenty.setGeometry(QtCore.QRect(1570, 480, 131, 21))
        self.Lcenty.setObjectName("Lcenty")
        self.centy = QtWidgets.QSlider(self.centralwidget)
        self.centy.setGeometry(QtCore.QRect(1340, 500, 561, 31))
        self.centy.setOrientation(QtCore.Qt.Horizontal)
        self.centy.setObjectName("centy")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(1620, 680, 111, 41))
        self.Reset.setObjectName("Reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFileButton.setText(_translate("MainWindow", "Open image"))
        self.ImgDisplay.setText(_translate("MainWindow", "TextLabel"))
        self.LR2.setText(_translate("MainWindow", "Deformation 2th term"))
        self.LR4.setText(_translate("MainWindow", "Deformation 4th term"))
        self.LR6.setText(_translate("MainWindow", "Deformation 6th term"))
        self.Lcentx.setText(_translate("MainWindow", "focus position X"))
        self.SaveImg.setText(_translate("MainWindow", "Save picture"))
        self.Lcenty.setText(_translate("MainWindow", "focus position Y"))
        self.Reset.setText(_translate("MainWindow", "Reset Slider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

