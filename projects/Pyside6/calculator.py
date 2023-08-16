from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont  # Import QFont from QtGui module

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        # trying out different widgets
        self.setGeometry(100, 60, 1000, 800)
        custom_font = QFont("Arial", 16)  # Create a QFont instance with the desired font and size
        self.total = 0

        # self.setMinimumSize(QSize(400, 300))
        # Set the central widget of the Window.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.number_label = QLabel(f"Total: {self.total}")
        self.layout.addWidget(self.number_label)
        self.number_label.setFont(QFont('Arial', 20))
        
        self.running_number = 0
        self.running = QLabel(f"Running Number: {self.running_number}")
        self.layout.addWidget(self.running)
        self.running.setFont(QFont('Arial', 20))

        self.oneButton = QPushButton("1")
        self.oneButton.clicked.connect(self.one)
        self.oneButton.setFixedSize(50, 50)
        self.layout.addWidget(self.oneButton)
        self.oneButton.setFont(QFont('Arial', 50))
        self.oneButton.setFont(custom_font)

        self.twoButton = QPushButton("2")
        self.twoButton.clicked.connect(self.two)
        self.twoButton.setFixedSize(50, 50)
        self.layout.addWidget(self.twoButton)
        self.twoButton.setFont(QFont('Arial', 50))
        self.twoButton.setFont(custom_font)



        self.button = QPushButton("calculate")
        self.button.clicked.connect(self.calculate)
        self.button.setFixedSize(500, 100)
        self.layout.addWidget(self.button)
        self.button.setFont(QFont('Arial', 600))
        self.button.setFont(custom_font)


    def calculate(self):
        self.total += self.running_number

        self.number_label.setText(f"Number: {self.total}")


    def one(self):
        self.running_number = self.running_number + 1
        self.running.setText(f"Running Number: {self.total}")

    def two(self):
        print("2")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()