from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AppKu")
        
        button = QPushButton("Tekan Saya!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Telah diklik")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()