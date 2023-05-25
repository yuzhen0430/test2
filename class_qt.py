
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from mainwindow import Ui_Dialog
import sys

class MyWindow(QMainWindow):
    def __init__(self):            #介面
        super().__init__()    #呼叫副類別的init
        self.ui = Ui_Dialog()     #定義物件
        self.ui.setupUi(self)     #設定物件特徵 
        self.ui.pushButton.clicked.connect(self.clicked_hello)
        self.group1 = QButtonGroup(self)       #定義物件
        self.group1.addButton(self.ui.radioButton)    #設定物件特徵 
        self.group1.addButton(self.ui.radioButton2)

        
        
    def clicked_hello(self):          #跳出的物件
        print("hello")
        message = QMessageBox() 
        message.setWindowTitle("surprise")  
        message.setInformativeText("你按了圖片") 

if __name__=="__main__":
    app = QApplication(sys.argv)    
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_()) 

    


