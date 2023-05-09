import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit)


class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()  # Call our function used to set up window

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Create New User')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account.
        """
        # Create label for image
        new_user_image = "image/grinning-cat.png"
        try:
            with open(new_user_image):
                new_user = QLabel(self)
                pixmap = QPixmap(new_user_image)
                new_user.setPixmap(pixmap)
                new_user.move(150, 60)
        except FileNotFoundError:
            print("Image not found.")

        login_label = QLabel(self)
        login_label.setText("Create New Account")
        login_label.move(60, 20)
        login_label.setFont(QFont('Arial', 20))
        # Username and fullname labels and line edit widgets
        name_label = QLabel("Username:", self)
        name_label.move(50, 200)
        self.name_entry = QLineEdit(self)
        self.name_entry.move(130, 200)
        self.name_entry.resize(200, 20)
        name_label = QLabel("Full name:", self)
        name_label.move(50, 230)
        name_entry = QLineEdit(self)
        name_entry.move(130, 230)
        name_entry.resize(200, 20)
        # Create password and confirm password labels and line edit widgets
        pswd_label = QLabel("Password:", self)
        pswd_label.move(50, 260)
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.pswd_entry.move(130, 260)
        self.pswd_entry.resize(200, 20)
        confirm_label = QLabel("Confirm:", self)
        confirm_label.move(50, 290)
        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.move(130, 290)
        self.confirm_entry.resize(200, 20)
        # Create sign up button
        sign_up_button = QPushButton("sign up", self)
        sign_up_button.move(100, 330)
        sign_up_button.resize(200, 40)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec_())
