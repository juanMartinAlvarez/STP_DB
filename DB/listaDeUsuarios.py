from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

class listaDeUsuarios():
    def __init__(self, parent, db_ui):
        self.parent = parent
        
        self.db_ui = db_ui
        self.db_ui.dRegistrarUsuario.setEnabled(False)
        print("init lista")        
        #parent.parent.VBox.addWidget(self.usuarios_widget,5)
        #parent.VBox.setContentsMargins(0, 0, 0, 0)
        #parent.setLayout(self.VBox)
        #parent.setFixedWidth(1147)
        #parent.setFixedHeight(520)
        #self.DB_widget = QtWidgets.QWidget()
        #self.DB_ui = loader.load('DB/DB.ui', self.DB_widget)
        #self.usuarios_widget = QtWidgets.QWidget()
        #loader = QUiLoader()
        #self.usuarios_ui = loader.load('DB/listaDeUsuarios.ui', self.parent.DB_ui.dConfiguracion)
        
        
