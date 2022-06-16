from PySide2.QtUiTools import QUiLoader
import DB.conexion as conexion

class perfilDeUsuario():
    def __init__(self, db_ui):
        self.db_ui = db_ui
        self.perfil_ui = QUiLoader().load('DB/perfil.ui', self.db_ui.stage)
        self.perfil_ui.btn_buscar.clicked.connect(self.buscar_datos)
        self.perfil_ui.btn_guardar.clicked.connect(self.insertar_qle_datos)

    def buttonDown(self, state):
        self.state = state
        self.db_ui.Registrar_btn.setAutoExclusive(self.state)
        self.db_ui.Eliminar_btn.setAutoExclusive(self.state)
        self.db_ui.Editar_btn.setAutoExclusive(self.state)
        self.db_ui.BackUp_btn.setAutoExclusive(self.state)
    
    def buscar_datos(self):
        self.dni = self.perfil_ui.qle_search.text()
        consulta = '''SELECT * FROM user WHERE dni = {}'''.format(self.dni)
        self.user = conexion.RegistroDatos(consulta).listado()
        DNI = self.user[0][3]
        nombre = self.user[0][1]
        apellido = self.user[0][2]
        unidad = self.user[0][4]
        #Insert user data in placeholders
        self.perfil_ui.qle_DNI.setText(DNI)
        self.perfil_ui.qle_nombre.setText(nombre)
        self.perfil_ui.qle_apellido.setText( apellido)
        self.perfil_ui.qle_unidad.setText(unidad)

        
    def insertar_qle_datos(self):
        self.dni= self.perfil_ui.qle_search.text()
        DNI= self.perfil_ui.qle_DNI.text()
        nombre= self.perfil_ui.qle_nombre.text()
        apellido = self.perfil_ui.qle_apellido.text()
        unidad = self.perfil_ui.qle_unidad.text()
        
        consulta ='''UPDATE user SET  nombre =' {}' , apellido = '{}', DNI = '{}', unidad = '{}'
        WHERE DNI = '{}' '''.format(nombre, apellido, DNI, unidad, self.dni)

        self.insert = conexion.RegistroDatos(consulta)
        self.insert.close()

    def perfilUiShow(self):
        self.perfil_ui.show()
