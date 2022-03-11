from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

class perfilDeUsuario():
    def __init__(self, db_ui):
        self.db_ui = db_ui

    def perfilUiShow(self):
        perfil_ui = QUiLoader().load('DB/perfil.ui', self.db_ui.stage)
        perfil_ui.show()
            
    def buttonDown(self, state):
        self.state = state
        self.db_ui.aListaDeUsuarios.setAutoExclusive(self.state)
        self.db_ui.bBackUp.setAutoExclusive(self.state)
        self.db_ui.cEditarPerfil.setAutoExclusive(self.state)
        self.db_ui.dRegistrarUsuario.setAutoExclusive(self.state)