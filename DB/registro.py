from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import DB.conexion as conexion


class registroDeUsuario():
    def __init__(self, db_ui):
        self.db_ui = db_ui
        self.registro_ui = QUiLoader().load('DB/registro.ui', self.db_ui.stage)
        self.registro_ui.btn_Agregar.clicked.connect(self.inserta_user_datos)
    
    def buttonDown(self, state):
        self.state = state
        self.db_ui.Eliminar_btn.setAutoExclusive( self.state)
        self.db_ui.BackUp_btn.setAutoExclusive( self.state)
        self.db_ui.Editar_btn.setAutoExclusive( self.state)
        self.db_ui.Registrar_btn.setAutoExclusive( self.state)
    
    def inserta_user_sql(self, nombre, apellido, DNI, unidad):
        consulta = '''INSERT INTO user (nombre, apellido, DNI, unidad) 
        VALUES('{}','{}','{}','{}')'''.format(nombre, apellido, DNI, unidad)
        self.insert = conexion.RegistroDatos(consulta)
        self.insert.close()
        
    def inserta_user_datos(self):
        # Pull data from the qlineedit of the Ui
        nombre = self.registro_ui.addNombre.text()
        apellido = self.registro_ui.addApellido.text()
        DNI = self.registro_ui.addDNI.text()
        unidad = self.registro_ui.addUnidad.text()
        # call function to add data in DB
        self.inserta_user_sql(nombre, apellido, DNI, unidad )
        # reset data from the qlineedit of the Ui
        self.registro_ui.addNombre.clear()
        self.registro_ui.addApellido.clear()
        self.registro_ui.addDNI.clear()
        self.registro_ui.addUnidad.clear()
    
    def registroUiShow(self):
        self.registro_ui.show()

