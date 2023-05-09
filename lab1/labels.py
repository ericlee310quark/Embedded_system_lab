import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import time

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabel Example')
        self.displayLabels()
        self.show()

    def displayLabels(self):
        """
        Display text and images using QLabels.
        Check to see if image files exist, if not throw an
        exception.
        """
        text = QLabel(self)
        text.setText("Hello")
        text.move(105, 15)
        image = "image/face-with-tears-of-joy.png"
  
        try:
          
            with open(image):
                emoji = QLabel(self)
                pixmap = QPixmap(image)
                emoji.setPixmap(pixmap)
                emoji.move(65, 65)
        except FileNotFoundError:
            print("Image not found.")


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())
