from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AppKu")
        
        button = QPushButton("Tekan Saya!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Telah diklik")
        
    def the_button_was_toggled(self,checked):
        print("Checked?",checked)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()