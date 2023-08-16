from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel, QMainWindow,QCheckBox, QComboBox, QDateEdit, QVBoxLayout, QLineEdit, QPushButton


# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("NFT Minter")
        self.setGeometry(100, 100, 1200, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Enter Data")
        self.layout.addWidget(self.label)

        self.label = QLineEdit()
        self.layout.addWidget(self.label)
        self.label = QLabel("Add API Key")
        self.layout.addWidget(self.label)
        self.label = QLineEdit()
        self.layout.addWidget(self.label)
        self.button = QPushButton("Create NFT")
        self.layout.addWidget(self.button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()