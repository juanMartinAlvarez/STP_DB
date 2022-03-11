from PySide2.QtWidgets import (
    QWidget, QLineEdit, QScrollArea, QMainWindow,
    QApplication, QVBoxLayout, QSpacerItem, QSizePolicy
    )
from PySide2.QtUiTools import (QUiLoader)

class listaDeUsuarios():
    def __init__(self, db_ui):
        self.db_ui = db_ui

    def buttonDown(self, state):
        self.state = state
        self.db_ui.aListaDeUsuarios.setAutoExclusive(self.state)
        self.db_ui.bBackUp.setAutoExclusive(self.state)
        self.db_ui.cEditarPerfil.setAutoExclusive(self.state)
        self.db_ui.dRegistrarUsuario.setAutoExclusive(self.state)

    def NombreDeUsuarios(self):
        listaDeUsuarios = ["Juan Martin Alvarez","Juan Gasulla","Ricardo Telleria"]
        return listaDeUsuarios

    def Dni(self):
        listaDni = ["29592521","25365365","15365365"]
        return listaDni
    
    def userUiShow(self, listaDeUsuario, listaDni):
        usuarios_ui = QUiLoader().load('DB/listaDeUsuarios.ui', self.db_ui.stage)
        #usuarios_ui.searchbar = QLineEdit()
        #usuarios_ui.searchbar.textChanged.connect(self.textChanged)
        usuarios_ui.listaDeUsuarios.addItems(listaDeUsuario)
        usuarios_ui.listaDni.addItems(listaDni)
        usuarios_ui.show()

    def textChanged(self):
        print("textChanged")


