# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calibracion.ui',
# licensing of 'ui_calibracion.ui' applies.
#
# Created: Fri Feb 14 11:32:06 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Calibracion(object):
    def setupUi(self, Calibracion):
        Calibracion.setObjectName("Calibracion")
        Calibracion.resize(400, 300)
        self.label = QtWidgets.QLabel(Calibracion)
        self.label.setGeometry(QtCore.QRect(0, 0, 62, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Calibracion)
        QtCore.QMetaObject.connectSlotsByName(Calibracion)

    def retranslateUi(self, Calibracion):
        Calibracion.setWindowTitle(QtWidgets.QApplication.translate("Calibracion", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Calibracion", "TextLabel", None, -1))

