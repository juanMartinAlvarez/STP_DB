from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QTableWidgetItem
import DB.listaDeUsuarios as mostrar
import DB.registro as login
import DB.eliminarUsuario as eliminar
import DB.perfilDeUsuario as editar
import DB.backUp as backUp

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
        self.eliminar = eliminar.eliminarUsuario(self.parent.DB_ui)
        self.perfil = editar.perfilDeUsuario(self.parent.DB_ui)
        self.bkUp = backUp.backUp(self.parent.DB_ui)
        self.listaDeUsuarios()

    def listaDeUsuarios(self):
        self.usuarios.buttonDown(True)
        self.usuarios.crea_tabla()
        dbUser = self.usuarios.allUsers()
        self.usuarios.fillTable(dbUser)
        self.usuarios.userUiShow()

    def registrarUsusario(self):
        
        self.registro.buttonDown(True)
        #self.usuarios.crea_tabla()
        self.registro.registroUiShow()
        

    def eliminarUsuario(self):
        
        self.eliminar.buttonDown(True)
        self.eliminar.delUserUiShow()
        
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
        self.parent.DB_ui.Eliminar_btn.setChecked(False)
        self.parent.DB_ui.BackUp_btn.setChecked(False)
        self.parent.DB_ui.Editar_btn.setChecked(False)
        self.parent.DB_ui.Registrar_btn.setChecked(False)
        self.parent.DB_widget.setParent(None)
        #-Fix window
        self.parent.setFixedHeight(100)
        
