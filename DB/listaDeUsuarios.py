from PySide2.QtWidgets import (
    QWidget, QLineEdit, QScrollArea, QMainWindow,
    QApplication, QVBoxLayout, QSpacerItem, QSizePolicy
    )
from PySide2.QtUiTools import (QUiLoader)
import DB.conexion as conexion

class listaDeUsuarios():
    def __init__(self, db_ui):
        self.db_ui = db_ui

    def crea_tabla(self):
        consulta = '''CREATE TABLE IF NOT EXISTS user 
        (
            ID INT PRIMARY KEY NOT NULL, 
            FNAME TEXT CHAR (50),  
            LNAME TEXT CHAR (50), 
            DNI TEXT  CHAR (50) 
        );'''
        self.version = conexion.RegistroDatos(consulta)
        self.version.close()

    def buttonDown(self, state):
        self.state = state
        self.db_ui.Eliminar_btn.setAutoExclusive(self.state)
        self.db_ui.BackUp_btn.setAutoExclusive(self.state)
        self.db_ui.Editar_btn.setAutoExclusive(self.state)
        self.db_ui.Registrar_btn.setAutoExclusive(self.state)
    """
    def consultarUsuarios(self):
        consulta = '''SELECT * FROM user;'''
        self.usuarios = conexion.RegistroDatos(consulta)
        self.usuarios.close()
    
        
    def NombreDeUsuarios(self):
        listaDeUsuarios = ["Juan Martin Alvarez","Juan Gasulla","Ricardo Telleria"]
        return listaDeUsuarios
    """
    def NombreDeUsuarios(self):
        consulta = '''SELECT * FROM user;'''
        consultaUsuarios = conexion.RegistroDatos(consulta)
        return consultaUsuarios.listado()
    
    def Dni(self):
        listaDni = ["29592521","25365365","15365365"]
        return listaDni
    
    def userUiShow(self, listaDeUsuario, listaDni):
        usuarios_ui = QUiLoader().load('DB/listaDeUsuarios.ui', self.db_ui.stage)
        #usuarios_ui.searchbar = QLineEdit()
        #usuarios_ui.searchbar.textChanged.connect(self.textChanged)
        usuarios_ui.listaDeUsuarios.addItems(listaDeUsuario)
        usuarios_ui.listaDni.addItems(listaDni)
        #usuarios_ui.listaDni.addItems(listaDni)
        usuarios_ui.show()

    def textChanged(self):
        print("textChanged")


