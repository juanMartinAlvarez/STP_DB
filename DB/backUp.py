from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

class backUp():
    def __init__(self, db_ui):
        self.db_ui = db_ui
    
    def bkUpUiShow(self):
        backUp_ui = QUiLoader().load('DB/backUp.ui', self.db_ui.stage)
        backUp_ui.show()
        
    def buttonDown(self, state):
        self.state = state
        self.db_ui.aListaDeUsuarios.setAutoExclusive(self.state)
        self.db_ui.bBackUp.setAutoExclusive(self.state)
        self.db_ui.cEditarPerfil.setAutoExclusive(self.state)
        self.db_ui.dRegistrarUsuario.setAutoExclusive(self.state)