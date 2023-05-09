import os
import sys

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QPushButton, QCheckBox, QSpinBox, QDoubleSpinBox, QFrame, QFileDialog,
                             QMessageBox, QHBoxLayout, QVBoxLayout, QAction)

style_sheet = """
    QLabel#ImageLabel{
        color: darkgrey;
        border: 2px solid #000000;
        qproperty-alignment: AlignCenter       
    }"""


class ImageProcessingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Initialize the window and display its contents to the screen."""
        self.setMinimumSize(900, 600)
        self.setWindowTitle('Lab5-1 - Image Processing GUI')

        self.contrast_adjusted = False
        self.brightness_adjusted = False
        self.image_smoothing_checked = False
        self.edge_detection_checked = False

        self.setupWindow()
        self.setupMenu()
        self.show()

    def setupWindow(self):
        """Set up widgets in the main window."""
        self.image_label = QLabel()
        self.image_label.setObjectName("ImageLabel")

        # Create various widgets for image processing in the side panel
        contrast_label = QLabel("Contrast [Range: 0.0:4.0]")
        self.contrast_spinbox = QDoubleSpinBox()
        self.contrast_spinbox.setMinimumWidth(100)
        # TODO: Set the accepted range of contrast_spinbox to match the description above
        self.contrast_spinbox.setMinimum(0.0)
        self.contrast_spinbox.setMaximum(4.0)

        self.contrast_spinbox.setValue(1.0)
        self.contrast_spinbox.setSingleStep(.10)
        self.contrast_spinbox.valueChanged.connect(self.adjustContrast)

        brightness_label = QLabel("Brightness [Range: -127:127]")
        self.brightness_spinbox = QSpinBox()
        self.brightness_spinbox.setMinimumWidth(100)
        # TODO: Set the accepted range of brightness_spinbox to match the description above
        self.brightness_spinbox.setMinimum(-127)
        self.brightness_spinbox.setMaximum(127)

        self.brightness_spinbox.setValue(0)
        self.brightness_spinbox.setSingleStep(1)
        self.brightness_spinbox.valueChanged.connect(self.adjustBrightness)

        smoothing_label = QLabel("Image Smoothing Filters")
        self.filter_2D_cb = QCheckBox("2D Convolution")
        self.filter_2D_cb.stateChanged.connect(self.imageSmoothingFilter)

        edges_label = QLabel("Detect Edges")
        self.canny_cb = QCheckBox("Canny Edge Detector")
        self.canny_cb.stateChanged.connect(self.edgeDetection)

        self.apply_process_button = QPushButton("Apply Processes")
        self.apply_process_button.setEnabled(False)
        self.apply_process_button.clicked.connect(self.applyImageProcessing)

        reset_button = QPushButton("Reset Image Settings")
        reset_button.clicked.connect(self.resetImageAndSettings)

        # Create horizontal and vertical layouts for the side panel and main window
        side_panel_v_box = QVBoxLayout()
        side_panel_v_box.setAlignment(Qt.AlignTop)
        side_panel_v_box.addWidget(contrast_label)
        side_panel_v_box.addWidget(self.contrast_spinbox)
        side_panel_v_box.addWidget(brightness_label)
        side_panel_v_box.addWidget(self.brightness_spinbox)
        side_panel_v_box.addSpacing(15)
        side_panel_v_box.addWidget(smoothing_label)
        side_panel_v_box.addWidget(self.filter_2D_cb)
        side_panel_v_box.addWidget(edges_label)
        side_panel_v_box.addWidget(self.canny_cb)
        side_panel_v_box.addWidget(self.apply_process_button)
        side_panel_v_box.addStretch(1)
        side_panel_v_box.addWidget(reset_button)

        side_panel_frame = QFrame()
        side_panel_frame.setMinimumWidth(200)
        side_panel_frame.setFrameStyle(QFrame.WinPanel)
        side_panel_frame.setLayout(side_panel_v_box)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.image_label, 1)
        main_h_box.addWidget(side_panel_frame)

        # Create container widget and set main window's widget
        container = QWidget()
        container.setLayout(main_h_box)
        self.setCentralWidget(container)

    def setupMenu(self):
        """Simple menu bar to select and save local images."""
        # Create actions for file menu
        open_act = QAction('Open...', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openImageFile)

        save_act = QAction('Save...', self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveImageFile)

        # Create menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)

    def adjustContrast(self):
        """The slot corresponding to adjusting image contrast."""
        if self.image_label.pixmap() is not None:
            self.contrast_adjusted = True

    def adjustBrightness(self):
        """The slot corresponding to adjusting image brightness."""
        if self.image_label.pixmap() is not None:
            self.brightness_adjusted = True

    def imageSmoothingFilter(self, state):
        """The slot corresponding to applying 2D Convolution for smoothing the image."""
        if state == Qt.Checked and self.image_label.pixmap() is not None:
            self.image_smoothing_checked = True
        elif state != Qt.Checked and self.image_label.pixmap() is not None:
            self.image_smoothing_checked = False

    def edgeDetection(self, state):
        """The slot corresponding to applying edge detection."""
        if state == Qt.Checked and self.image_label.pixmap() is not None:
            self.edge_detection_checked = True
        elif state != Qt.Checked and self.image_label.pixmap() is not None:
            self.edge_detection_checked = False

    def applyImageProcessing(self):
        """For the boolean variables related to the image processing techniques, if
        True, apply the corresponding process to the image and display the changes
        in the QLabel, image_label."""
        if self.contrast_adjusted is True or self.brightness_adjusted is True:
            contrast = self.contrast_spinbox.value()
            brightness = self.brightness_spinbox.value()
            self.cv_image = cv2.convertScaleAbs(self.cv_image, self.processed_cv_image, contrast, brightness)
        if self.image_smoothing_checked:
            # TODO: apply a 5x5 averaging filter to cv_image to smooth it.
            self.cv_image = cv2.blur(self.cv_image, (5, 5))

            pass
        if self.edge_detection_checked:
            # TODO: apply canny edge detector to cv_image.
            self.cv_image = cv2.Canny(self.cv_image, 250, 250)

            pass
        self.convertCVToQImage(self.cv_image)

        self.image_label.repaint()  # Repaint the updated image on the label

    def resetImageAndSettings(self):
        """Reset the displayed image and widgets used for image processing."""
        answer = QMessageBox.information(self, "Reset Image",
                                         "Are you sure you want to reset the image settings?", QMessageBox.Yes
                                         | QMessageBox.No, QMessageBox.No)

        if answer == QMessageBox.No:
            pass
        elif answer == QMessageBox.Yes and self.image_label.pixmap() is not None:
            self.resetWidgetValues()
            self.cv_image = self.copy_cv_image  # Restore the original image
            self.convertCVToQImage(self.copy_cv_image)

    def resetWidgetValues(self):
        """Reset the spinbox and checkbox values to their beginning values."""
        # TODO: Reset contrast_spinbox to 1.0; brightness_spinbox to 0; uncheck filter_2D_cb & canny_cb
        self.contrast_spinbox.setValue(1.0)
        self.brightness_spinbox.setValue(1.0)
        self.filter_2D_cb.setChecked(False)
        self.canny_cb.setChecked(False)
        pass

    def openImageFile(self):
        """Open an image file and display the contents in the label widget."""
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image",
                                                    os.getenv('HOME'), "Images (*.png *.jpeg *.jpg *.bmp)")

        if image_file:
            self.resetWidgetValues()  # Reset the states of the widgets
            self.apply_process_button.setEnabled(True)

            self.cv_image = cv2.imread(image_file)  # Original image
            self.copy_cv_image = self.cv_image  # A copy of the original image
            # Create a destination image for the contrast and brightness processes
            self.processed_cv_image = np.zeros(self.cv_image.shape, self.cv_image.dtype)
            self.convertCVToQImage(self.cv_image)  # Convert the OpenCV image to a Qt Image
        else:
            QMessageBox.information(self, "Error",
                                    "No image was loaded.", QMessageBox.Ok)

    def saveImageFile(self):
        """Save the contents of the image_label to file."""
        save_file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", os.getenv('HOME'),
                                                        "JPEG (*.jpeg);;JPG (*.jpg);;PNG (*.png);;Bitmap (*.bmp)")

        if save_file_path and self.image_label.pixmap() is not None:
            # TODO: Save the processed image to save_file_path
            cv2.imwrite(save_file_path, self.cv_image)
           # if save_file_path.endswith('.jpge'):
            #notepad_text = self.cv_image.()
            #with open(file_name, 'w') as f:
            #    f.write(notepad_text)
                
           # print(123)
            #elif file_name.endswith('.html'):
            #notepad_richtext = self.text_field.toHtml()
            #with open(file_name, 'w') as f:
            #    f.write(notepad_richtext)
            #


            pass
        else:
            QMessageBox.information(self, "Error",
                                    "Unable to save image.", QMessageBox.Ok)

    def convertCVToQImage(self, image):
        """Load a cv image and convert the image to a Qt QImage. Display the image in image_label."""
        cv_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get the shape of the image, height * width * channels. BGR/RGB/HSV images have 3 channels
        height, width, channels = cv_image.shape  # Format: (rows, columns, channels)
        # Number of bytes required by the image pixels in a row; dependency on the number of channels
        bytes_per_line = width * channels
        # Create instance of QImage using data from cv_image
        converted_Qt_image = QImage(cv_image, width, height, bytes_per_line, QImage.Format_RGB888)

        self.image_label.setPixmap(QPixmap.fromImage(converted_Qt_image).scaled(
            self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = ImageProcessingGUI()
    sys.exit(app.exec_())
