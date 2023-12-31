from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtGui import QFont  # Import QFont from QtGui module

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        # trying out different widgets
        self.setGeometry(100, 60, 1000, 800)
        custom_font = QFont("Arial", 16) 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        layout2 = QHBoxLayout()  # Create a horizontal layout

        self.central_widget.setLayout(self.layout)
         # Create a QFont instance with the desired font and size
        self.total = 0

        self.operation = ""

        


        # self.setMinimumSize(QSize(400, 300))
        # Set the central widget of the Window.


        self.number_label = QLabel(f"{self.total}")
        self.layout.addWidget(self.number_label)
        self.number_label.setFont(QFont('Arial', 20))
        
        self.running_number = 0

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





        self.plusButton = QPushButton("+")
        self.plusButton.clicked.connect(self.add)
        self.plusButton.setFixedSize(50, 50)
        self.layout.addWidget(self.plusButton)
        self.plusButton.setFont(QFont('Arial', 50))
        self.plusButton.setFont(custom_font)

        self.oneButton = QPushButton("-")
        self.oneButton.clicked.connect(self.subtract)
        self.oneButton.setFixedSize(50, 50)
        self.layout.addWidget(self.oneButton)
        self.oneButton.setFont(QFont('Arial', 50))
        self.oneButton.setFont(custom_font)

        self.oneButton = QPushButton("*")
        self.oneButton.clicked.connect(self.multiply)
        self.oneButton.setFixedSize(50, 50)
        self.layout.addWidget(self.oneButton)
        self.oneButton.setFont(QFont('Arial', 50))
        self.oneButton.setFont(custom_font)

        self.oneButton = QPushButton("/")
        self.oneButton.clicked.connect(self.divide)
        self.oneButton.setFixedSize(50, 50)
        self.layout.addWidget(self.oneButton)
        self.oneButton.setFont(QFont('Arial', 50))
        self.oneButton.setFont(custom_font)

        self.button = QPushButton("calculate")
        self.button.clicked.connect(self.calculate)
        self.button.setFixedSize(500, 100)
        self.layout.addWidget(self.button)
        self.button.setFont(QFont('Arial', 600))
        self.button.setFont(custom_font)




    def add(self):
        self.operation = "add"

    def subtract(self):
        self.operation = "subtract"

    def multiply(self):
        self.operation = "multiply"

    def divide(self):
        self.operation = "divide"

    def calculate(self):
        self.total += self.running_number

        self.number_label.setText(f"{self.total}")


    def one(self):
        self.running_number = self.running_number + 1
        

    def two(self):
        print("2")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()