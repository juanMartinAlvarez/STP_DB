from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.listaDeUsuarios as usuarios


class DB():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.usuarios_widget = QtWidgets.QWidget()
        loader = QUiLoader()
        self.usuarios_ui = loader.load('DB/listaDeUsuarios.ui', self.usuarios_widget)
        self.parent.VBox.addWidget(self.parent.DB_widget,5)
        self.parent.VBox.setContentsMargins(0, 0, 0, 0)
        self.parent.setLayout(self.parent.VBox)
        self.parent.setFixedWidth(1360)
        self.parent.setFixedHeight(680)
        self.usuarios = usuarios.listaDeUsuarios(self, self.parent.DB_ui)
        
        

    def listaDeUsuarios(self):
        print("listaDeUsuarios")
        self.parent.DB_ui.bBackUp.setEnabled(False)
        self.parent.DB_ui.cEditarPerfil.setEnabled(False)
        self.parent.DB_ui.dRegistrarUsuario.setEnabled(False)
        
        #users = usuarios.listaDeUsuarios()

    def backUp(self):
        print("Back up")

    def editarPerfil(self):
        print("Editar Perfil")

    def registrarUsusario(self):
        print("Registrar Usuario")

    def salir(self):
        print("Salir DB")
        self.parent.DB_ui.bBackUp.setEnabled(True)
        self.parent.DB_ui.cEditarPerfil.setEnabled(True)
        self.parent.DB_ui.dRegistrarUsuario.setEnabled(True)
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.EjerEvalButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.DB_widget.setParent(None)
        self.parent.setFixedHeight(100)
        

        
