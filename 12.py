# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/test/Desktop/1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_naver(object):
    def setupUi(self, naver):
        naver.setObjectName("naver")
        naver.resize(398, 81)
        self.URL_Box = QtWidgets.QLineEdit(naver)
        self.URL_Box.setGeometry(QtCore.QRect(20, 40, 271, 21))
        self.URL_Box.setText("")
        self.URL_Box.setObjectName("URL_Box")
        self.label = QtWidgets.QLabel(naver)
        self.label.setGeometry(QtCore.QRect(20, 10, 56, 21))
        self.label.setObjectName("label")
        self.Down_Button = QtWidgets.QPushButton(naver)
        self.Down_Button.setGeometry(QtCore.QRect(300, 40, 75, 23))
        self.Down_Button.setObjectName("Down_Button")
        self.retranslateUi(naver)
        self.URL_Box.returnPressed.connect(self.Down_Button.click)
        self.Down_Button.clicked.connect(naver.slot1_1st)
        QtCore.QMetaObject.connectSlotsByName(naver)

    def retranslateUi(self, naver):
        _translate = QtCore.QCoreApplication.translate
        naver.setWindowTitle(_translate("naver", "Dialog"))
        self.label.setText(_translate("naver", "URL"))
        self.Down_Button.setText(_translate("naver", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    naver = QtWidgets.QDialog()
    ui = Ui_naver()
    ui.setupUi(naver)
    naver.show()
    sys.exit(app.exec_())

