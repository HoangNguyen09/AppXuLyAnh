# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import cv2
import pyautogui
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QFileDialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(251, 248, 241)")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnOpen = QtWidgets.QToolButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(40, 40, 80, 40))
        self.btnOpen.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                   "border-radius: 8px;"
                                   "font: 14pt \"Arial\";")
        self.btnOpen.setObjectName("btnOpen")

        self.btnSave = QtWidgets.QToolButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(160, 40, 80, 40))
        self.btnSave.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                   "border-radius: 8px;"
                                   "font: 14pt \"Arial\";")
        self.btnSave.setObjectName("btnSave")

        self.btnReset = QtWidgets.QToolButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(280, 40, 80, 40))
        self.btnReset.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                    "border-radius: 8px;" 
                                    "font: 14pt \"Arial\";")
        self.btnReset.setObjectName("btnReset")

        self.lblBalanceImage = QtWidgets.QLabel(self.centralwidget)
        self.lblBalanceImage.setGeometry(QtCore.QRect(40, 100, 140, 40))
        self.lblBalanceImage.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 12pt \"Arial\";")
        self.lblBalanceImage.setObjectName("lblBalanceImage")

        self.btnGrayscale = QtWidgets.QToolButton(self.centralwidget)
        self.btnGrayscale.setGeometry(QtCore.QRect(40, 160, 140, 40))
        self.btnGrayscale.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                        "border-radius: 8px;" 
                                        "font: 12pt \"Arial\";")
        self.btnGrayscale.setObjectName("btnGrayscale")

        self.btnReverse = QtWidgets.QToolButton(self.centralwidget)
        self.btnReverse.setGeometry(QtCore.QRect(220, 160, 140, 40))
        self.btnReverse.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                      "border-radius: 8px;"
                                      "font: 12pt \"Arial\";")
        self.btnReverse.setObjectName("btnReverse")

        self.btnGamma = QtWidgets.QToolButton(self.centralwidget)
        self.btnGamma.setGeometry(QtCore.QRect(40, 220, 140, 40))
        self.btnGamma.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                    "border-radius: 8px;"
                                    "font: 12pt \"Arial\";")
        self.btnGamma.setObjectName("btnGamma")

        self.btnHistogram = QtWidgets.QToolButton(self.centralwidget)
        self.btnHistogram.setGeometry(QtCore.QRect(220, 220, 140, 40))
        self.btnHistogram.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                        "border-radius: 8px;"
                                        "font: 12pt \"Arial\";")
        self.btnHistogram.setObjectName("btnHistogram")

        self.btnLogarit = QtWidgets.QToolButton(self.centralwidget)
        self.btnLogarit.setGeometry(QtCore.QRect(40, 280, 140, 40))
        self.btnLogarit.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                      "border-radius: 8px;"
                                      "font: 12pt \"Arial\";")
        self.btnLogarit.setObjectName("btnLogarit")

        self.lblFilterImage = QtWidgets.QLabel(self.centralwidget)
        self.lblFilterImage.setGeometry(QtCore.QRect(40, 340, 140, 40))
        self.lblFilterImage.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 12pt \"Arial\";")
        self.lblFilterImage.setObjectName("lblFilterImage")

        self.btnGaussianFilter = QtWidgets.QToolButton(self.centralwidget)
        self.btnGaussianFilter.setGeometry(QtCore.QRect(40, 400, 140, 40))
        self.btnGaussianFilter.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                             "border-radius: 8px;"
                                             "font: 11pt \"Arial\";")
        self.btnGaussianFilter.setObjectName("btnGaussianFilter")

        self.btnMedianThreshold = QtWidgets.QToolButton(self.centralwidget)
        self.btnMedianThreshold.setGeometry(QtCore.QRect(220, 400, 140, 40))
        self.btnMedianThreshold.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                              "border-radius: 8px;"
                                              "font: 11pt \"Arial\";")
        self.btnMedianThreshold.setObjectName("btnMedianThreshold")

        self.btnBlur = QtWidgets.QToolButton(self.centralwidget)
        self.btnBlur.setGeometry(QtCore.QRect(40, 460, 140, 40))
        self.btnBlur.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                   "border-radius: 8px;"
                                   "font: 11pt \"Arial\";")
        self.btnBlur.setObjectName("btnBlur")

        self.btnMedianFilter = QtWidgets.QToolButton(self.centralwidget)
        self.btnMedianFilter.setGeometry(QtCore.QRect(220, 460, 140, 40))
        self.btnMedianFilter.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                           "border-radius: 8px;"
                                           "font: 11pt \"Arial\";")
        self.btnMedianFilter.setObjectName("btnMedianFilter")

        self.lblZoomImage = QtWidgets.QLabel(self.centralwidget)
        self.lblZoomImage.setGeometry(QtCore.QRect(40, 520, 140, 40))
        self.lblZoomImage.setStyleSheet("color: rgb(0, 0, 0);\n" 
                                   "font: 12pt \"Arial\";")
        self.lblZoomImage.setObjectName("lblZoomImage")

        self.btnZoomIn = QtWidgets.QToolButton(self.centralwidget)
        self.btnZoomIn.setGeometry(QtCore.QRect(40, 580, 140, 40))
        self.btnZoomIn.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                     "border-radius: 8px;" 
                                     "font: 12pt \"Arial\";")
        self.btnZoomIn.setObjectName("btnZoomIn")

        self.btnZoomOut = QtWidgets.QToolButton(self.centralwidget)
        self.btnZoomOut.setGeometry(QtCore.QRect(220, 580, 140, 40))
        self.btnZoomOut.setStyleSheet("background-color: rgb(84, 186, 185);\n"
                                      "border-radius: 8px;" 
                                      "font: 12pt \"Arial\";")
        self.btnZoomOut.setObjectName("btnZoomOut")

        self.lblOriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.lblOriginalImage.setGeometry(QtCore.QRect(540, 40, 80, 30))
        self.lblOriginalImage.setStyleSheet("color: rgb(0, 0, 0);\n" 
                                            "font: 12pt \"Arial\";")
        self.lblOriginalImage.setObjectName("lblOriginalImage")

        self.lblFrameOriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.lblFrameOriginalImage.setGeometry(QtCore.QRect(400, 100, 380, 440))
        self.lblFrameOriginalImage.setStyleSheet("background-color: rgb(84, 186, 185);")
        self.lblFrameOriginalImage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblFrameOriginalImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblFrameOriginalImage.setLineWidth(5)
        self.lblFrameOriginalImage.setText("")
        self.lblFrameOriginalImage.setObjectName("lblFrameOriginalImage")

        self.lblChangeImage = QtWidgets.QLabel(self.centralwidget)
        self.lblChangeImage.setGeometry(QtCore.QRect(970, 40, 131, 31))
        self.lblChangeImage.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "font: 12pt \"Arial\";")
        self.lblChangeImage.setObjectName("lblChangeImage")

        self.lblFrameChangeImage = QtWidgets.QLabel(self.centralwidget)
        self.lblFrameChangeImage.setGeometry(QtCore.QRect(850, 100, 381, 441))
        self.lblFrameChangeImage.setStyleSheet("background-color: rgb(84, 186, 185);")
        self.lblFrameChangeImage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblFrameChangeImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblFrameChangeImage.setLineWidth(5)
        self.lblFrameChangeImage.setText("")
        self.lblFrameChangeImage.setObjectName("lblFrameChangeImage")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Khai bao su kien clicked o day
        self.btnOpen.clicked.connect(self.open_img)
        self.btnSave.clicked.connect(self.save_img)
        self.btnReset.clicked.connect(self.reset_img)


        self.btnGrayscale.clicked.connect(self.anh_Xam)
        self.btnReverse.clicked.connect(self.anh_Invert)
        self.btnLogarit.clicked.connect(self.anh_Log)
        self.btnHistogram.clicked.connect(self.anh_Histogram)
        self.btnGamma.clicked.connect(self.gamma)


        self.btnBlur.clicked.connect(self.blur)
        self.btnMedianFilter.clicked.connect(self.median_filter)
        self.btnGaussianFilter.clicked.connect(self.gaussian_filter)


        self.btnMedianThreshold.clicked.connect(self.median_threshold)


        self.btnZoomOut.clicked.connect(self.zom_in)
        self.btnZoomIn.clicked.connect(self.zom_out)

    def loadImage(self, fname):
        self.image = cv2.imread(fname)
        self.tmp = self.image
        self.displayImage()

    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        img = img.rgbSwapped()
        if window == 1:
            self.lblFrameOriginalImage.setPixmap(QPixmap.fromImage(img))
            self.lblFrameOriginalImage.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.lblFrameOriginalImage.setFixedSize(385, 606)
        if window == 2:
            self.lblFrameChangeImage.setPixmap(QPixmap.fromImage(img))
            self.lblFrameChangeImage.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.lblFrameChangeImage.setFixedSize(385, 606)

    def open_img(self):
        fname, filter = QFileDialog.getOpenFileName(None, 'open', 'C:\\Users')
        print(filter)
        print(fname)
        if fname:
            self.loadImage(fname)
        else:
            pyautogui.alert("Không tìm thấy ảnh")
            print('Không tìm thấy ảnh')

    def save_img(self):
        fname, filter = QFileDialog.getSaveFileName(None, 'save', 'C:\\Users')
        if fname:
            cv2.imwrite(fname, self.image)
            pyautogui.alert("Lưu ảnh thành công")
        else:
            pyautogui.alert("Lưu ảnh không thành công")
            print("Lỗi")

    def zom_out(self):
        self.image = cv2.resize(self.image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)

    def zom_in(self):
        self.image = cv2.resize(self.image, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
        self.displayImage(2)

    def reset_img(self):
        self.image = self.tmp
        self.displayImage(2)
        pyautogui.alert("Reset ảnh thành công")

    def anh_Xam(self):
        self.image = self.tmp
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.displayImage(2)

    def anh_Invert(self):
        self.image = self.tmp
        self.image = ~self.image
        self.displayImage(2)

    def anh_Log(self):
        self.image = self.tmp
        img_2 = np.uint8(np.log(self.image))
        c = 2
        self.image = cv2.threshold(img_2, c, 225, cv2.THRESH_BINARY)[1]
        self.displayImage(2)

    def anh_Histogram(self):
        self.image = self.tmp
        img_yuv = cv2.cvtColor(self.image, cv2.COLOR_RGB2YUV)
        img_yuv[:, 2:, 0] = cv2.equalizeHist(img_yuv[:, 2:, 0])
        self.image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
        self.displayImage(2)

    def anh_Gamma(self, gamma):
        self.image = self.tmp
        gamma = gamma * 0.1
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        self.image = cv2.LUT(self.image, table)
        self.displayImage(2)

    def gamma(self):
        self.image = self.tmp
        gamma = 1.5
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        self.image = cv2.LUT(self.image, table)
        self.displayImage(2)

    def blur(self):
        self.image = self.tmp
        self.image = cv2.blur(self.image, (5, 5))
        self.displayImage(2)



    def median_filter(self):
        self.image = self.tmp
        self.image = cv2.medianBlur(self.image, 5)
        self.displayImage(2)

    def gaussian_filter(self):
        self.image = self.tmp
        self.image = cv2.GaussianBlur(self.image, (5, 5), 0)
        self.displayImage(2)

    def median_threshold(self):
        self.image = self.tmp
        grayscaled = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.medianBlur(self.image, 5)
        retval, threshold = cv2.threshold(grayscaled, 125, 125, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.image = threshold
        self.displayImage(2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XỬ LÝ ẢNH"))
        MainWindow.setWindowIcon(QIcon("logo.png"))
        self.btnOpen.setText(_translate("MainWindow", "Open"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.lblBalanceImage.setText(_translate("MainWindow", "Cân Bằng ảnh"))
        self.btnGrayscale.setText(_translate("MainWindow", "Độ Xám"))
        self.btnReverse.setText(_translate("MainWindow", "Đảo Ngược"))
        self.btnGamma.setText(_translate("MainWindow", "Gamma"))
        self.btnHistogram.setText(_translate("MainWindow", "Histogram"))
        self.btnLogarit.setText(_translate("MainWindow", "Logarit"))
        self.lblFilterImage.setText(_translate("MainWindow", "Lọc Ảnh"))
        self.btnGaussianFilter.setText(_translate("MainWindow", "Gaussian filter"))
        self.btnMedianThreshold.setText(_translate("MainWindow", "Median threshold"))
        self.btnBlur.setText(_translate("MainWindow", "Blur"))
        self.btnMedianFilter.setText(_translate("MainWindow", "Median filter"))
        self.lblZoomImage.setText(_translate("MainWindow", "Zoom Ảnh"))
        self.btnZoomIn.setText(_translate("MainWindow", "Phóng To"))
        self.btnZoomOut.setText(_translate("MainWindow", "Thu Nhỏ"))
        self.lblOriginalImage.setText(_translate("MainWindow", "Ảnh Gốc"))
        self.lblChangeImage.setText(_translate("MainWindow", "Ảnh Biến Đổi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
