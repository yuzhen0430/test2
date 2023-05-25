from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog
import sys


def isfloat(num):      #確認是否為浮點數
    try:               
        float(num)
        return True
    except ValueError:
        return False   

def clicked_press_me():
    x = ui.lineEdit.text()     
    y = ui.lineEdit_2.text()

    value1 = isfloat(x)   #確認是否為浮點數
    value2 = isfloat(y)
    if value1 and value2:
        print("true")
        message = QMessageBox()      #彈出視窗
        i = float(x) + float(y)                  #轉成數字                               
        message.setWindowTitle("surprise")
        message.setInformativeText(str(i))   #結果轉成字串
        message.exec_()

    else:
        print("false")
        message = QMessageBox()      #彈出視窗
        message.setWindowTitle("surprise")
        message.setInformativeText("error")   #結果轉成字串
        message.exec_()

def clicked_hello():
    ui.label.setText("hello")
    print("hello")    

def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_()        

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)

ui.pushButton.clicked.connect(clicked_press_me)     #連結按鍵
'''ui.helloButton.clicked.connect(clicked_hello)
ui.calculateButton.clicked.connect()'''
ui.label_2.mouseReleaseEvent = pic_click

widge.show()
sys.exit(app.exec_())
