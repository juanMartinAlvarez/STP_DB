from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import MenuCtrlVisualizacion.MenuCtrlVisualizacion as menuctrlvisualizacion
import MenuCtrlVisualizacion.RecursosSTPUI

class reproduccionwindow(QtWidgets.QWidget, menuctrlvisualizacion.Ui_CtrlVisualizacion):
    
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        
        self.parent = parent
        self.button_connections()
        
        
    def button_connections(self):
        #self.pushGuardar.clicked.connect(self.Guardar)
        pass
        
    def Guardar(self):
        print ("guardar")

    def closeEvent(self, event):
        print("Close")
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.EjerEvalButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)

