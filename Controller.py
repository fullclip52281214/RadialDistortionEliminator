from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
from distortion import Distortion
import cv2
#from math import log

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        #initial value
        self.k1=0
        self.k2=0
        self.k3=0
        self.img=cv2.imread("grid.png")
        self.qimg=self.ImageConvertor(self.img)
        self.ui.ImgDisplay.setPixmap(QPixmap.fromImage(self.qimg))
        self.SliderReset()

    def setup_control(self):
        self.ui.Reset.clicked.connect(self.SliderReset)
        self.ui.OpenFileButton.clicked.connect(self.open_file) 
        self.ui.R2.valueChanged.connect(self.R2change)
        self.ui.R4.valueChanged.connect(self.R4change)
        self.ui.R6.valueChanged.connect(self.R6change)
        self.ui.centx.valueChanged.connect(self.centxchange)
        self.ui.centy.valueChanged.connect(self.centychange)
        self.ui.SaveImg.clicked.connect(self.imageSave)
        
    def SliderReset(self):
        self.centxValue=self.img.shape[1]/2
        self.centyValue=self.img.shape[0]/2
        self.ui.R2.setValue(50)
        self.ui.R4.setValue(50)
        self.ui.R6.setValue(50)
        self.ui.centx.setValue(50)
        self.ui.centy.setValue(50)  

    def ImageConvertor(self,img):
        height, width, channel = img.shape
        bytesPerline = 3 * width
        Qimg=QImage(img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        return Qimg

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                  "Open file",
                  "./")                # start path
        self.img=cv2.imread(filename)
        self.qimg=self.ImageConvertor(self.img)
        self.ui.ImgDisplay.setPixmap(QPixmap.fromImage(self.qimg))
        
    def ValueChange(self):
        distCoeff=(self.k1,self.k2,0,0,self.k3)
        self.outImg=Distortion(self.img, distCoeff,[self.centxValue,self.centyValue])
        self.qimg=self.ImageConvertor(self.outImg)
        self.ui.ImgDisplay.setPixmap(QPixmap.fromImage(self.qimg))
    
    def R2change(self):
        if(self.ui.R2.value()>=50):
            self.k1=5e-6*((self.ui.R2.value()-50)/10)**2
        else:
            self.k1=-5e-6*((50-self.ui.R2.value())/10)**2
        self.ValueChange()
    
    def R4change(self):
        if(self.ui.R4.value()>=50):
            self.k2=5e-9*((self.ui.R4.value()-50)/10)**2
        else:
            self.k2=-5e-9*((50-self.ui.R4.value())/10)**2
        self.ValueChange()
        
    def R6change(self):
        if(self.ui.R6.value()>=50):
            self.k3=5e-12*((self.ui.R6.value()-50)/10)**2
        else:
            self.k3=-5e-12*((50-self.ui.R6.value())/10)**2
        self.ValueChange()
    
    def centxchange(self):
        self.centxValue=self.ui.centx.value()/100*self.img.shape[1]
        self.ValueChange()
    
    def centychange(self):
        self.centyValue=self.ui.centy.value()/100*self.img.shape[0]
        self.ValueChange()
        
    def imageSave(self):
        cv2.imwrite("Output_Image.png",self.outImg)
        
        