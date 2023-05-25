from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog
import sys

def clicked_press_me():
    x = ui.lineEdit.text()
    message = QMessageBox()      #彈出視窗
    message.setWindowTitle("surprise")
    message.setInformativeText(x)
    message.exec_()

def clicked_hello():
    ui.label.setText("hello")
    print("hello")    

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)

ui.PressMeButton.clicked.connect(clicked_press_me)     #連結按鍵
ui.helloButton.clicked.connect(clicked_press_me)

widge.show()
sys.exit(app.exec_())




#pyuic5 -x mainwindow.ui -o mainwindow.py     #xxxx.ui轉成mainwindow.py
