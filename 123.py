# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/test/Desktop/1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
import urllib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from selenium import webdriver


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
        self.Down_Button.clicked.connect(self.Crawler_run())
        QtCore.QMetaObject.connectSlotsByName(naver)

    @pyqtSlot(name="slot1_1st")
    def slot1_1st(self):
        self.URL_Box.setText("아하하하하하하")

    def retranslateUi(self, naver):
        _translate = QtCore.QCoreApplication.translate
        naver.setWindowTitle(_translate("naver", "Dialog"))
        self.label.setText(_translate("naver", "URL"))
        self.Down_Button.setText(_translate("naver", "Download"))

    def naver_cafe_img_crawler(url):
        wd = webdriver.Chrome("./webdriver/chromedriver.exe")
        wd.get(url)
        wd.switch_to.frame("cafe_main")
        html = wd.page_source
        soup = BeautifulSoup(html, "html.parser")
        img_tag = soup.find("div", {"id": "tbody"})
        img_tags = img_tag.find_all("img")
        title_tag = soup.find("div", {"id": "main-area"})
        title = title_tag.find("span", {"class": "b m-tcol-c"}).string
        date = title_tag.find("td", {"class": "m-tcol-c date"}).string.split(" ")
        date = date[0].replace(".", "")
        save_path = os.getcwd()

        for i, img_src in enumerate(img_tags):
            src = img_src.get("src")
            if os.path.exists("{0}/{1}".format(save_path, date)):
                urllib.request.urlretrieve(src, "{0}/{1}/{2}_{3}.jpg".format(save_path, date, title, i + 1))
            else:
                os.makedirs("{0}/{1}".format(save_path, date))
                urllib.request.urlretrieve(src, "{0}/{1}/{2}_{3}.jpg".format(save_path, date, title, i + 1))


    url = "http://cafe.naver.com/temadica/711258"


    def Crawler_run(self):
        self.naver_cafe_img_crawler(self.URL_Box.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    naver = QtWidgets.QDialog()
    ui = Ui_naver()
    ui.setupUi(naver)
    naver.show()
    sys.exit(app.exec_())
