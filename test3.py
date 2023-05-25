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

def click_radio():
    print("click radio")




def clicked_hello():
    ui.label.setText("hello")
    print("hello")    

def pic_click(event):                 #點擊圖片
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_() 
    print(event.x())
    print(event.y())
    print(event.button())




app = QApplication(sys.argv)      #QT式子 忽略
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)


ui.pushButton.clicked.connect(clicked_press_me)     #連結按鍵
'''ui.helloButton.clicked.connect(clicked_hello)
ui.calculateButton.clicked.connect()'''
ui.label_2.mouseReleaseEvent = pic_click
ui.radioButton.clicked.connect(click_radio)

group1 = QButtonGroup(widge)           #群組內互斥
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton2)
group1.addButton(ui.radioButton3)
group1.addButton(ui.radioButton4)
ui.radioButton.clicked.connect(click_radio)

widge.show()
sys.exit(app.exec_())