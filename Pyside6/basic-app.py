from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # trying out different widgets
        # button = QLabel("Press Me!")
        button = QPushButton("Press Me!")
        # button.setFixedSize(QSize(400, 300))
        button.setMaximumSize(QSize(400, 300))
        # self.setMinimumSize(QSize(400, 300))
        # Set the central widget of the Window.
        self.setCentralWidget(button)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = QPushButton("I love to be clicked.")
# window = QmainWindow()
window = MainWindow()

window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.