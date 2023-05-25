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
        a = ui.radioButton.isChecked()      #回傳值   #是否被勾選
        b = ui.radioButton2.isChecked()
        c = ui.radioButton4.isChecked()
        d = ui.radioButton3.isChecked()
        #print(a,b,c,d)
        if ui.checkBox.isChecked():   #對調
            x, y = y, x

            '''tamp = x  #交換
            x = y
            y = tmp '''

        if a:
            i = float(x) + float(y)    
        if b:
            i = float(x) - float(y)
        if c:
            i = float(x) * float(y)
        if d:
            i = float(x) / float(y)
        i = i*ui.horizontalSlider.value()/100      #與水平軸連動  
        if ui.comboBox.currentText()=="中文":      #轉換中英文
            r = "答案是"+str(i)
    
        if ui.comboBox.currentText()=="English":
            r = "anser is "+str(i)
                   
        message.setWindowTitle("surprise")   #視窗顯示的文字
        message.setInformativeText(r)   #結果轉成字串
        ui.label.setText(r)
        message.exec_()

    else:
        print("false")
        message = QMessageBox()      #彈出視窗
        message.setWindowTitle("surprise")
        message.setInformativeText("error")   #結果轉成字串
        message.exec_()             #執行

def click_radio():                   #設定radiobutton
    print("click radio")
    a = ui.radioButton
    b = ui.radioButton2
    c = ui.radioButton4
    d = ui.radioButton3

def clicked_hello():
    ui.label.setText("hello")
    print(ui.checkBox.isChecked())
    print(ui.comboBox.currentText())
    print(ui.comboBox.currentIndex())
    ui.progressBar.setValue(40)

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


t = QTranslator()             #語言轉換式子    #放啟動指令前!!!
t.load("chinese.qm")
app.installTranslator(t)


ui = Ui_Dialog()
ui.setupUi(widge)


def change(i):           #傳入一值
    print(i)
    ui.progressBar.setValue(i)
def slider_change():
    x = ui.horizontalSlider.value()
    print("change value is "+str(x))
    change(x)               #改進度條數值

def slider_release():
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("選擇的數值是 "+ str(ui.horizontalSlider.value()))
    message.exec_()

ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(3)
ui.horizontalSlider.setMaximum(100)
ui.horizontalSlider.setMinimum(0)
ui.horizontalSlider.valueChanged.connect(slider_change)
ui.horizontalSlider.sliderReleased.connect(slider_release)

ui.pushButton.clicked.connect(clicked_press_me)     #連結按鍵
'''ui.helloButton.clicked.connect(clicked_hello)
ui.calculateButton.clicked.connect()'''
ui.label_2.mouseReleaseEvent = pic_click
ui.radioButton.clicked.connect(click_radio)
#ui.checkBox.clicked.connect(change)
ui.comboBox.addItems(["中文","English"])

group1 = QButtonGroup(widge)           #群組內互斥
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton2)
group1.addButton(ui.radioButton3)
group1.addButton(ui.radioButton4)
ui.radioButton.clicked.connect(click_radio)


widge.show()
sys.exit(app.exec_())