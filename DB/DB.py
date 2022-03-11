from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.listaDeUsuarios as usuarios
import DB.backUp as backUp
import DB.perfil as perfil
import DB.registro as registro

class DB():
    def __init__(self, parent):
        self.parent = parent
        #--- Set Vertical Box
        self.parent.VBox.addWidget(self.parent.DB_widget,5)
        self.parent.VBox.setContentsMargins(0, 0, 0, 0)
        #---Set Layout 
        self.parent.setLayout(self.parent.VBox)
        self.parent.setFixedWidth(1360)
        self.parent.setFixedHeight(680)
        #-Initialize classes listaDeUsuarios BackUp perfil registro 
        self.usuarios = usuarios.listaDeUsuarios(self.parent.DB_ui)
        self.bkUp = backUp.backUp(self.parent.DB_ui)
        self.perfil = perfil.perfilDeUsuario(self.parent.DB_ui)
        self.registro = registro.registroDeUsuario(self.parent.DB_ui)

    def listaDeUsuarios(self):
        self.usuarios.buttonDown(True)
        listaDeUsuarios = self.usuarios.NombreDeUsuarios()
        listaDeDni = self.usuarios.Dni()
        self.usuarios.userUiShow(listaDeUsuarios, listaDeDni)


    def backUp(self):
        self.bkUp.buttonDown(True)
        self.bkUp.bkUpUiShow()

    def editarPerfil(self):
        self.perfil.buttonDown(True)
        self.perfil.perfilUiShow()
        
    def registrarUsusario(self):
        self.registro.buttonDown(True)
        self.registro.registroUiShow()
        
    def salir(self):
        #-Reset butttons Main Menu        
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.EjerEvalButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        #-Reset butttons Data Base
        self.parent.DB_ui.aListaDeUsuarios.setChecked(False)
        self.parent.DB_ui.bBackUp.setChecked(False)
        self.parent.DB_ui.cEditarPerfil.setChecked(False)
        self.parent.DB_ui.dRegistrarUsuario.setChecked(False)
        self.parent.DB_widget.setParent(None)
        #-Fix window
        self.parent.setFixedHeight(100)
        

        
