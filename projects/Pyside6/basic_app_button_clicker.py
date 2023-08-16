from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont  # Import QFont from QtGui module

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clicker Game")
        # trying out different widgets
        self.setGeometry(100, 60, 1000, 800)
        custom_font = QFont("Arial", 16)  # Create a QFont instance with the desired font and size

        # self.setMinimumSize(QSize(400, 300))
        # Set the central widget of the Window.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.number = 0

        self.number_label = QLabel(f"Number: {self.number}")
        self.layout.addWidget(self.number_label)
        self.number_label.setFont(QFont('Arial', 20))
        

        
        self.win = QLabel("Click to win!")
        self.layout.addWidget(self.win)
        self.win.setFont(QFont('Arial', 20))


        self.button = QPushButton("Click +1")
        self.button.clicked.connect(self.button_click)
        self.button.setFixedSize(1000, 600)
        self.layout.addWidget(self.button)
        self.button.setFont(QFont('Arial', 600))
        self.button.setFont(custom_font)
    def button_click(self):
        self.number += 1
        self.number_label.setText(f"Number: {self.number}")






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()