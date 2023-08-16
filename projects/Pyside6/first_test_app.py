from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel, QMainWindow,QCheckBox, QComboBox, QDateEdit, QVBoxLayout, QLineEdit, QPushButton

import requests
# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(100, 60, 1000, 800)

        self.setWindowTitle("NFT Minter")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.quantity = QLabel("Enter a quantity(optional)")
        self.layout.addWidget(self.quantity)

        self.quantity_input = QLineEdit()
        self.layout.addWidget(self.quantity_input)


        self.api_label = QLabel("Add API Key")
        self.layout.addWidget(self.api_label)

        self.api_input = QLineEdit()
        self.layout.addWidget(self.api_input)

        self.name_label = QLabel("Enter Name for NFT")
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.button = QPushButton("Mint NFT")
        self.button.clicked.connect(self.button_click)
        self.layout.addWidget(self.button)

    def button_click(self):
        api_key = self.api_input.text()
        nft_name = self.name_input.text()
        quantity_input = self.quantity_input.text()
        print("API Key:", api_key)
        print("NFT Name:", nft_name)
        print("Quantity:", quantity_input)



def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()