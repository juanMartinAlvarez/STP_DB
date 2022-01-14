from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.listaDeUsuarios as usuarios

class DB():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self = parent

        self.usuarios_widget = QtWidgets.QWidget()
        loader = QUiLoader()
        self.usuarios_ui = loader.load('DB/listaDeUsuarios.ui', self.usuarios_widget)
        self.VBox.addWidget(self.DB_widget,5)
        self.VBox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.VBox)
        self.setFixedWidth(1360)
        self.setFixedHeight(680)
        

    def listaDeUsuarios(self):
        print("listaDeUsuarios")
        self.parent.DB_ui.bBackUp.setEnabled(False)
        self.parent.DB_ui.cEditarPerfil.setEnabled(False)
        self.parent.DB_ui.dRegistrarUsuario.setEnabled(False)
        self.usuarios = usuarios.listaDeUsuarios(self)
        #users = usuarios.listaDeUsuarios()

    def backUp(self):
        print("Back up")

    def editarPerfil(self):
        print("Editar Perfil")

    def registrarUsusario(self):
        print("Registrar Usuario")

    def salir(self):
        print("Salir DB")
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.EjerEvalButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.DB_widget.setParent(None)
        self.parent.setFixedHeight(100)
        

        
