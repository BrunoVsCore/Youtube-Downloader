# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout_8.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(707, 321)
        MainWindow.setMinimumSize(QSize(707, 321))
        MainWindow.setMaximumSize(QSize(1000, 400))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/newPrefix/download.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(999999, 16777215))
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setStyleSheet(u"#centralwidget{ background-color: qlineargradient(spread:pad, x1:0.363, y1:0.534, x2:0.028, y2:0.097, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(92, 136, 255, 255));}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Url_icone = QLabel(self.frame)
        self.Url_icone.setObjectName(u"Url_icone")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Url_icone.sizePolicy().hasHeightForWidth())
        self.Url_icone.setSizePolicy(sizePolicy1)
        self.Url_icone.setMinimumSize(QSize(80, 54))
        self.Url_icone.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Url_icone.setFont(font)
        self.Url_icone.setStyleSheet(u"image: url(:/newPrefix/url_icon.ico);")

        self.horizontalLayout.addWidget(self.Url_icone)

        self.lineEdit_Inserir_url = QLineEdit(self.frame)
        self.lineEdit_Inserir_url.setObjectName(u"lineEdit_Inserir_url")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_Inserir_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_Inserir_url.setSizePolicy(sizePolicy2)
        self.lineEdit_Inserir_url.setMinimumSize(QSize(15, 15))
        self.lineEdit_Inserir_url.setMaximumSize(QSize(500, 25))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.lineEdit_Inserir_url.setFont(font1)
        self.lineEdit_Inserir_url.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_Inserir_url.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_Inserir_url.setAutoFillBackground(False)
        self.lineEdit_Inserir_url.setStyleSheet(u"\n"
" border-radius: 8px;\n"
"border: 2px solid rgb(0, 200, 255);")
        self.lineEdit_Inserir_url.setInputMethodHints(Qt.ImhHiddenText)
        self.lineEdit_Inserir_url.setFrame(True)
        self.lineEdit_Inserir_url.setEchoMode(QLineEdit.Normal)
        self.lineEdit_Inserir_url.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_Inserir_url.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_Inserir_url)

        self.botao_colarurl = QPushButton(self.frame)
        self.botao_colarurl.setObjectName(u"botao_colarurl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.botao_colarurl.sizePolicy().hasHeightForWidth())
        self.botao_colarurl.setSizePolicy(sizePolicy3)
        self.botao_colarurl.setMinimumSize(QSize(10, 10))
        self.botao_colarurl.setMaximumSize(QSize(150, 30))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.botao_colarurl.setFont(font2)
        self.botao_colarurl.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.506, x2:0, y2:1, stop:0.511364 rgba(0, 0, 0, 255), stop:1 rgba(0, 116, 133, 255));\n"
"color:#ffffff;\n"
"\n"
"\n"
"border-top-color:4px  rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(150, 150, 150);\n"
"border-bottom-color: rgb(150, 150, 150);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(0, 255, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 1px solid black;\n"
"\n"
"  \n"
"\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.botao_colarurl)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setMinimumSize(QSize(332, 131))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.foto_imagem = QLabel(self.frame_4)
        self.foto_imagem.setObjectName(u"foto_imagem")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.foto_imagem.sizePolicy().hasHeightForWidth())
        self.foto_imagem.setSizePolicy(sizePolicy5)
        self.foto_imagem.setMinimumSize(QSize(125, 0))
        self.foto_imagem.setStyleSheet(u"\n"
"border: 3px solid rgb(0, 200, 255);\n"
"border-radius: 5px;\n"
"color:#ffffff;")

        self.horizontalLayout_3.addWidget(self.foto_imagem)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.nome = QLabel(self.frame_3)
        self.nome.setObjectName(u"nome")
        sizePolicy6.setHeightForWidth(self.nome.sizePolicy().hasHeightForWidth())
        self.nome.setSizePolicy(sizePolicy6)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.nome.setFont(font3)
        self.nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.nome)

        self.download = QLabel(self.frame_3)
        self.download.setObjectName(u"download")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy7)
        self.download.setFont(font3)
        self.download.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.download)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.botao_baixar_musica = QPushButton(self.frame)
        self.botao_baixar_musica.setObjectName(u"botao_baixar_musica")
        sizePolicy7.setHeightForWidth(self.botao_baixar_musica.sizePolicy().hasHeightForWidth())
        self.botao_baixar_musica.setSizePolicy(sizePolicy7)
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.botao_baixar_musica.setFont(font4)
        self.botao_baixar_musica.setFocusPolicy(Qt.ClickFocus)
        self.botao_baixar_musica.setContextMenuPolicy(Qt.PreventContextMenu)
        self.botao_baixar_musica.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.506, x2:0, y2:1, stop:0.511364 rgba(0, 0, 0, 255), stop:1 rgba(0, 116, 133, 255));\n"
"color:#ffffff;\n"
"font-size:15pt;\n"
"\n"
"border-top-color:4px  rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(150, 150, 150);\n"
"border-bottom-color: rgb(150, 150, 150);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(0, 255, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.506, x2:0, y2:1, stop:0.511364 rgba(0, 0, 0, 255), stop:1 rgba(0, 116, 133, 255));\n"
"color:#ffffff;\n"
"font-size:15pt;\n"
"\n"
"\n"
"\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.botao_baixar_musica)

        self.botao_baixar_video = QPushButton(self.frame)
        self.botao_baixar_video.setObjectName(u"botao_baixar_video")
        sizePolicy7.setHeightForWidth(self.botao_baixar_video.sizePolicy().hasHeightForWidth())
        self.botao_baixar_video.setSizePolicy(sizePolicy7)
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.botao_baixar_video.setFont(font5)
        self.botao_baixar_video.setContextMenuPolicy(Qt.PreventContextMenu)
        self.botao_baixar_video.setStyleSheet(u"QPushButton{\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.506, x2:0, y2:1, stop:0.511364 rgba(0, 0, 0, 255), stop:1 rgba(0, 116, 133, 255));\n"
"color:#ffffff;\n"
"font-size:15pt;\n"
"\n"
"border-top-color:4px  rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(150, 150, 150);\n"
"border-bottom-color: rgb(150, 150, 150);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(0, 255, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 2px solid gray;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.506, x2:0, y2:1, stop:0.511364 rgba(0, 0, 0, 255), stop:1 rgba(0, 116, 133, 255));\n"
"color:#ffffff;\n"
"font-size:15pt;\n"
"\n"
"\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.botao_baixar_video)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" Youtube Downloader", None))
        self.Url_icone.setText("")
        self.lineEdit_Inserir_url.setInputMask("")
        self.lineEdit_Inserir_url.setText("")
        self.lineEdit_Inserir_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira a URL", None))
#if QT_CONFIG(tooltip)
        self.botao_colarurl.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">run</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.botao_colarurl.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; color:#00ff00;\">Pesquisar URL</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.botao_colarurl.setText(QCoreApplication.translate("MainWindow", u"Pesquisar URL", None))
        self.foto_imagem.setText("")
        self.nome.setText(QCoreApplication.translate("MainWindow", u" Nome:", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u" Download:", None))
#if QT_CONFIG(whatsthis)
        self.botao_baixar_musica.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Baixar Musica</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.botao_baixar_musica.setText(QCoreApplication.translate("MainWindow", u"Baixar Música", None))
        self.botao_baixar_video.setText(QCoreApplication.translate("MainWindow", u"Baixar Vídeo", None))
    # retranslateUi

