# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit, QFileDialog
import cv2
import numpy as np
import pytesseract
import io 
from PIL import ImageFont, ImageDraw, Image

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_realimage = QtWidgets.QLabel(self.centralwidget)
        self.label_realimage.setGeometry(QtCore.QRect(10, 20, 561, 611))
        self.label_realimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_realimage.setObjectName("label_realimage")
        self.label_resultimage = QtWidgets.QLabel(self.centralwidget)
        self.label_resultimage.setGeometry(QtCore.QRect(610, 20, 561, 611))
        self.label_resultimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultimage.setObjectName("label_resultimage")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 650, 581, 211))
        self.groupBox.setObjectName("groupBox")
        self.btn_chooseimage = QtWidgets.QPushButton(self.groupBox)
        self.btn_chooseimage.setGeometry(QtCore.QRect(120, 90, 121, 23))
        self.btn_chooseimage.setObjectName("btn_chooseimage")
         
        self.btn_boundingboxes = QtWidgets.QPushButton(self.groupBox)
        self.btn_boundingboxes.setGeometry(QtCore.QRect(120, 150, 121, 23))
        self.btn_boundingboxes.setObjectName("btn_boundingboxes")
        self.btn_generatetext = QtWidgets.QPushButton(self.groupBox)
        self.btn_generatetext.setGeometry(QtCore.QRect(350, 90, 121, 23))
        self.btn_generatetext.setObjectName("btn_generatetext")
        self.btn_translate = QtWidgets.QPushButton(self.groupBox)
        self.btn_translate.setGeometry(QtCore.QRect(350, 150, 121, 23))
        self.btn_translate.setObjectName("btn_translate")
        self.btn_proceed = QtWidgets.QPushButton(self.groupBox)
        self.btn_proceed.setGeometry(QtCore.QRect(150, 40, 251, 23))
        self.btn_proceed.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_proceed.setCheckable(False)
        self.btn_proceed.setDefault(False)
        self.btn_proceed.setFlat(False)
        self.btn_proceed.setObjectName("btn_proceed")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 111, 16))
        self.label_3.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(360, 120, 141, 16))
        self.label_4.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 180, 121, 16))
        self.label_5.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(130, 180, 111, 16))
        self.label_6.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_6.setObjectName("label_6")
        self.spinBox_fontsize = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_fontsize.setGeometry(QtCore.QRect(470, 40, 42, 22))
        self.spinBox_fontsize.setProperty("value", 15)
        self.spinBox_fontsize.setObjectName("spinBox_fontsize")
        self.spinBox_fontsize.valueChanged.connect(self.fontchanged)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(420, 40, 41, 21))
        self.label_7.setStyleSheet("font: 25 8pt \"Segoe UI Light\";")
        self.label_7.setObjectName("label_7")
        self.textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit.setGeometry(QtCore.QRect(650, 660, 531, 201))
        self.textedit.setObjectName("textedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filepath = ""
        self.fontsize = 15
        self.text = ""
        self.image = None
        self.resultimage = None
        self.btn_chooseimage.clicked.connect(self.showDialog)
        self.btn_proceed.clicked.connect(self.generateText)
        self.btn_generatetext.clicked.connect(self.assignText)
        self.btn_boundingboxes.clicked.connect(self.generatBoundingBox)
        self.btn_translate.clicked.connect(self.translateText)

        self.btn_boundingboxes.setDisabled(True)
        self.btn_generatetext.setDisabled(True)
        self.btn_translate.setDisabled(True)

    

    def showDialog(self):
        options = QFileDialog.Options()
        fname, ok = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Image Files (*.jpg *.png *.jpeg *.PNG)", options=options)
        if ok:
            self.filepath = fname
            self.show_image()
            self.btn_boundingboxes.setDisabled(False)
            self.btn_generatetext.setDisabled(False)
            self.btn_translate.setDisabled(False)
        else:
            self.disperrmessage("FileName Error", "Please choos an image again.")
    
    def fontchanged(self):
        self.fontsize = int(self.spinBox_fontsize.value())

    def generateText(self):
        if len(self.filepath) > 0:
            self.text = ""
            img = cv2.imread(self.filepath)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgh, imgw = grey.shape
            self.resultimage = np.zeros((imgh, imgw, 3), np.uint8)
            text = pytesseract.image_to_data(img, lang="amh")
            imgpil = Image.fromarray(self.resultimage)
            draw = ImageDraw.Draw(imgpil)
            font = ImageFont.truetype(".\AbyssinicaSIL-Regular.ttf", self.fontsize)

            for x, i in enumerate(text.splitlines()):
                if x != 0 and len(i.split()) == 12:
                    i = i.split()
                    self.text += i[11] + " "
                    x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
                    draw.text((x,y), i[11], fill=(255,255,255,0), font=font)


            self.resultimage = np.array(imgpil)
            self.show_resultimage()
        else:
            self.disperrmessage("Idle image Error" , "Please choose an image first")

    def translateText(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This feature not available for this version")
        msg.setWindowTitle("Feature")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def disperrmessage(self, tittle, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(tittle)
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def generatBoundingBox(self):
        if len(self.filepath) > 0:
            img = cv2.imread(self.filepath)
            text = pytesseract.image_to_data(img, lang="amh")
            for x, i in enumerate(text.splitlines()):
                
                if x != 0 and len(i.split()) == 12:
                    i = i.split()
                    x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
            
            cv2.imshow("Bounding boxes", img)
        else:
            self.disperrmessage("Idle image Error" , "Please choose an image first")

    def assignText(self):
        if len(self.filepath) > 0:
            fontdb = QFontDatabase()
            fontdb.addApplicationFont(".\\AbyssinicaSIL-Regular.ttf")
            font  = QFont("Abyssinica SIL", 10, 1)
            self.textedit.setFont(font)
            self.textedit.setText(self.text)
        else:
            self.disperrmessage("Idle image Error" , "Please choose an image first")

    @QtCore.pyqtSlot()
    def show_image(self):
        self.image = cv2.imread(self.filepath)
        self.image = cv2.resize(self.image, (500,800))
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_realimage.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label_realimage.setScaledContents(True)
        

    @QtCore.pyqtSlot()
    def show_resultimage(self):
        self.resultimage = cv2.resize(self.resultimage, (500,800))
        self.resultimage = QtGui.QImage(self.resultimage.data, self.resultimage.shape[1], self.resultimage.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_resultimage.setPixmap(QtGui.QPixmap.fromImage(self.resultimage))
        self.label_resultimage.setScaledContents(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amharic OCR"))
        self.label_realimage.setText(_translate("MainWindow", "Real Image"))
        self.label_resultimage.setText(_translate("MainWindow", "Result image"))
        self.groupBox.setTitle(_translate("MainWindow", "ToolBox"))
        self.btn_chooseimage.setText(_translate("MainWindow", "Choose image"))
        self.btn_boundingboxes.setText(_translate("MainWindow", "Bounding boxes"))
        self.btn_generatetext.setText(_translate("MainWindow", "Generat text"))
        self.btn_translate.setText(_translate("MainWindow", "Translate to English"))
        self.btn_proceed.setText(_translate("MainWindow", "Proceed"))
        self.label_3.setText(_translate("MainWindow", "choose image from file"))
        self.label_4.setText(_translate("MainWindow", "Generate text from image"))
        self.label_5.setText(_translate("MainWindow", "Translate text to English"))
        self.label_6.setText(_translate("MainWindow", "Show areas with texts"))
        self.label_7.setText(_translate("MainWindow", "Font size"))




app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())