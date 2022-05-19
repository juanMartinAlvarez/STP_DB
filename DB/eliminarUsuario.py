from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

class eliminarUsuario():
    def __init__(self, db_ui):
        self.db_ui = db_ui

    def perfilUiShow(self):
        perfil_ui = QUiLoader().load('DB/eliminarUsuario.ui', self.db_ui.stage)
        perfil_ui.show()
            
    def buttonDown(self, state):
        self.state = state
        self.db_ui.Registrar_btn.setAutoExclusive(self.state)
        self.db_ui.Eliminar_btn.setAutoExclusive(self.state)
        self.db_ui.Editar_btn.setAutoExclusive(self.state)
        self.db_ui.BackUp_btn.setAutoExclusive(self.state)
