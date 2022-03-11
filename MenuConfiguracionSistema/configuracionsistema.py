# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfiguracionSistema.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import RecursosSTPUI_rc

class Ui_Configuracion(object):
    def setupUi(self, Configuracion):
        if not Configuracion.objectName():
            Configuracion.setObjectName(u"Configuracion")
        Configuracion.resize(1360, 635)
        Configuracion.setMinimumSize(QSize(1360, 635))
        Configuracion.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 40, 50);\n"
"	background-color: #232F3E;\n"
"}\n"
"QComboBox{\n"
"    border: 2px solid  rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"   alignment: AlignRight;\n"
"}\n"
"QLineEdit{\n"
"    border: 2px solid  rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"   alignment: AlignRight;\n"
"}")
        self.pushButtonSalir = QPushButton(Configuracion)
        self.pushButtonSalir.setObjectName(u"pushButtonSalir")
        self.pushButtonSalir.setGeometry(QRect(1336, 3, 20, 20))
        self.pushButtonSalir.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Imagnes MainSTP/MyIconos/icono Salir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSalir.setIcon(icon)
        self.pushButtonSalir.setIconSize(QSize(20, 20))
        self.labelConfiguracionGeneralSist = QLabel(Configuracion)
        self.labelConfiguracionGeneralSist.setObjectName(u"labelConfiguracionGeneralSist")
        self.labelConfiguracionGeneralSist.setGeometry(QRect(20, 30, 1341, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.labelConfiguracionGeneralSist.sizePolicy().hasHeightForWidth())
        self.labelConfiguracionGeneralSist.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelConfiguracionGeneralSist.setFont(font)
        self.labelConfiguracionGeneralSist.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(40, 50, 70);\n"
"")
        self.labelConfiguracionGeneralSist.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget = QWidget(Configuracion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 100, 1211, 478))
        self.gridLayoutSistema = QGridLayout(self.layoutWidget)
        self.gridLayoutSistema.setObjectName(u"gridLayoutSistema")
        self.gridLayoutSistema.setHorizontalSpacing(20)
        self.gridLayoutSistema.setVerticalSpacing(8)
        self.gridLayoutSistema.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.label_9, 3, 6, 1, 1)

        self.labelPuntosX = QLabel(self.layoutWidget)
        self.labelPuntosX.setObjectName(u"labelPuntosX")
        sizePolicy1.setHeightForWidth(self.labelPuntosX.sizePolicy().hasHeightForWidth())
        self.labelPuntosX.setSizePolicy(sizePolicy1)
        self.labelPuntosX.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelPuntosX, 2, 6, 1, 1)

        self.labelCamara = QLabel(self.layoutWidget)
        self.labelCamara.setObjectName(u"labelCamara")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelCamara.setFont(font1)
        self.labelCamara.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.gridLayoutSistema.addWidget(self.labelCamara, 10, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSistema.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.labelAnchoPantalla = QLabel(self.layoutWidget)
        self.labelAnchoPantalla.setObjectName(u"labelAnchoPantalla")
        sizePolicy1.setHeightForWidth(self.labelAnchoPantalla.sizePolicy().hasHeightForWidth())
        self.labelAnchoPantalla.setSizePolicy(sizePolicy1)
        self.labelAnchoPantalla.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelAnchoPantalla, 8, 1, 1, 1)

        self.labelDistCamaraProyector = QLabel(self.layoutWidget)
        self.labelDistCamaraProyector.setObjectName(u"labelDistCamaraProyector")
        sizePolicy1.setHeightForWidth(self.labelDistCamaraProyector.sizePolicy().hasHeightForWidth())
        self.labelDistCamaraProyector.setSizePolicy(sizePolicy1)
        self.labelDistCamaraProyector.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelDistCamaraProyector, 12, 1, 1, 1)

        self.lineTiempoLaserOn = QLineEdit(self.layoutWidget)
        self.lineTiempoLaserOn.setObjectName(u"lineTiempoLaserOn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineTiempoLaserOn.sizePolicy().hasHeightForWidth())
        self.lineTiempoLaserOn.setSizePolicy(sizePolicy2)
        self.lineTiempoLaserOn.setMinimumSize(QSize(100, 0))
        self.lineTiempoLaserOn.setMaximumSize(QSize(100, 16777215))
        self.lineTiempoLaserOn.setLayoutDirection(Qt.LeftToRight)
        self.lineTiempoLaserOn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineTiempoLaserOn, 1, 2, 1, 1)

        self.lineEscalaResultado = QLineEdit(self.layoutWidget)
        self.lineEscalaResultado.setObjectName(u"lineEscalaResultado")
        sizePolicy2.setHeightForWidth(self.lineEscalaResultado.sizePolicy().hasHeightForWidth())
        self.lineEscalaResultado.setSizePolicy(sizePolicy2)
        self.lineEscalaResultado.setMinimumSize(QSize(100, 0))
        self.lineEscalaResultado.setMaximumSize(QSize(100, 16777215))
        self.lineEscalaResultado.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineEscalaResultado, 5, 2, 1, 1)

        self.lineTiempoEntreDisparos = QLineEdit(self.layoutWidget)
        self.lineTiempoEntreDisparos.setObjectName(u"lineTiempoEntreDisparos")
        sizePolicy2.setHeightForWidth(self.lineTiempoEntreDisparos.sizePolicy().hasHeightForWidth())
        self.lineTiempoEntreDisparos.setSizePolicy(sizePolicy2)
        self.lineTiempoEntreDisparos.setMinimumSize(QSize(100, 0))
        self.lineTiempoEntreDisparos.setMaximumSize(QSize(100, 16777215))
        self.lineTiempoEntreDisparos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineTiempoEntreDisparos, 3, 2, 1, 1)

        self.comboResolucionCamara = QComboBox(self.layoutWidget)
        self.comboResolucionCamara.setObjectName(u"comboResolucionCamara")
        sizePolicy2.setHeightForWidth(self.comboResolucionCamara.sizePolicy().hasHeightForWidth())
        self.comboResolucionCamara.setSizePolicy(sizePolicy2)
        self.comboResolucionCamara.setMinimumSize(QSize(100, 0))
        self.comboResolucionCamara.setMaximumSize(QSize(100, 16777215))
        self.comboResolucionCamara.setLayoutDirection(Qt.LeftToRight)
        self.comboResolucionCamara.setStyleSheet(u"")

        self.gridLayoutSistema.addWidget(self.comboResolucionCamara, 10, 2, 1, 1)

        self.lineDistCamaraProyector = QLineEdit(self.layoutWidget)
        self.lineDistCamaraProyector.setObjectName(u"lineDistCamaraProyector")
        sizePolicy2.setHeightForWidth(self.lineDistCamaraProyector.sizePolicy().hasHeightForWidth())
        self.lineDistCamaraProyector.setSizePolicy(sizePolicy2)
        self.lineDistCamaraProyector.setMinimumSize(QSize(100, 0))
        self.lineDistCamaraProyector.setMaximumSize(QSize(100, 16777215))
        self.lineDistCamaraProyector.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineDistCamaraProyector, 12, 2, 1, 1)

        self.labelCantPulsosDisparoFalso = QLabel(self.layoutWidget)
        self.labelCantPulsosDisparoFalso.setObjectName(u"labelCantPulsosDisparoFalso")
        sizePolicy1.setHeightForWidth(self.labelCantPulsosDisparoFalso.sizePolicy().hasHeightForWidth())
        self.labelCantPulsosDisparoFalso.setSizePolicy(sizePolicy1)
        self.labelCantPulsosDisparoFalso.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelCantPulsosDisparoFalso, 4, 1, 1, 1)

        self.lineAnchoPantalla = QLineEdit(self.layoutWidget)
        self.lineAnchoPantalla.setObjectName(u"lineAnchoPantalla")
        sizePolicy2.setHeightForWidth(self.lineAnchoPantalla.sizePolicy().hasHeightForWidth())
        self.lineAnchoPantalla.setSizePolicy(sizePolicy2)
        self.lineAnchoPantalla.setMinimumSize(QSize(100, 0))
        self.lineAnchoPantalla.setMaximumSize(QSize(100, 16777215))
        self.lineAnchoPantalla.setLayoutDirection(Qt.LeftToRight)
        self.lineAnchoPantalla.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineAnchoPantalla, 8, 2, 1, 1)

        self.comboCantidadTiradores = QComboBox(self.layoutWidget)
        self.comboCantidadTiradores.setObjectName(u"comboCantidadTiradores")
        sizePolicy2.setHeightForWidth(self.comboCantidadTiradores.sizePolicy().hasHeightForWidth())
        self.comboCantidadTiradores.setSizePolicy(sizePolicy2)
        self.comboCantidadTiradores.setMinimumSize(QSize(100, 0))
        self.comboCantidadTiradores.setMaximumSize(QSize(100, 16777215))
        self.comboCantidadTiradores.setStyleSheet(u"")

        self.gridLayoutSistema.addWidget(self.comboCantidadTiradores, 6, 2, 1, 1)

        self.lineDisTiradorPantalla = QLineEdit(self.layoutWidget)
        self.lineDisTiradorPantalla.setObjectName(u"lineDisTiradorPantalla")
        sizePolicy2.setHeightForWidth(self.lineDisTiradorPantalla.sizePolicy().hasHeightForWidth())
        self.lineDisTiradorPantalla.setSizePolicy(sizePolicy2)
        self.lineDisTiradorPantalla.setMinimumSize(QSize(100, 0))
        self.lineDisTiradorPantalla.setMaximumSize(QSize(100, 16777215))
        self.lineDisTiradorPantalla.setLayoutDirection(Qt.LeftToRight)
        self.lineDisTiradorPantalla.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineDisTiradorPantalla, 2, 2, 1, 1)

        self.labelTiempoEntreDisparos = QLabel(self.layoutWidget)
        self.labelTiempoEntreDisparos.setObjectName(u"labelTiempoEntreDisparos")
        sizePolicy1.setHeightForWidth(self.labelTiempoEntreDisparos.sizePolicy().hasHeightForWidth())
        self.labelTiempoEntreDisparos.setSizePolicy(sizePolicy1)
        self.labelTiempoEntreDisparos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelTiempoEntreDisparos, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayoutSistema.addItem(self.horizontalSpacer, 7, 1, 1, 1)

        self.labelAsistentes = QLabel(self.layoutWidget)
        self.labelAsistentes.setObjectName(u"labelAsistentes")
        self.labelAsistentes.setFont(font1)
        self.labelAsistentes.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.gridLayoutSistema.addWidget(self.labelAsistentes, 0, 4, 1, 1)

        self.labelResolucionProyector = QLabel(self.layoutWidget)
        self.labelResolucionProyector.setObjectName(u"labelResolucionProyector")
        sizePolicy1.setHeightForWidth(self.labelResolucionProyector.sizePolicy().hasHeightForWidth())
        self.labelResolucionProyector.setSizePolicy(sizePolicy1)
        self.labelResolucionProyector.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelResolucionProyector, 14, 1, 1, 1)

        self.lineCantPulsosDisparoFalso = QLineEdit(self.layoutWidget)
        self.lineCantPulsosDisparoFalso.setObjectName(u"lineCantPulsosDisparoFalso")
        sizePolicy2.setHeightForWidth(self.lineCantPulsosDisparoFalso.sizePolicy().hasHeightForWidth())
        self.lineCantPulsosDisparoFalso.setSizePolicy(sizePolicy2)
        self.lineCantPulsosDisparoFalso.setMinimumSize(QSize(100, 0))
        self.lineCantPulsosDisparoFalso.setMaximumSize(QSize(100, 16777215))
        self.lineCantPulsosDisparoFalso.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineCantPulsosDisparoFalso, 4, 2, 1, 1)

        self.labelEscalaResultado = QLabel(self.layoutWidget)
        self.labelEscalaResultado.setObjectName(u"labelEscalaResultado")
        sizePolicy1.setHeightForWidth(self.labelEscalaResultado.sizePolicy().hasHeightForWidth())
        self.labelEscalaResultado.setSizePolicy(sizePolicy1)
        self.labelEscalaResultado.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelEscalaResultado, 5, 1, 1, 1)

        self.labelResolucionCamara = QLabel(self.layoutWidget)
        self.labelResolucionCamara.setObjectName(u"labelResolucionCamara")
        sizePolicy1.setHeightForWidth(self.labelResolucionCamara.sizePolicy().hasHeightForWidth())
        self.labelResolucionCamara.setSizePolicy(sizePolicy1)
        self.labelResolucionCamara.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelResolucionCamara, 10, 1, 1, 1)

        self.lineTiempoExposicion = QLineEdit(self.layoutWidget)
        self.lineTiempoExposicion.setObjectName(u"lineTiempoExposicion")
        sizePolicy2.setHeightForWidth(self.lineTiempoExposicion.sizePolicy().hasHeightForWidth())
        self.lineTiempoExposicion.setSizePolicy(sizePolicy2)
        self.lineTiempoExposicion.setMinimumSize(QSize(100, 0))
        self.lineTiempoExposicion.setMaximumSize(QSize(100, 16777215))
        self.lineTiempoExposicion.setLayoutDirection(Qt.LeftToRight)
        self.lineTiempoExposicion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineTiempoExposicion, 0, 2, 1, 1)

        self.comboResolucionProyector = QComboBox(self.layoutWidget)
        self.comboResolucionProyector.setObjectName(u"comboResolucionProyector")
        sizePolicy2.setHeightForWidth(self.comboResolucionProyector.sizePolicy().hasHeightForWidth())
        self.comboResolucionProyector.setSizePolicy(sizePolicy2)
        self.comboResolucionProyector.setMinimumSize(QSize(100, 0))
        self.comboResolucionProyector.setMaximumSize(QSize(100, 16777215))
        self.comboResolucionProyector.setLayoutDirection(Qt.LeftToRight)
        self.comboResolucionProyector.setStyleSheet(u"alignment: AlignRight;")

        self.gridLayoutSistema.addWidget(self.comboResolucionProyector, 14, 2, 1, 1)

        self.lineCuadrosPorSegundo = QLineEdit(self.layoutWidget)
        self.lineCuadrosPorSegundo.setObjectName(u"lineCuadrosPorSegundo")
        sizePolicy2.setHeightForWidth(self.lineCuadrosPorSegundo.sizePolicy().hasHeightForWidth())
        self.lineCuadrosPorSegundo.setSizePolicy(sizePolicy2)
        self.lineCuadrosPorSegundo.setMinimumSize(QSize(100, 0))
        self.lineCuadrosPorSegundo.setMaximumSize(QSize(100, 16777215))
        self.lineCuadrosPorSegundo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineCuadrosPorSegundo, 11, 2, 1, 1)

        self.labelCuadrosPorSegundo = QLabel(self.layoutWidget)
        self.labelCuadrosPorSegundo.setObjectName(u"labelCuadrosPorSegundo")
        sizePolicy1.setHeightForWidth(self.labelCuadrosPorSegundo.sizePolicy().hasHeightForWidth())
        self.labelCuadrosPorSegundo.setSizePolicy(sizePolicy1)
        self.labelCuadrosPorSegundo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelCuadrosPorSegundo, 11, 1, 1, 1)

        self.labelSistema = QLabel(self.layoutWidget)
        self.labelSistema.setObjectName(u"labelSistema")
        self.labelSistema.setFont(font1)
        self.labelSistema.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.gridLayoutSistema.addWidget(self.labelSistema, 0, 0, 1, 1)

        self.labelPantalla = QLabel(self.layoutWidget)
        self.labelPantalla.setObjectName(u"labelPantalla")
        self.labelPantalla.setFont(font1)
        self.labelPantalla.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.gridLayoutSistema.addWidget(self.labelPantalla, 8, 0, 1, 1)

        self.labelTiempoExposicion = QLabel(self.layoutWidget)
        self.labelTiempoExposicion.setObjectName(u"labelTiempoExposicion")
        sizePolicy1.setHeightForWidth(self.labelTiempoExposicion.sizePolicy().hasHeightForWidth())
        self.labelTiempoExposicion.setSizePolicy(sizePolicy1)
        self.labelTiempoExposicion.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelTiempoExposicion, 0, 1, 1, 1)

        self.labelCalibCamaraProy = QLabel(self.layoutWidget)
        self.labelCalibCamaraProy.setObjectName(u"labelCalibCamaraProy")
        sizePolicy1.setHeightForWidth(self.labelCalibCamaraProy.sizePolicy().hasHeightForWidth())
        self.labelCalibCamaraProy.setSizePolicy(sizePolicy1)
        self.labelCalibCamaraProy.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelCalibCamaraProy, 0, 5, 1, 1)

        self.labelCantidadTiradores = QLabel(self.layoutWidget)
        self.labelCantidadTiradores.setObjectName(u"labelCantidadTiradores")
        sizePolicy1.setHeightForWidth(self.labelCantidadTiradores.sizePolicy().hasHeightForWidth())
        self.labelCantidadTiradores.setSizePolicy(sizePolicy1)
        self.labelCantidadTiradores.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelCantidadTiradores, 6, 1, 1, 1)

        self.labelTiempoLaserOn = QLabel(self.layoutWidget)
        self.labelTiempoLaserOn.setObjectName(u"labelTiempoLaserOn")
        sizePolicy1.setHeightForWidth(self.labelTiempoLaserOn.sizePolicy().hasHeightForWidth())
        self.labelTiempoLaserOn.setSizePolicy(sizePolicy1)
        self.labelTiempoLaserOn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelTiempoLaserOn, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSistema.addItem(self.horizontalSpacer_2, 13, 1, 1, 1)

        self.labelProyector = QLabel(self.layoutWidget)
        self.labelProyector.setObjectName(u"labelProyector")
        self.labelProyector.setFont(font1)
        self.labelProyector.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.gridLayoutSistema.addWidget(self.labelProyector, 14, 0, 1, 1)

        self.labelDistTiradorPantalla = QLabel(self.layoutWidget)
        self.labelDistTiradorPantalla.setObjectName(u"labelDistTiradorPantalla")
        sizePolicy1.setHeightForWidth(self.labelDistTiradorPantalla.sizePolicy().hasHeightForWidth())
        self.labelDistTiradorPantalla.setSizePolicy(sizePolicy1)
        self.labelDistTiradorPantalla.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelDistTiradorPantalla, 2, 1, 1, 1)

        self.lineEditAnchoBorde = QLineEdit(self.layoutWidget)
        self.lineEditAnchoBorde.setObjectName(u"lineEditAnchoBorde")
        self.lineEditAnchoBorde.setMinimumSize(QSize(100, 0))
        self.lineEditAnchoBorde.setMaximumSize(QSize(100, 16777215))
        self.lineEditAnchoBorde.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineEditAnchoBorde, 4, 7, 1, 1)

        self.pushGuardarConfiguracion = QPushButton(self.layoutWidget)
        self.pushGuardarConfiguracion.setObjectName(u"pushGuardarConfiguracion")
        self.pushGuardarConfiguracion.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.pushGuardarConfiguracion.setFont(font2)
        self.pushGuardarConfiguracion.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(180, 0, 0);")

        self.gridLayoutSistema.addWidget(self.pushGuardarConfiguracion, 0, 9, 1, 1)

        self.linePuntosCuadriculaEnX = QLineEdit(self.layoutWidget)
        self.linePuntosCuadriculaEnX.setObjectName(u"linePuntosCuadriculaEnX")
        sizePolicy2.setHeightForWidth(self.linePuntosCuadriculaEnX.sizePolicy().hasHeightForWidth())
        self.linePuntosCuadriculaEnX.setSizePolicy(sizePolicy2)
        self.linePuntosCuadriculaEnX.setMinimumSize(QSize(100, 0))
        self.linePuntosCuadriculaEnX.setMaximumSize(QSize(100, 16777215))
        self.linePuntosCuadriculaEnX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.linePuntosCuadriculaEnX, 2, 7, 1, 1)

        self.labelPresCuadricula = QLabel(self.layoutWidget)
        self.labelPresCuadricula.setObjectName(u"labelPresCuadricula")
        sizePolicy1.setHeightForWidth(self.labelPresCuadricula.sizePolicy().hasHeightForWidth())
        self.labelPresCuadricula.setSizePolicy(sizePolicy1)
        self.labelPresCuadricula.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelPresCuadricula, 2, 5, 1, 1)

        self.lineEdiTDiametrodePuntos = QLineEdit(self.layoutWidget)
        self.lineEdiTDiametrodePuntos.setObjectName(u"lineEdiTDiametrodePuntos")
        self.lineEdiTDiametrodePuntos.setMinimumSize(QSize(100, 0))
        self.lineEdiTDiametrodePuntos.setMaximumSize(QSize(100, 16777215))
        self.lineEdiTDiametrodePuntos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutSistema.addWidget(self.lineEdiTDiametrodePuntos, 3, 7, 1, 1)

        self.labelAnchoBorde = QLabel(self.layoutWidget)
        self.labelAnchoBorde.setObjectName(u"labelAnchoBorde")
        sizePolicy1.setHeightForWidth(self.labelAnchoBorde.sizePolicy().hasHeightForWidth())
        self.labelAnchoBorde.setSizePolicy(sizePolicy1)
        self.labelAnchoBorde.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelAnchoBorde, 4, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSistema.addItem(self.horizontalSpacer_3, 9, 1, 1, 1)

        self.pushCalibracionAutomatica = QPushButton(self.layoutWidget)
        self.pushCalibracionAutomatica.setObjectName(u"pushCalibracionAutomatica")
        sizePolicy2.setHeightForWidth(self.pushCalibracionAutomatica.sizePolicy().hasHeightForWidth())
        self.pushCalibracionAutomatica.setSizePolicy(sizePolicy2)
        self.pushCalibracionAutomatica.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.pushCalibracionAutomatica.setFont(font3)
        self.pushCalibracionAutomatica.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(55, 60, 80);")

        self.gridLayoutSistema.addWidget(self.pushCalibracionAutomatica, 0, 6, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSistema.addItem(self.horizontalSpacer_4, 0, 8, 1, 1)

        self.labelRegPosicionCamara = QLabel(self.layoutWidget)
        self.labelRegPosicionCamara.setObjectName(u"labelRegPosicionCamara")
        sizePolicy1.setHeightForWidth(self.labelRegPosicionCamara.sizePolicy().hasHeightForWidth())
        self.labelRegPosicionCamara.setSizePolicy(sizePolicy1)
        self.labelRegPosicionCamara.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayoutSistema.addWidget(self.labelRegPosicionCamara, 8, 5, 1, 1)

        self.pushCapturaContinua = QPushButton(self.layoutWidget)
        self.pushCapturaContinua.setObjectName(u"pushCapturaContinua")
        sizePolicy2.setHeightForWidth(self.pushCapturaContinua.sizePolicy().hasHeightForWidth())
        self.pushCapturaContinua.setSizePolicy(sizePolicy2)
        self.pushCapturaContinua.setMinimumSize(QSize(0, 30))
        self.pushCapturaContinua.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(55, 60, 80);")

        self.gridLayoutSistema.addWidget(self.pushCapturaContinua, 8, 6, 1, 2)

        self.pushProyectarCuadricula = QPushButton(self.layoutWidget)
        self.pushProyectarCuadricula.setObjectName(u"pushProyectarCuadricula")
        self.pushProyectarCuadricula.setMinimumSize(QSize(0, 30))
        self.pushProyectarCuadricula.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(55, 60, 80);")

        self.gridLayoutSistema.addWidget(self.pushProyectarCuadricula, 5, 6, 1, 2)


        self.retranslateUi(Configuracion)
        self.pushButtonSalir.clicked.connect(Configuracion.close)

        QMetaObject.connectSlotsByName(Configuracion)
    # setupUi

    def retranslateUi(self, Configuracion):
        Configuracion.setWindowTitle(QCoreApplication.translate("Configuracion", u"Configuracion General", None))
        self.pushButtonSalir.setText("")
        self.labelConfiguracionGeneralSist.setText(QCoreApplication.translate("Configuracion", u"Configuraci\u00f3n General del Sistema", None))
        self.label_9.setText(QCoreApplication.translate("Configuracion", u"Diametro de puntos", None))
        self.labelPuntosX.setText(QCoreApplication.translate("Configuracion", u"Puntos en X", None))
        self.labelCamara.setText(QCoreApplication.translate("Configuracion", u"Camara", None))
        self.labelAnchoPantalla.setText(QCoreApplication.translate("Configuracion", u"Ancho Pantalla [m]", None))
        self.labelDistCamaraProyector.setText(QCoreApplication.translate("Configuracion", u"Distancia Camara Proyector", None))
        self.labelCantPulsosDisparoFalso.setText(QCoreApplication.translate("Configuracion", u"Cant. Pulsos disparo falso", None))
        self.labelTiempoEntreDisparos.setText(QCoreApplication.translate("Configuracion", u"Tiempo entre disparos [ms]", None))
        self.labelAsistentes.setText(QCoreApplication.translate("Configuracion", u"Asistentes", None))
        self.labelResolucionProyector.setText(QCoreApplication.translate("Configuracion", u"Resoluci\u00f3n Proyector", None))
        self.labelEscalaResultado.setText(QCoreApplication.translate("Configuracion", u"Escala Resultado", None))
        self.labelResolucionCamara.setText(QCoreApplication.translate("Configuracion", u"Resoluci\u00f3n Camara", None))
        self.labelCuadrosPorSegundo.setText(QCoreApplication.translate("Configuracion", u"Cuadros por segundo", None))
        self.labelSistema.setText(QCoreApplication.translate("Configuracion", u"Sistema", None))
        self.labelPantalla.setText(QCoreApplication.translate("Configuracion", u"Pantalla", None))
        self.labelTiempoExposicion.setText(QCoreApplication.translate("Configuracion", u"Tiempo de Exposici\u00f3n", None))
        self.labelCalibCamaraProy.setText(QCoreApplication.translate("Configuracion", u"Calibraci\u00f3n Camara-Proyector", None))
        self.labelCantidadTiradores.setText(QCoreApplication.translate("Configuracion", u"Cantidad de Tiradores", None))
        self.labelTiempoLaserOn.setText(QCoreApplication.translate("Configuracion", u"Tiempo Laser ON [us]", None))
        self.labelProyector.setText(QCoreApplication.translate("Configuracion", u"Proyector", None))
        self.labelDistTiradorPantalla.setText(QCoreApplication.translate("Configuracion", u"Distancia Tirador Pantalla", None))
        self.pushGuardarConfiguracion.setText(QCoreApplication.translate("Configuracion", u"Guardar Configuraci\u00f3n", None))
        self.labelPresCuadricula.setText(QCoreApplication.translate("Configuracion", u"Presentaci\u00f3n Cuadricula", None))
        self.labelAnchoBorde.setText(QCoreApplication.translate("Configuracion", u"Ancho borde", None))
        self.pushCalibracionAutomatica.setText(QCoreApplication.translate("Configuracion", u"Calibraci\u00f3n Autom\u00e1tica", None))
        self.labelRegPosicionCamara.setText(QCoreApplication.translate("Configuracion", u"Regular Posici\u00f3n Camara", None))
        self.pushCapturaContinua.setText(QCoreApplication.translate("Configuracion", u"Captura Cont\u00ednua", None))
        self.pushProyectarCuadricula.setText(QCoreApplication.translate("Configuracion", u"Proyectar cuadricula", None))
    # retranslateUi

