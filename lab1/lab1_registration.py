import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit,QHBoxLayout,
                             QVBoxLayout)


class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()  # Call our function used to set up window

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Lab1-1 Registration GUI')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account.
        """
        # Create label for image
        
        title = QLabel(self)
        title.setText("Create New Account")
        title.setFont(QFont('Arial', 17))
        title.move(80, 15)
        
        image = "image/grinning-cat.png"
        try:
            with open(image):
                emoji = QLabel(self)
                pixmap = QPixmap(image)
                emoji.setPixmap(pixmap)
                emoji.move(120, 50)
        except FileNotFoundError:
            print("Image not found.")

        # Username and fullname labels and line edit widgets
        Username_label = QLabel(self)
        Username_label.setText("Username: ")
        Username_label.move(50, 190)
        self.Username = QLineEdit(self)
        self.Username.resize(200, 20)
        self.Username.move(150, 190)

        Fullname_label = QLabel(self)
        Fullname_label.setText("Fullname: ")
        Fullname_label.move(50, 220)
        self.Fullname = QLineEdit(self)
        self.Fullname.resize(200, 20)
        self.Fullname.move(150, 220)
        # Create password and confirm password labels and line edit widgets
        Pwd_label = QLabel(self)
        Pwd_label.setText("Password: ")
        Pwd_label.move(50,250)
        self.Pwd = QLineEdit(self)
        self.Pwd.resize(200, 20)
        self.Pwd.setEchoMode(QLineEdit.Password)
        self.Pwd.move(150,250)

        Comfirm_label = QLabel(self)
        Comfirm_label.setText("Comfirm: ")
        Comfirm_label.move(50,280)
        self.comfirm = QLineEdit(self)
        self.comfirm.resize(200, 20)
        self.comfirm.setEchoMode(QLineEdit.Password)
        self.comfirm.move(150,280)
        # Create sign up button
        sign_button = QPushButton("sign up", self)
        sign_button.move(125,320)
      


   
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec_())
