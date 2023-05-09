import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QTextEdit, QSpinBox,
                             QComboBox, QHBoxLayout, QGridLayout)


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
        Title = QLabel("Appointment Submission Form")
        Title.setFont(QFont('Arial', 24))
        Title.setAlignment(Qt.AlignCenter)
        
        Full_nla = QLabel("Full Name")
        self.fullName = QLineEdit("")
        self.fullName.resize(200, 20)
        
        addr_la = QLabel("Address")
        self.addr = QLineEdit("")
        self.addr.resize(200, 20)


        Mo = QLabel("Mobile Number")
        self.mobile_num = QLineEdit()
        self.mobile_num.setInputMask("0000-000000;")
        self.addr.resize(200, 20)

        Age = QLabel("Age")
        self.age = QSpinBox()

        Height =QLabel("Height")
        self.height =QLineEdit("cm")

        Weight = QLabel("Weight")
        self.weight =QLineEdit("Weight")

        lit1 = QHBoxLayout()
        lit1.addWidget(Age)
        lit1.addWidget(self.age)
        lit1.addWidget(Height)
        lit1.addWidget(self.height)
        lit1.addWidget(Weight)
        lit1.addWidget(self.weight)






        Gender = QLabel("Gender")
        infomation = ["Male", "Female"]
        self.gender = QComboBox(self)
        self.gender.addItems(infomation)


        Past = QLabel("Past")
        self.past = QTextEdit("separate by ','")
        
        Blood = QLabel("Blood Type")
        infomation2 = ["A", "B","O","AB"]
        self.bl = QComboBox(self)
        self.bl.addItems(infomation2)

       
        

        De = QLabel("Desired Time")
        self.t1 = QSpinBox()
        infomation3 = [":00", ":01",":02",":03",":04",":05",":06",":07",":08",":09",":10"]
        for i in range(11,61):
            infomation3.append(":"+str(i))
        
        self.t2 = QComboBox(self)
        self.t2.addItems(infomation3)

        infomation4 = ["AM", "PM"]
        self.t3 = QComboBox(self)
        self.t3.addItems(infomation4)
        lit2 = QHBoxLayout()
        lit2.addWidget(De)
        lit2.addWidget(self.t1)
        lit2.addWidget(self.t2)
        lit2.addWidget(self.t3)

        # Create horizontal layout and add age, height, and weight to h_box
        


        # Create horizontal layout and add time information
        
        # Create form layout
        main_grid = QGridLayout()
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Arial', 
                                 12))
        todo_title.setAlignment(Qt.AlignCenter)
        # Add all widgets to form layout
        main_grid.addWidget(Title, 0, 0, 1,3)
        main_grid.addWidget(Full_nla, 1, 0, 1,1)
        main_grid.addWidget( self.fullName, 1, 1, 1,1)
        main_grid.addWidget(addr_la, 2, 0, 1,1)
        main_grid.addWidget(self.addr, 2, 1, 1,1)
        main_grid.addWidget(Mo, 3, 0, 1,1)
        main_grid.addWidget( self.mobile_num, 3, 1, 1,1)
  #      main_grid.addWidget(Age, 4, 0, 1,1)
   #     main_grid.addWidget(self.age, 4, 1, 1,1)
    #    main_grid.addWidget( Height, 4, 2, 1,1)
     #   main_grid.addWidget( self.height, 4, 3, 1,1)
      #  main_grid.addWidget( Weight, 4, 4, 1,1)
     #   main_grid.addWidget( self.weight, 4, 5, 1,1)
      
     
        main_grid.addLayout(lit1,4,0,1,2)
        main_grid.addWidget(  Gender, 5, 0, 1,1)
        main_grid.addWidget( self.gender, 5, 1, 1,1)
        main_grid.addWidget( Past, 6, 0, 1,1)
        main_grid.addWidget( self.past, 6, 1, 1,1)
        main_grid.addWidget(  Blood, 7, 0, 1,1)
        main_grid.addWidget( self.bl, 7, 1, 1,1)
        main_grid.addLayout(lit2,8,0,-1,-1)
    #    main_grid.addWidget( De, 8, 0, 1,1)
   #     main_grid.addWidget( self.t1, 8, 1, 1,1)
  #      main_grid.addWidget( self.t2, 8, 2, 1,1)
 #       main_grid.addWidget( self.t3, 8, 3, 1,1)

        self.setLayout(main_grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GetApptForm()
    sys.exit(app.exec_())
