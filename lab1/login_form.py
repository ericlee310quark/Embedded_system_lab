import sys

from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Using Checkboxes")
        self.setGeometry(50, 50, 500, 500)
        self.initializeUI()

    def initializeUI(self):
        # Input field
        self.name = QLineEdit(self)
        self.surname = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.name.move(150, 50)
        self.surname.setPlaceholderText("Enter your surname")
        self.surname.move(150, 80)

        # Checkbox field
        self.remember = QCheckBox("Remember me", self)
        self.remember.move(150, 110)

        # Submit button
        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.remember.isChecked():
            print("Name : " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me checked")
        else:
            print("Name : " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me not checked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
