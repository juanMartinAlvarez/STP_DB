from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.listaDeUsuarios as mostrar
import DB.backUp as backUp
import DB.perfilDeUsuario as editar
import DB.registro as login

class DB():
    def __init__(self, parent):
        self.parent = parent
        #-- pyside settings
        #--- Set Vertical Box
        self.parent.VBox.addWidget(self.parent.DB_widget,5)
        self.parent.VBox.setContentsMargins(0, 0, 0, 0)
        #---Set Layout 
        self.parent.setLayout(self.parent.VBox)
        self.parent.setFixedWidth(1360)
        self.parent.setFixedHeight(680)

        #-Initialize classes
        self.usuarios = mostrar.listaDeUsuarios(self.parent.DB_ui)
        self.registro = login.registroDeUsuario(self.parent.DB_ui)
        
        self.perfil = editar.perfilDeUsuario(self.parent.DB_ui)
        self.bkUp = backUp.backUp(self.parent.DB_ui)

    def listaDeUsuarios(self):
        self.usuarios.buttonDown(True)
        self.usuarios.crea_tabla()
        listaDeUsuarios = self.usuarios.NombreDeUsuarios()
        listaDeDni = self.usuarios.Dni()
        self.usuarios.userUiShow(listaDeUsuarios, listaDeDni)
   
    def registrarUsusario(self):
        self.registro.buttonDown(True)
        self.registro.registroUiShow()
    
    def editarPerfil(self):
        self.perfil.buttonDown(True)
        self.perfil.perfilUiShow()

    def backUp(self):
        self.bkUp.buttonDown(True)
        self.bkUp.bkUpUiShow()

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
        
