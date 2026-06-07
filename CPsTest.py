import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPS Test")
        self.setGeometry(0, 0, 800, 600)
        self.initUI()
    
    def initUI(self):
        self.label=QLabel("Welcome to CP", self)
        self.label.setGeometry(((self.width()-580)//2), ((self.height()-50)//2)-50, 200, 50)
        self.label.setFont(QFont("Mono", 40))
        self.label.setStyleSheet("color: #87a0c7;"
        "background-color: #202938;"
        "font-weight: bold;")
        self.label.adjustSize()
        QTimer.singleShot(2500, self.change_label)

    def change_label(self):
        self.label.setText("Welcome to CPS Test")
        self.label.adjustSize()
        QTimer.singleShot(1000, self.buttonUI)

    def buttonUI(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.button.show()
        QTimer.singleShot(5000, self.finished)
    
    def on_click(self):
        print("click")
        self.no_clicks+=1
        print(self.no_clicks)

    def finished(self):
        self.button.hide()
        cps=self.no_clicks/(5000/1000)
        print(cps)
        self.cps_label=QLabel(f"Your CPS is {cps}", self)
        self.cps_label.setFont(QFont("Mono", 40))
        self.cps_label.setStyleSheet("color: #87a0c7;"
        "background-color: #202938;"
        "font-weight: bold;")
        self.cps_label.adjustSize()
        self.cps_label.move((self.width()-self.cps_label.width())//2, (self.height()-self.cps_label.height())//2)
        self.cps_label.show()
        self.no_clicks=0

def main():
    app=QApplication(sys.argv)
    app.setDesktopFileName("cps_test")
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
main()