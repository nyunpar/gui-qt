import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("AppKu")
        
        button = QPushButton("Tekan Saya")
        
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()