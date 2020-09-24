
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
  
  # Dashboard
  def dashboard(self):
    self.stackedWidget.setCurrentIndex(4)
  
  # Camera on
  def camera_on(self):
    self.stackedWidget.setCurrentIndex(5)
  
  # working
  def working(self):
    self.stackedWidget.setCurrentIndex(6)
  
  #  plates
  def plates(self):
    self.stackedWidget.setCurrentIndex(0)
  
  # history
  def history(self):
    self.stackedWidget.setCurrentIndex(1)
  
  # users
  def users(self):
    self.stackedWidget.setCurrentIndex(2)
  
  # developers
  def developers(self):
    self.stackedWidget.setCurrentIndex(3)
  
  # Camera Stacks Events
  def  detect_video(self):
    self.camera_stacks.setCurrentIndex(1)
  
  def detect_from_photo(self):
    self.camera_stacks.setCurrentIndex(0)
    
  def browse_image(self):
    leaf_image_url = ""
    leaf_image_path = ""
    types = ['png', 'jpg', 'jpeg', 'JPEG', 'JPG']
    try:
      fname = QFileDialog.getOpenFileName()
      pixmap = QPixmap(fname[0])
      ext = fname[0].split(".")
      if ext[1] in types:
        pixmap = pixmap.scaled(610, 410, QtCore.Qt.KeepAspectRatio)
        self.image_for_detection.setPixmap(pixmap)
        # leaf_image_path = fname[0]
      else:
        msg = QMessageBox()
        msg.setWindowTitle("MESSAGE ")
        msg.setText("ERROR! PUT IMAGE,PNG,JPG,JPEG ARE ACCEPTABLE")
        msg.setIcon(QMessageBox.Question)
        msg.exec()
    except e:
      print("Error")
  def find_number(self):
        msg = QMessageBox()
        msg.setWindowTitle("MESSAGE ")
        msg.setText("PROCESSING IMAGE")
        msg.setIcon(QMessageBox.Question)
        msg.exec()

  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1288, 684)
    MainWindow.setWindowOpacity(1.0)
    MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.frame = QtWidgets.QFrame(self.centralwidget)
    self.frame.setGeometry(QtCore.QRect(10, 80, 181, 581))
    self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
    self.frame.setFrameShape(QtWidgets.QFrame.Panel)
    self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame.setObjectName("frame")
    self.leaf_button_2 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_2.setGeometry(QtCore.QRect(10, 80, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_2.setFont(font)
    self.leaf_button_2.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("../icons/security-camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_2.setIcon(icon)
    self.leaf_button_2.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_2.setObjectName("leaf_button_2")
    self.leaf_button_3 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_3.setGeometry(QtCore.QRect(10, 200, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_3.setFont(font)
    self.leaf_button_3.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("../icons/number.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_3.setIcon(icon1)
    self.leaf_button_3.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_3.setObjectName("leaf_button_3")
    self.leaf_button_4 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_4.setGeometry(QtCore.QRect(10, 260, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_4.setFont(font)
    self.leaf_button_4.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("../icons/seo-report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_4.setIcon(icon2)
    self.leaf_button_4.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_4.setObjectName("leaf_button_4")
    self.leaf_button_5 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_5.setGeometry(QtCore.QRect(10, 320, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_5.setFont(font)
    self.leaf_button_5.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap("../icons/user (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_5.setIcon(icon3)
    self.leaf_button_5.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_5.setObjectName("leaf_button_5")
    self.leaf_button_6 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_6.setGeometry(QtCore.QRect(10, 380, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_6.setFont(font)
    self.leaf_button_6.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap("../icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_6.setIcon(icon4)
    self.leaf_button_6.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_6.setObjectName("leaf_button_6")
    self.leaf_button_7 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_7.setGeometry(QtCore.QRect(10, 140, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_7.setFont(font)
    self.leaf_button_7.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap("../icons/system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_7.setIcon(icon5)
    self.leaf_button_7.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_7.setObjectName("leaf_button_7")
    self.leaf_button_8 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_8.setGeometry(QtCore.QRect(10, 440, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_8.setFont(font)
    self.leaf_button_8.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap("../icons/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_8.setIcon(icon6)
    self.leaf_button_8.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_8.setObjectName("leaf_button_8")
    self.leaf_button_9 = QtWidgets.QPushButton(self.frame)
    self.leaf_button_9.setGeometry(QtCore.QRect(10, 20, 161, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(14)
    font.setBold(True)
    font.setWeight(75)
    self.leaf_button_9.setFont(font)
    self.leaf_button_9.setStyleSheet("border:1px solid black;\n"
                                     "background-color: rgb(0, 255, 0);")
    icon7 = QtGui.QIcon()
    icon7.addPixmap(QtGui.QPixmap("../icons/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.leaf_button_9.setIcon(icon7)
    self.leaf_button_9.setIconSize(QtCore.QSize(60, 35))
    self.leaf_button_9.setObjectName("leaf_button_9")
    self.frame_2 = QtWidgets.QFrame(self.centralwidget)
    self.frame_2.setGeometry(QtCore.QRect(10, 10, 1261, 71))
    self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "border-bottom-color: rgb(0, 255, 0);")
    self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
    self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_2.setObjectName("frame_2")
    self.label = QtWidgets.QLabel(self.frame_2)
    self.label.setGeometry(QtCore.QRect(250, 0, 841, 61))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(24)
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setStyleSheet("color: rgb(0, 255, 0);")
    self.label.setFrameShape(QtWidgets.QFrame.Panel)
    self.label.setObjectName("label")
    self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
    self.stackedWidget.setGeometry(QtCore.QRect(200, 80, 1071, 581))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.stackedWidget.setFont(font)
    self.stackedWidget.setStyleSheet("")
    self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
    self.stackedWidget.setObjectName("stackedWidget")
    self.page = QtWidgets.QWidget()
    self.page.setObjectName("page")
    self.label_4 = QtWidgets.QLabel(self.page)
    self.label_4.setGeometry(QtCore.QRect(180, 180, 351, 51))
    self.label_4.setObjectName("label_4")
    self.label_17 = QtWidgets.QLabel(self.page)
    self.label_17.setGeometry(QtCore.QRect(10, 20, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_17.setFont(font)
    self.label_17.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_17.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_17.setObjectName("label_17")
    self.stackedWidget.addWidget(self.page)
    self.page_4 = QtWidgets.QWidget()
    self.page_4.setObjectName("page_4")
    self.label_5 = QtWidgets.QLabel(self.page_4)
    self.label_5.setGeometry(QtCore.QRect(250, 220, 351, 51))
    self.label_5.setObjectName("label_5")
    self.label_18 = QtWidgets.QLabel(self.page_4)
    self.label_18.setGeometry(QtCore.QRect(10, 20, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_18.setFont(font)
    self.label_18.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_18.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_18.setObjectName("label_18")
    self.stackedWidget.addWidget(self.page_4)
    self.page_5 = QtWidgets.QWidget()
    self.page_5.setObjectName("page_5")
    self.label_3 = QtWidgets.QLabel(self.page_5)
    self.label_3.setGeometry(QtCore.QRect(160, 200, 351, 51))
    self.label_3.setObjectName("label_3")
    self.label_19 = QtWidgets.QLabel(self.page_5)
    self.label_19.setGeometry(QtCore.QRect(10, 20, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_19.setFont(font)
    self.label_19.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_19.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_19.setObjectName("label_19")
    self.stackedWidget.addWidget(self.page_5)
    self.page_6 = QtWidgets.QWidget()
    self.page_6.setObjectName("page_6")
    self.label_20 = QtWidgets.QLabel(self.page_6)
    self.label_20.setGeometry(QtCore.QRect(10, 20, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_20.setFont(font)
    self.label_20.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_20.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_20.setObjectName("label_20")
    self.stackedWidget.addWidget(self.page_6)
    self.page_2 = QtWidgets.QWidget()
    self.page_2.setObjectName("page_2")
    self.label_7 = QtWidgets.QLabel(self.page_2)
    self.label_7.setGeometry(QtCore.QRect(10, 40, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_7.setFont(font)
    self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "color: rgb(0, 255, 0);")
    self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_7.setObjectName("label_7")
    self.frame_3 = QtWidgets.QFrame(self.page_2)
    self.frame_3.setGeometry(QtCore.QRect(40, 110, 311, 91))
    self.frame_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "")
    self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_3.setObjectName("frame_3")
    self.total_plates = QtWidgets.QLabel(self.frame_3)
    self.total_plates.setGeometry(QtCore.QRect(10, 10, 291, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.total_plates.setFont(font)
    self.total_plates.setStyleSheet("color: rgb(0, 255, 0);")
    self.total_plates.setAlignment(QtCore.Qt.AlignCenter)
    self.total_plates.setObjectName("total_plates")
    self.frame_4 = QtWidgets.QFrame(self.page_2)
    self.frame_4.setGeometry(QtCore.QRect(360, 110, 321, 91))
    self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "\n"
                               "")
    self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_4.setObjectName("frame_4")
    self.correct_results = QtWidgets.QLabel(self.frame_4)
    self.correct_results.setGeometry(QtCore.QRect(10, 10, 301, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.correct_results.setFont(font)
    self.correct_results.setStyleSheet("color: rgb(0, 255, 0);")
    self.correct_results.setAlignment(QtCore.Qt.AlignCenter)
    self.correct_results.setObjectName("correct_results")
    self.frame_5 = QtWidgets.QFrame(self.page_2)
    self.frame_5.setGeometry(QtCore.QRect(690, 110, 331, 91))
    self.frame_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "")
    self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_5.setObjectName("frame_5")
    self.incorrect_results = QtWidgets.QLabel(self.frame_5)
    self.incorrect_results.setGeometry(QtCore.QRect(30, 10, 261, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.incorrect_results.setFont(font)
    self.incorrect_results.setStyleSheet("color: rgb(0, 255, 0);")
    self.incorrect_results.setAlignment(QtCore.Qt.AlignCenter)
    self.incorrect_results.setObjectName("incorrect_results")
    self.frame_6 = QtWidgets.QFrame(self.page_2)
    self.frame_6.setGeometry(QtCore.QRect(40, 210, 311, 91))
    self.frame_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "")
    self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_6.setObjectName("frame_6")
    self.users = QtWidgets.QLabel(self.frame_6)
    self.users.setGeometry(QtCore.QRect(10, 10, 291, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.users.setFont(font)
    self.users.setStyleSheet("color: rgb(0, 255, 0);\n"
                             "text-align:center;")
    self.users.setAlignment(QtCore.Qt.AlignCenter)
    self.users.setObjectName("users")
    self.frame_7 = QtWidgets.QFrame(self.page_2)
    self.frame_7.setGeometry(QtCore.QRect(360, 210, 321, 91))
    self.frame_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "")
    self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_7.setObjectName("frame_7")
    self.label_13 = QtWidgets.QLabel(self.frame_7)
    self.label_13.setGeometry(QtCore.QRect(10, 10, 301, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_13.setFont(font)
    self.label_13.setStyleSheet("color: rgb(0, 255, 0);")
    self.label_13.setAlignment(QtCore.Qt.AlignCenter)
    self.label_13.setObjectName("label_13")
    self.frame_8 = QtWidgets.QFrame(self.page_2)
    self.frame_8.setGeometry(QtCore.QRect(690, 210, 331, 91))
    self.frame_8.setStyleSheet("background-color: rgb(0, 0, 0);")
    self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
    self.frame_8.setObjectName("frame_8")
    self.counter = QtWidgets.QLabel(self.frame_8)
    self.counter.setGeometry(QtCore.QRect(30, 10, 271, 71))
    font = QtGui.QFont()
    font.setFamily("Ebrima")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.counter.setFont(font)
    self.counter.setStyleSheet("color: rgb(0, 255, 0);")
    self.counter.setAlignment(QtCore.Qt.AlignCenter)
    self.counter.setObjectName("counter")
    self.stackedWidget.addWidget(self.page_2)
    self.page_3 = QtWidgets.QWidget()
    self.page_3.setObjectName("page_3")
    self.label_15 = QtWidgets.QLabel(self.page_3)
    self.label_15.setGeometry(QtCore.QRect(10, 10, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_15.setFont(font)
    self.label_15.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_15.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_15.setObjectName("label_15")
    self.cam_frame = QtWidgets.QFrame(self.page_3)
    self.cam_frame.setGeometry(QtCore.QRect(10, 70, 1051, 481))
    self.cam_frame.setStyleSheet("background-color: rgb(0, 0,0);")
    self.cam_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.cam_frame.setFrameShadow(QtWidgets.QFrame.Plain)
    self.cam_frame.setObjectName("cam_frame")
    self.camera_stacks = QtWidgets.QStackedWidget(self.cam_frame)
    self.camera_stacks.setGeometry(QtCore.QRect(0, 60, 831, 421))
    self.camera_stacks.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "border:1px solid rgb(0, 255, 0);;")
    self.camera_stacks.setFrameShape(QtWidgets.QFrame.Box)
    self.camera_stacks.setObjectName("camera_stacks")
    self.detect_from_image = QtWidgets.QWidget()
    self.detect_from_image.setObjectName("detect_from_image")
    self.camera_stacks.addWidget(self.detect_from_image)
    self.image_for_detection = QtWidgets.QLabel(self.detect_from_image)
    self.image_for_detection.setGeometry(QtCore.QRect(260, 10, 561, 391))
    self.image_for_detection.setObjectName("image_for_detection")
    self.live_mode_2 = QtWidgets.QPushButton(self.detect_from_image)
    self.live_mode_2.setGeometry(QtCore.QRect(20, 120, 221, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.live_mode_2.setFont(font)
    self.live_mode_2.setStyleSheet("border:1px solid black;\n"
                                   "background-color: rgb(0, 255, 0);")
    icon8 = QtGui.QIcon()
    icon8.addPixmap(QtGui.QPixmap("../icons/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.live_mode_2.setIcon(icon8)
    self.live_mode_2.setIconSize(QtCore.QSize(60, 35))
    self.live_mode_2.setObjectName("live_mode_2")

    self.browse_image_2 = QtWidgets.QPushButton(self.detect_from_image)
    self.browse_image_2.setGeometry(QtCore.QRect(20, 190, 221, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.browse_image_2.setFont(font)
    self.browse_image_2.setStyleSheet("border:1px solid black;\n"
                                      "background-color: rgb(0, 255, 0);")
    icon9 = QtGui.QIcon()
    icon9.addPixmap(QtGui.QPixmap("../icons/automation (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.browse_image_2.setIcon(icon9)
    self.browse_image_2.setIconSize(QtCore.QSize(60, 35))
    self.browse_image_2.setObjectName("browse_image_2")

    self.detect_from_video = QtWidgets.QWidget()
    self.detect_from_video.setObjectName("detect_from_video")
    self.camera_stacks.addWidget(self.detect_from_video)

    self.live_video_label = QtWidgets.QLabel(self.detect_from_video)
    self.live_video_label.setGeometry(QtCore.QRect(10, 10, 801, 391))
    self.live_video_label.setObjectName("live_video_label")
    self.camera_stacks.addWidget(self.detect_from_video)

    self.page_10 = QtWidgets.QWidget()
    self.page_10.setObjectName("page_10")
    self.camera_stacks.addWidget(self.page_10)
    self.live_mode = QtWidgets.QPushButton(self.cam_frame)
    self.live_mode.setGeometry(QtCore.QRect(10, 0, 171, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.live_mode.setFont(font)
    self.live_mode.setStyleSheet("border:1px solid black;\n"
                                 "background-color: rgb(0, 255, 0);")
    icon8 = QtGui.QIcon()
    icon8.addPixmap(QtGui.QPixmap("../icons/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.live_mode.setIcon(icon8)
    self.live_mode.setIconSize(QtCore.QSize(60, 35))
    self.live_mode.setObjectName("live_mode")
    self.detect_from_image_2 = QtWidgets.QPushButton(self.cam_frame)
    self.detect_from_image_2.setGeometry(QtCore.QRect(190, 0, 271, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(16)
    font.setBold(True)
    font.setWeight(75)
    self.detect_from_image_2.setFont(font)
    self.detect_from_image_2.setStyleSheet("border:1px solid black;\n"
                                           "background-color: rgb(0, 255, 0);")
    icon9 = QtGui.QIcon()
    icon9.addPixmap(QtGui.QPixmap("../icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.detect_from_image_2.setIcon(icon9)
    self.detect_from_image_2.setIconSize(QtCore.QSize(60, 35))
    self.detect_from_image_2.setObjectName("detect_from_image_2")
    self.label_6 = QtWidgets.QLabel(self.cam_frame)
    self.label_6.setGeometry(QtCore.QRect(840, 220, 191, 41))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(18)
    font.setBold(True)
    font.setWeight(75)
    self.label_6.setFont(font)
    self.label_6.setStyleSheet("color: rgb(0, 255, 0);")
    self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.label_6.setObjectName("label_6")
    self.licence_number_plate = QtWidgets.QLabel(self.cam_frame)
    self.licence_number_plate.setGeometry(QtCore.QRect(840, 260, 201, 71))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(18)
    font.setBold(True)
    font.setWeight(75)
    self.licence_number_plate.setFont(font)
    self.licence_number_plate.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                            "color: rgb(0, 255, 0);")
    self.licence_number_plate.setFrameShape(QtWidgets.QFrame.Panel)
    self.licence_number_plate.setObjectName("licence_number_plate")
    self.cam_frame.raise_()
    self.label_15.raise_()
    self.stackedWidget.addWidget(self.page_3)
    self.page_31 = QtWidgets.QWidget()
    self.page_31.setObjectName("page_31")
    self.label_16 = QtWidgets.QLabel(self.page_31)
    self.label_16.setGeometry(QtCore.QRect(10, 20, 1041, 51))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label_16.setFont(font)
    self.label_16.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                "color: rgb(0, 255, 0);")
    self.label_16.setFrameShape(QtWidgets.QFrame.Panel)
    self.label_16.setObjectName("label_16")
    self.stackedWidget.addWidget(self.page_31)
    self.stackedWidget.raise_()
    self.frame.raise_()
    self.frame_2.raise_()
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)
    
    self.retranslateUi(MainWindow)
    self.stackedWidget.setCurrentIndex(4)
    self.camera_stacks.setCurrentIndex(1)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # Method Event Binding
    self.leaf_button_9.clicked.connect(self.dashboard)
    self.leaf_button_2.clicked.connect(self.camera_on)
    self.leaf_button_7.clicked.connect(self.working)
    self.leaf_button_3.clicked.connect(self.plates)
    self.leaf_button_4.clicked.connect(self.history)
    # self.leaf_button_5.clicked.connect(self.users)
    self.leaf_button_8.clicked.connect(self.developers)
    # Camera Mode
    self.live_mode.clicked.connect(self.detect_video)
    self.detect_from_image_2.clicked.connect(self.detect_from_photo)
    self.live_mode_2.clicked.connect(self.browse_image)
    self.browse_image_2.clicked.connect(self.find_number)
  
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Automatic Licence Number Plate Detection And Recognition"))
    self.leaf_button_2.setText(_translate("MainWindow", "CAMERA ON"))
    self.leaf_button_3.setText(_translate("MainWindow", " PLATES"))
    self.leaf_button_4.setText(_translate("MainWindow", "HISTORY"))
    self.leaf_button_5.setText(_translate("MainWindow", "USERS"))
    self.leaf_button_6.setText(_translate("MainWindow", "LOGOUT"))
    self.leaf_button_7.setText(_translate("MainWindow", "ANATOMY"))
    self.leaf_button_8.setText(_translate("MainWindow", "DEVS"))
    self.leaf_button_9.setText(_translate("MainWindow", "DASHBOARD"))
    self.label.setText(_translate("MainWindow", "Automatic Licence Number Plate Detection And Recognition "))
    self.label_4.setText(_translate("MainWindow", "PLATES"))
    self.label_17.setText(_translate("MainWindow", "SAVED NUMBER PLATES"))
    self.label_5.setText(_translate("MainWindow", "system anatomy"))
    self.label_18.setText(_translate("MainWindow", "RECOGNIZING HISTORY"))
    self.label_3.setText(_translate("MainWindow", "HISTORY"))
    self.label_19.setText(_translate("MainWindow", "USERS"))
    self.label_20.setText(_translate("MainWindow", "DEVELOPERS GLIMPSES"))
    self.label_7.setText(_translate("MainWindow", "DASHBOARD"))
    self.total_plates.setText(_translate("MainWindow", "PLATES 44"))
    self.correct_results.setText(_translate("MainWindow", "CORRECT 44"))
    self.incorrect_results.setText(_translate("MainWindow", "INCORRECT 45"))
    self.users.setText(_translate("MainWindow", "USERS 3"))
    self.label_13.setText(_translate("MainWindow", "EEEEEEEEEEEEEE00"))
    self.counter.setText(_translate("MainWindow", "COUNTER 444"))
    self.label_15.setText(_translate("MainWindow", "CAMERA ON"))
    self.live_mode.setText(_translate("MainWindow", "LIVE MODE"))
    self.detect_from_image_2.setText(_translate("MainWindow", "DETECT FROM IMAGE"))
    self.label_6.setText(_translate("MainWindow", "LICENCE PLATE"))
    self.licence_number_plate.setText(_translate("MainWindow", "EE-0345"))
    self.label_16.setText(_translate("MainWindow", "SYSTEM ANATOMY"))
    self.live_mode_2.setText(_translate("MainWindow", "BROWSE IMAGE"))
    self.browse_image_2.setText(_translate("MainWindow", "DETECT NUMBER"))


if __name__ == "__main__":
  import sys
  
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())
