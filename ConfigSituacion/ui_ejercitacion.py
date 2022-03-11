# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ejercitacion.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Ejercitacion(object):
    def setupUi(self, Ejercitacion):
        if not Ejercitacion.objectName():
            Ejercitacion.setObjectName(u"Ejercitacion")
        Ejercitacion.resize(400, 300)
        self.label = QLabel(Ejercitacion)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 71, 51))
        self.label2 = QLabel(Ejercitacion)
        self.label2.setObjectName(u"label2")
        self.label2.setEnabled(True)
        self.label2.setGeometry(QRect(170, 0, 191, 101))

        self.retranslateUi(Ejercitacion)

        QMetaObject.connectSlotsByName(Ejercitacion)
    # setupUi

    def retranslateUi(self, Ejercitacion):
        Ejercitacion.setWindowTitle(QCoreApplication.translate("Ejercitacion", u"Form", None))
        self.label.setText(QCoreApplication.translate("Ejercitacion", u"TextLabel", None))
        self.label2.setText("")
    # retranslateUi

