import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout,QHBoxLayout)


class ToDoList(QWidget):
    def __init__(self):  # Constructor
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle('Lab1-2 ToDo List GUI')
        self.setupWidgets()
        self.show()

    def setupWidgets(self):
        main_grid = QGridLayout()
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        
     
        Must_Dos = QLabel("Must Dos")
        Must_Dos.setFont(QFont('Arial', 24))
        
        
        App = QLabel("Appointments")
        App.setFont(QFont('Arial', 24))
        
       
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        # Create section labels for to-do list
        

        # Create must-do section

        Must_box = QVBoxLayout()
        Must_box.setContentsMargins(5,5,5,5)
        Must_box.addWidget(Must_Dos)
        
       
        # Create button group to contain checkboxes
    ###    scale_bg = QButtonGroup(self)
    #    Must_box.addStretch()
        
        Must_row = []
        scale_cb = []
        self.Must_text = []

        for row in range(15):
            self.Must_text.append(QTextEdit(self))
            scale_cb.append(QCheckBox("", self))
         #   self.Must_text[row].resize(200,10)
            self.Must_text[row].setMinimumSize(200, 10)
            Must_row.append(QHBoxLayout())
            Must_row[row].addWidget(scale_cb[row])
            Must_row[row].addWidget(self.Must_text[row])
            Must_box.addLayout(Must_row[row])
         #   Must_box.addStretch()
        

    #    Must_box.addStretch()


        Text_2box = QVBoxLayout()
        Text_2box.setContentsMargins(5,5,5,5)
        
        Text_2box.addWidget(App)
        
        Morning = QLabel("Morning")
        Morning.setFont(QFont('Arial', 24))
        
        Text_2box.addWidget(Morning)
        
        
        self.M1 =QTextEdit(self)
        self.M1.setPlaceholderText("")
        
        Text_2box.addWidget(self.M1)
        
        Noon = QLabel("Noon")
        Noon.setFont(QFont('Arial', 24))
        Text_2box.addWidget(Noon)
        
        self.M2 =QTextEdit(self)
        self.M2.setPlaceholderText("")
        
        Text_2box.addWidget(self.M2)
        
        Evening =QLabel("Evening")
        Evening.setFont(QFont('Arial', 24))
        Text_2box.addWidget(Evening)
        self.M3 =QTextEdit(self)
        self.M3.setPlaceholderText("")
        
        Text_2box.addWidget(self.M3)
        
        # Create checkboxes and line edit widgets

        # Create labels for appointments section

        # Create vertical layout and add widgets

        # Add other layouts to main layout
        
        
        
        
        v_box2 =  QVBoxLayout()
        
        
        main_grid.addWidget(todo_title, 0, 0, 1,3)
      ###  main_grid.addStretch()
        main_grid.addLayout(Must_box, 1, 0, 1, 1)
      ###  main_grid.addWidget(App, 1, 2, 1, 1)
        main_grid.addLayout(Text_2box, 1, 3, 1, 1)
        
        main_grid.addWidget(close_button, 2, 2, 1, 1)
        
        main_grid.setContentsMargins(5,5,5,5)
        
        
        self.setLayout(main_grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())
