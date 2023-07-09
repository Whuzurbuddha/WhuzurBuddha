# -*- coding: utf-8 -*-

######################################
##                                  ##
##                                  ##
## Written by: Qt Alexander Päplow  ##
##                                  ##
##                                  ##
######################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from show_audio_info import show_audio_info
from show_gpu_info import show_gpu_info
from show_cpu_info import show_cpu_info
from show_storage_info import show_storage_info

class Ui_Hardwarecomponents(object):
    def setupUi(self, Hardwarecomponents):
        if not Hardwarecomponents.objectName():
            Hardwarecomponents.setObjectName(u"Hardwarecomponents")
        Hardwarecomponents.resize(1342, 870)
        Hardwarecomponents.setAutoFillBackground(False)
        self.audioButton = QPushButton(Hardwarecomponents)
        self.audioButton.setObjectName(u"audioButton")
        self.audioButton.setGeometry(QRect(0, 10, 127, 44))
        self.audioButton.setCheckable(False)
        self.cpuButton = QPushButton(Hardwarecomponents)
        self.cpuButton.setObjectName(u"cpuButton")
        self.cpuButton.setGeometry(QRect(0, 60, 127, 44))
        self.gpuButton = QPushButton(Hardwarecomponents)
        self.gpuButton.setObjectName(u"gpuButton")
        self.gpuButton.setGeometry(QRect(0, 110, 127, 44))
        self.textBrowser = QTextBrowser(Hardwarecomponents)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(140, 10, 1191, 851))
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setAutoFormatting(QTextEdit.AutoAll)
        self.storageButton = QPushButton(Hardwarecomponents)
        self.storageButton.setObjectName(u"storageButton")
        self.storageButton.setGeometry(QRect(0, 160, 127, 44))

        self.retranslateUi(Hardwarecomponents)

        QMetaObject.connectSlotsByName(Hardwarecomponents)
        self.audioButton.clicked.connect(self.show_audio_info)
        self.cpuButton.clicked.connect(self.show_cpu_info)
        self.gpuButton.clicked.connect(self.show_gpu_info)
        self.storageButton.clicked.connect(self.show_storage_info)

    def retranslateUi(self, Hardwarecomponents):
        Hardwarecomponents.setWindowTitle(QCoreApplication.translate("Hardwarecomponents", u"Hardware components", None))
        self.audioButton.setText(QCoreApplication.translate("Hardwarecomponents", u"Audio", None))
        self.cpuButton.setText(QCoreApplication.translate("Hardwarecomponents", u"CPU", None))
        self.gpuButton.setText(QCoreApplication.translate("Hardwarecomponents", u"GPU", None))
        self.storageButton.setText(QCoreApplication.translate("Hardwarecomponents", u"Storage", None))

    def show_audio_info(self):
        audio_info = str("Audio info:" + "\n\n" + show_audio_info())
        self.textBrowser.setText(audio_info)

    def show_cpu_info(self):
        cpu_info = str("CPU info:" + "\n\n" + show_cpu_info())
        self.textBrowser.setText(cpu_info)

    def show_gpu_info(self):
        gpu_info = str("GPU info:" + "\n\n" + show_gpu_info())
        self.textBrowser.setText(gpu_info)

    def show_storage_info(self):
        storage_info = str("Storage info:" + "\n\n" + show_storage_info()) 
        self.textBrowser.setText(storage_info)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Hardwarecomponents = QMainWindow()
    ui = Ui_Hardwarecomponents()
    ui.setupUi(Hardwarecomponents)
    Hardwarecomponents.show()
    sys.exit(app.exec_())
