import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QTextEdit, QSpinBox,
                             QComboBox, QHBoxLayout)


class GetApptForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Lab 1-3 Application Form GUI')
        self.formWidgets()
        self.show()

    def formWidgets(self):
        """
        Create widgets that will be used in the application form.
        """
        # Create widgets
        
        # Create horizontal layout and add age, height, and weight to h_box
        
        # Create horizontal layout and add time information
        
        # Create form layout
        
        # Add all widgets to form layout
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GetApptForm()
    sys.exit(app.exec_())
