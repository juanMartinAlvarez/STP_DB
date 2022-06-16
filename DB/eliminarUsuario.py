from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.conexion as conexion
#import DB.DB as DBfunc


class eliminarUsuario():
    def __init__(self, db_ui):
        self.db_ui = db_ui
        self.eliminarUsuario_ui = QUiLoader().load('DB/eliminarUsuario.ui', self.db_ui.stage)
        self.eliminarUsuario_ui.btn_eliminar.clicked.connect(self.select_user_to_del)
        #self.eliminarUsuario_ui.btn_Volver.clicked.connect(DBfunc.DB.listaDeUsuarios())  
          
    def buttonDown(self, state):
        self.state = state
        self.db_ui.Registrar_btn.setAutoExclusive(self.state)
        self.db_ui.Eliminar_btn.setAutoExclusive(self.state)
        self.db_ui.Editar_btn.setAutoExclusive(self.state)
        self.db_ui.BackUp_btn.setAutoExclusive(self.state)

    def erase_user(self, user):
        self.user= str(user)
        consulta = '''DELETE FROM user WHERE dni = {}'''.format(self.user)
        self.erase = conexion.RegistroDatos(consulta)
        self.erase.close()


    def select_user_to_del(self):
        self.dni = self.eliminarUsuario_ui.qle_DNI.text()
        print('-------'+ str(self.dni) +'-----------')
        self.erase_user('\"' + self.dni + '\"')

    def delUserUiShow(self):
        self.eliminarUsuario_ui.show()