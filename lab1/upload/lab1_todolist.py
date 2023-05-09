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
        

 ###       Must_box = QVBoxLayout()
       ### Must_h_box.setSpacing(60)  # Set spacing between in widgets in horizontal layout
 ###       Must_box.addStretch()
 ###       for rating in ratings:
  ###          rate_label = QLabel(rating, self)
   ###         ratings_h_box.addWidget(rate_label)
    ###    ratings_h_box.addStretch()
###
        


        # Create must-do section

        Must_box = QVBoxLayout()
        
        Must_box.addWidget(Must_Dos)
        
       
        # Create button group to contain checkboxes
    ###    scale_bg = QButtonGroup(self)
        Must_box.addStretch()
        
        
        
        def cr():
            self.Username = QTextEdit(self)
            self.Username.resize(10, 100)
            scale_cb = QCheckBox("", self)
            
            lit_box = QHBoxLayout()
            lit_box.addWidget(scale_cb)
            lit_box.addWidget(self.Username)
            
            
        
        for cb in range(5): 
           
                
           scale_cb = QCheckBox("", self)
           Must_box.addWidget(scale_cb)
           Must_box.addStretch(5)
        Must_box.addStretch(1)
           
       
        self.n = QTextEdit(self)
        self.n.move(90, 115)
        self.n1 = QTextEdit(self)
        self.n1.move(90, 195)
        self.n2 = QTextEdit(self)
        self.n2.move(90, 285)
        self.n3 = QTextEdit(self)
        self.n3.move(90, 365)
        self.n4 = QTextEdit(self)
        self.n4.move(90, 465) 
       
        
       
        
       
        
       
        
       
 #       Text_box = QVBoxLayout()
  #      for cb in range(15): 
  #          self.Username = QTextEdit(self)
  #         self.Username.resize(10, 100)
      ###    self.Username.move(150, 190)
           
  #          Text_box.addWidget(self.Username)
  #          Text_box.addStretch(5)
  #      Text_box.addStretch(1)










 #       little_box = QHBoxLayout()
  #      little_box.addLayout(Must_box)
   #     little_box.addLayout(Text_box)
    #    little_box.addStretch()


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
        
      ###  v_box1 =  QVBoxLayout()
        
        
        
        
        
        
        v_box2 =  QVBoxLayout()
        
        
        main_grid.addWidget(todo_title, 0, 0, 1,3)
      ###  main_grid.addStretch()
        main_grid.addLayout(Must_box, 1, 0, 1, 1)
      ###  main_grid.addWidget(App, 1, 2, 1, 1)
        main_grid.addLayout(Text_2box, 1, 3, 1, 1)
        
        main_grid.addWidget(close_button, 2, 2, 1, 1)
        
        
        
        
        self.setLayout(main_grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())
