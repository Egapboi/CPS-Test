import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPS Test")
        self.setGeometry(0, 0, 1200, 600)
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
        QTimer.singleShot(1000, self.buttonchoose)

    def buttonchoose(self):
        self.label.hide()
        self.label_select=QLabel("Select time", self)
        self.label_select.setGeometry(5, 5, 10, 10)
        self.setFont(QFont("Mono", 25))
        self.label_select.setStyleSheet("color: #87a0c7;"
        "background-color: #202938;"
        "font-weight: bold;")
        self.label_select.adjustSize()
        self.label_select.show()

        self.button_1sec=QPushButton("1 second", self)
        self.button_1sec.setGeometry(5, 60, 300, 40)
        self.button_2sec=QPushButton("2 second", self)
        self.button_2sec.setGeometry(5, 100, 300, 40)
        self.button_3sec=QPushButton("3 second", self)
        self.button_3sec.setGeometry(5, 140, 300, 40)
        self.button_5sec=QPushButton("5 second", self)
        self.button_5sec.setGeometry(5, 180, 300, 40)
        self.button_10sec=QPushButton("10 second", self)
        self.button_10sec.setGeometry(5, 220, 300, 40)
        self.button_30sec=QPushButton("30 second", self)
        self.button_30sec.setGeometry(5, 260, 300, 40)
        self.button_2m=QPushButton("Marathon (2 minute)", self)
        self.button_2m.setGeometry(5, 300, 500, 40)

        self.button_1sec.show()
        self.button_2sec.show()
        self.button_3sec.show()
        self.button_5sec.show()
        self.button_10sec.show()
        self.button_30sec.show()
        self.button_2m.show()

        self.button_1sec.clicked.connect(self.button_1sec_on_click)
        self.button_2sec.clicked.connect(self.button_2sec_on_click)
        self.button_3sec.clicked.connect(self.button_3sec_on_click)
        self.button_5sec.clicked.connect(self.button_5sec_on_click)
        self.button_10sec.clicked.connect(self.button_10sec_on_click)
        self.button_30sec.clicked.connect(self.button_30sec_on_click)
        self.button_2m.clicked.connect(self.button_2m_on_click)

    def button_1sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_1sec)
    def button_2sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_2sec)
    def button_3sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_3sec)
    def button_5sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_5sec)
    def button_10sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_10sec)
    def button_30sec_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_30sec)
    def button_2m_on_click(self):
        QTimer.singleShot(1000,self.buttonUI_2m)

    def buttonUI_1sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=1000

    def buttonUI_2sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=2000

    def buttonUI_3sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=3000
    
    def buttonUI_5sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=5000
    
    def buttonUI_10sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=10000
    
    def buttonUI_30sec(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=30000
    
    def buttonUI_2m(self):
        self.label.hide()
        self.button=QPushButton("Click me baby", self)
        self.button.setGeometry((self.width()-500)//2+200, (self.height()-500)//2, 500, 500)
        self.button.clicked.connect(self.on_click)
        self.no_clicks=0
        self.timer_started=False
        self.button.show()
        self.test_duration=120000

    def on_click(self):
        if not self.timer_started:
            self.timer_started=True
            QTimer.singleShot(self.test_duration, self.finished)
        print("click")
        self.no_clicks+=1
        print(self.no_clicks)

    def finished(self):
        self.button.hide()
        cps=self.no_clicks/round((self.test_duration/1000),2)
        print(cps)
        self.cps_label=QLabel(f"Your CPS is {cps}", self)
        self.cps_label.setFont(QFont("Mono", 40))
        self.cps_label.setStyleSheet("color: #87a0c7;"
        "background-color: #202938;"
        "font-weight: bold;")
        self.cps_label.adjustSize()
        self.cps_label.move((self.width()-self.cps_label.width())//2+200, (self.height()-self.cps_label.height())//2)
        self.cps_label.show()


    def retry(self):
        self.cps_label.hide()
        self.button_retry.hide()
        self.no_clicks=0
        self.buttonchoose()

def main():
    app=QApplication(sys.argv)
    app.setDesktopFileName("cps_test")
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
main()