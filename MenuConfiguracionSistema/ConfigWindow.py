#from PyQt5 import QtWidgets, uic
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader


import MenuConfiguracionSistema.configuracionsistema as configuracionsistema
import MenuConfiguracionSistema.ui_calibracion as ui_calibracion

class configwindow(QtWidgets.QWidget, configuracionsistema.Ui_Configuracion):
    
    def __init__(self, parent, screen, socket_madst, udp_madst):
        super().__init__()
        pass