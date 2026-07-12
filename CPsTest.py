import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CPS Test")
        self.setGeometry(100, 100, 1200, 600)
        self.setStyleSheet("background-color: #202938;") 
        
        self.test_duration = 5000
        self.no_clicks = 0
        self.timer_started = False
        self.time_buttons = []
        
        self.initUI()
    
    def initUI(self):
        self.label = QLabel("Welcome to CP", self)
        self.label.setFont(QFont("Mono", 40))
        self.label.setStyleSheet("color: #87a0c7; font-weight: bold;")
        self.label.adjustSize()
        self.label.move((self.width() - self.label.width()) // 2, (self.height() - self.label.height()) // 2)
        self.label.show()
        
        QTimer.singleShot(1500, self.change_label)
    
    def change_label(self):
        self.label.setText("Welcome to CPS Test")
        self.label.adjustSize()
        self.label.move((self.width() - self.label.width()) // 2, (self.height() - self.label.height()) // 2)
        
        QTimer.singleShot(1000, self.buttonchoose)

    def buttonchoose(self):
        self.label.hide()
        
        self.label_select = QLabel("Select Time Duration", self)
        self.label_select.setFont(QFont("Mono", 30))
        self.label_select.setStyleSheet("color: #87a0c7; font-weight: bold;")
        self.label_select.adjustSize()
        self.label_select.move((self.width() - self.label_select.width()) // 2, 80)
        self.label_select.show()

        intervals = [
            ("1 Sec", 1000), ("2 Sec", 2000), ("3 Sec", 3000), 
            ("5 Sec", 5000), ("10 Sec", 10000), ("30 Sec", 30000), 
            ("2 Min", 120000), ("Custom", -1)
        ]
        
        self.time_buttons.clear()
        
        start_x = (self.width() - (4 * 160 + 3 * 20)) // 2 # Center the 4x2 grid of buttons
        start_y = 200
        
        for i, (text, ms) in enumerate(intervals):
            btn = QPushButton(text, self)
            btn.setFont(QFont("Mono", 16))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2e3b4e; 
                    color: #87a0c7; 
                    border: 2px solid #87a0c7; 
                    border-radius: 8px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #3d4f68;
                }
            """)
            btn.resize(160, 60)
            
            row = i // 4
            col = i % 4
            btn.move(start_x + col * 180, start_y + row * 80)
            btn.clicked.connect(lambda checked, duration=ms: self.set_duration_and_start(duration))
            btn.show()
            self.time_buttons.append(btn)

    def set_duration_and_start(self, duration):
        if duration == -1:
            seconds, ok = QInputDialog.getInt(self, "Custom Time", "Enter duration in seconds:", value=5, min=1, max=3600)
            if ok:
                self.test_duration = seconds * 1000
            else:
                return
        else:
            self.test_duration = duration
            
        self.label_select.hide()
        for btn in self.time_buttons:
            btn.deleteLater()
        self.time_buttons.clear()
        self.buttonUI()

    def buttonUI(self):
        self.no_clicks = 0
        self.timer_started = False
        
        self.click_btn = QPushButton("CLICK HERE TO START", self)
        self.click_btn.setFont(QFont("Mono", 28))
        self.click_btn.setStyleSheet("""
            QPushButton {
                background-color: #2e3b4e;
                color: #87a0c7;
                border: 4px dashed #87a0c7;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3d4f68;
            }
        """)
        self.click_btn.setGeometry(100, 100, 1000, 400)
        self.click_btn.clicked.connect(self.on_click)
        self.click_btn.show()

    def on_click(self):
        if not self.timer_started:
            self.timer_started = True
            self.click_btn.setText("CLICK!!!")
            QTimer.singleShot(self.test_duration, self.finished)
        self.no_clicks += 1

    def finished(self):
        self.click_btn.hide()
        self.click_btn.deleteLater()
        if hasattr(self, "cps_label"):
            self.cps_label.deleteLater()
            
        cps = self.no_clicks / (self.test_duration / 1000)
        
        self.cps_label = QLabel(f"Your CPS is {cps:.2f}\nTotal Clicks: {self.no_clicks}", self)
        self.cps_label.setAlignment(Qt.AlignCenter)
        self.cps_label.setFont(QFont("Mono", 40))
        self.cps_label.setStyleSheet("color: #87a0c7; font-weight: bold;")
        self.cps_label.adjustSize()
        self.cps_label.move((self.width() - self.cps_label.width()) // 2, (self.height() - self.cps_label.height()) // 2)
        self.cps_label.show()
        self.restart_btn = QPushButton("Try Again", self)
        self.restart_btn.setFont(QFont("Mono", 16))
        self.restart_btn.setStyleSheet("background-color: #2e3b4e; color: #87a0c7; border: 2px solid #87a0c7;")
        self.restart_btn.setGeometry((self.width() - 200) // 2, self.height() - 100, 200, 50)
        self.restart_btn.clicked.connect(self.restart_game)
        self.restart_btn.show()

    def restart_game(self):
        self.cps_label.hide()
        self.restart_btn.hide()
        self.restart_btn.deleteLater()
        self.buttonchoose()

def main():
    app = QApplication(sys.argv)
    app.setDesktopFileName("cps_test")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()