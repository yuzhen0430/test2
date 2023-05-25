# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 502)
        Dialog.setStyleSheet("background-color: rgb(194, 255, 210);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 370, 161, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 21, 36);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 270, 161, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(249, 216, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 270, 161, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(188, 219, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 171, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../0508/emma.jpg"))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(620, 48, 121, 31))
        self.radioButton.setStyleSheet("font: 11pt \"Agency FB\";")
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton2.setGeometry(QtCore.QRect(620, 90, 121, 41))
        self.radioButton2.setStyleSheet("font: 11pt \"Agency FB\";")
        self.radioButton2.setAutoExclusive(True)
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton3.setGeometry(QtCore.QRect(620, 182, 121, 41))
        self.radioButton3.setStyleSheet("font: 18pt \"Agency FB\";")
        self.radioButton3.setAutoExclusive(True)
        self.radioButton3.setObjectName("radioButton3")
        self.radioButton4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton4.setGeometry(QtCore.QRect(620, 140, 121, 31))
        self.radioButton4.setStyleSheet("font: 18pt \"Agency FB\";")
        self.radioButton4.setAutoExclusive(True)
        self.radioButton4.setObjectName("radioButton4")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(410, 80, 71, 51))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setStyleSheet("font: 14pt \"Agency FB\";")
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 270, 80, 20))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 180, 361, 51))
        self.label.setStyleSheet("font: 12pt \"Agency FB\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(50, 390, 181, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 340, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "計算機2.0"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.radioButton.setText(_translate("Dialog", "＋"))
        self.radioButton2.setText(_translate("Dialog", "－"))
        self.radioButton3.setText(_translate("Dialog", "÷"))
        self.radioButton4.setText(_translate("Dialog", "×"))
        self.checkBox.setText(_translate("Dialog", "對調"))
        self.label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())