import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def dialog():
    mbox = QMessageBox()

    mbox.setText("System is started..")
    #mbox.setDetailedText("Yes, it is")
    #mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

def dialog1():
    mbox = QMessageBox()

    mbox.setText("Are you sure to stop?")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

def dialog2():
    mbox = QMessageBox()

    mbox.setText("System is reseting!")
    #mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

    def say_hello():
        print('Hello!')

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Plant Identification"
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 700, 500)

        text = QLabel(self)
        text.setText("Detecting in Progress")
        text.move(300, 50)

        label = QLabel(self, alignment = Qt.AlignCenter)
        pixmap = QPixmap('rumex.png')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)


        #label = QLabel(self)
        #label.setStyleSheet("QLabel" "{""border : 4px black;""}")
        #label.setGeometry(0, 0, 700, 500)
        #label.move(100, 50)
        #self.resize(pixmap.width(), pixmap.height())


        btn1 = QPushButton('Start', self)
        #btn1.setText("Start")
        btn1.setStyleSheet("background-color: green")
        btn1.setCursor(QCursor(Qt.PointingHandCursor))
        btn1.move(100, 450)
        btn1.clicked.connect(dialog)

        btn2 = QPushButton('Stop',self)
        #btn2.setText("Stop")
        btn2.setStyleSheet("background-color: red")
        btn2.setCursor(QCursor(Qt.PointingHandCursor))
        btn2.move(300, 450)
        btn2.clicked.connect(dialog1)

        btn3 = QPushButton('Reset',self)
        #btn3.setText("Reset")
        btn3.setStyleSheet("background-color: lightblue")
        btn3.setCursor(QCursor(Qt.PointingHandCursor))
        btn3.move(500, 450)
        btn3.clicked.connect(dialog2)

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

