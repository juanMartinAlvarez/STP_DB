# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuCtrlVisualizacion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import RecursosSTPUI_rc

class Ui_CtrlVisualizacion(object):
    def setupUi(self, CtrlVisualizacion):
        if not CtrlVisualizacion.objectName():
            CtrlVisualizacion.setObjectName(u"CtrlVisualizacion")
        CtrlVisualizacion.resize(652, 275)
        self.label = QLabel(CtrlVisualizacion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 60, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label_2 = QLabel(CtrlVisualizacion)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 210, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.comboBox = QComboBox(CtrlVisualizacion)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 50, 231, 31))
        self.Marcha = QToolButton(CtrlVisualizacion)
        self.Marcha.setObjectName(u"Marcha")
        self.Marcha.setGeometry(QRect(280, 210, 50, 50))
        self.Marcha.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Player/MyIconos/IconoPlay2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Marcha.setIcon(icon)
        self.Marcha.setIconSize(QSize(21, 21))
        self.Marcha.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolButton_3 = QToolButton(CtrlVisualizacion)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(350, 210, 50, 50))
        self.toolButton_3.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Player/MyIconos/IconPause2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QSize(21, 21))
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.horizontalSlider = QSlider(CtrlVisualizacion)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(140, 180, 391, 31))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.comboBox_2 = QComboBox(CtrlVisualizacion)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(570, 130, 61, 31))
        self.label_3 = QLabel(CtrlVisualizacion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 130, 151, 31))
        self.label_3.setFont(font)
        self.comboBox_3 = QComboBox(CtrlVisualizacion)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(140, 90, 231, 31))
        self.label_5 = QLabel(CtrlVisualizacion)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 111, 31))
        self.label_5.setFont(font)
        self.label_6 = QLabel(CtrlVisualizacion)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 130, 60, 31))
        self.label_6.setFont(font)
        self.comboBox_4 = QComboBox(CtrlVisualizacion)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(140, 130, 231, 31))
        self.label_8 = QLabel(CtrlVisualizacion)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(400, 90, 71, 31))
        self.label_8.setFont(font)
        self.pushButton_7 = QPushButton(CtrlVisualizacion)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(600, 90, 30, 30))
        self.pushButton_7.setStyleSheet(u"")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(20, 20))
        self.pushButton_8 = QPushButton(CtrlVisualizacion)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(570, 90, 30, 30))
        self.pushButton_8.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Player/MyIconos/IconoPlay3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.label_9 = QLabel(CtrlVisualizacion)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(400, 50, 141, 31))
        self.label_9.setFont(font)
        self.checkBox = QCheckBox(CtrlVisualizacion)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(540, 60, 18, 18))
        self.pushButton_9 = QPushButton(CtrlVisualizacion)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(630, 10, 20, 20))
        self.pushButton_9.setStyleSheet(u"border-image: url(:/Player/MyIconos/IconoCruz.png);")
        self.Parada = QToolButton(CtrlVisualizacion)
        self.Parada.setObjectName(u"Parada")
        self.Parada.setGeometry(QRect(210, 210, 50, 50))
        self.Parada.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Player/MyIconos/IconoInicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Parada.setIcon(icon3)
        self.Parada.setIconSize(QSize(20, 20))
        self.Parada.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.Parada_2 = QToolButton(CtrlVisualizacion)
        self.Parada_2.setObjectName(u"Parada_2")
        self.Parada_2.setGeometry(QRect(420, 210, 50, 50))
        self.Parada_2.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Player/MyIconos/IconoFinal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Parada_2.setIcon(icon4)
        self.Parada_2.setIconSize(QSize(20, 20))
        self.Parada_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.retranslateUi(CtrlVisualizacion)

        QMetaObject.connectSlotsByName(CtrlVisualizacion)
    # setupUi

    def retranslateUi(self, CtrlVisualizacion):
        CtrlVisualizacion.setWindowTitle(QCoreApplication.translate("CtrlVisualizacion", u"Form", None))
        self.label.setText(QCoreApplication.translate("CtrlVisualizacion", u"Situacion", None))
        self.label_2.setText(QCoreApplication.translate("CtrlVisualizacion", u"Control de Visualizacion", None))
        self.Marcha.setText(QCoreApplication.translate("CtrlVisualizacion", u"Marcha", None))
        self.toolButton_3.setText(QCoreApplication.translate("CtrlVisualizacion", u"Parada", None))
        self.label_3.setText(QCoreApplication.translate("CtrlVisualizacion", u"Velocidad Reproduccion", None))
        self.label_5.setText(QCoreApplication.translate("CtrlVisualizacion", u"N` Linea/Tirador", None))
        self.label_6.setText(QCoreApplication.translate("CtrlVisualizacion", u"Arma", None))
        self.label_8.setText(QCoreApplication.translate("CtrlVisualizacion", u"Impactos", None))
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.label_9.setText(QCoreApplication.translate("CtrlVisualizacion", u"Curva de Seguimiento", None))
        self.checkBox.setText("")
        self.pushButton_9.setText("")
        self.Parada.setText(QCoreApplication.translate("CtrlVisualizacion", u"Inicio", None))
        self.Parada_2.setText(QCoreApplication.translate("CtrlVisualizacion", u"Inicio", None))
    # retranslateUi

