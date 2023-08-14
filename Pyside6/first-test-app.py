from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel, QMainWindow,QCheckBox, QComboBox, QDateEdit, QVBoxLayout, QLineEdit


# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("My App")

        widgets = [
            
            QLineEdit,
            ]
        for widget in widgets:
          layout.addWidget(widget())
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()