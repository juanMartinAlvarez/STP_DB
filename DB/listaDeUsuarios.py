from PySide2.QtWidgets import (QWidget, QTableWidgetItem, QHeaderView, QLineEdit, QScrollArea, QTableWidget, QApplication, QVBoxLayout, QSpacerItem, QSizePolicy)
from PySide2.QtCore import Qt
from PySide2.QtUiTools import (QUiLoader)
import DB.conexion as conexion

class listaDeUsuarios():
    def __init__(self, db_ui):
        self.db_ui = db_ui
        self.usuarios_ui = QUiLoader().load('DB/listaDeUsuarios.ui', self.db_ui.stage)

    def buttonDown(self, state):
        self.state = state
        self.db_ui.Eliminar_btn.setAutoExclusive(self.state)
        self.db_ui.BackUp_btn.setAutoExclusive(self.state)
        self.db_ui.Editar_btn.setAutoExclusive(self.state)
        self.db_ui.Registrar_btn.setAutoExclusive(self.state)

    def crea_tabla(self):
        consulta = '''CREATE TABLE IF NOT EXISTS user 
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT CHAR (50),  
            apellido TEXT CHAR (50), 
            DNI TEXT CHAR (50),
            unidad TEXT CHAR (50)
        );'''
        self.version = conexion.RegistroDatos(consulta)
        self.version.close()

    def allUsers(self):
        consulta = '''SELECT * FROM user;'''
        consultaUsuarios = conexion.RegistroDatos(consulta)
        return consultaUsuarios.listado()

    def fillTable(self,users):
        self.users = users
        self.usuarios_ui.tableWidget.setColumnWidth(0, 25)
        self.usuarios_ui.tableWidget.setColumnCount(5)
        self.usuarios_ui.tableWidget.setRowCount(len(users))
        #self.usuarios_ui.tableWidget.setHorizontalHeaderLabels(('ID','Nombre','Apellido','DNI','Unidad'))
        
        tablerow = 0
        for row in users:
            id = QTableWidgetItem(str(row[0]))
            id.setTextAlignment(5)
            self.usuarios_ui.tableWidget.setItem(tablerow,0,id)
            nombre = QTableWidgetItem(row[1])
            nombre.setTextAlignment(5)
            self.usuarios_ui.tableWidget.setItem(tablerow,1,nombre)
            apellido = QTableWidgetItem(row[2])
            apellido.setTextAlignment(5)
            self.usuarios_ui.tableWidget.setItem(tablerow,2,apellido)
            dni = QTableWidgetItem(row[3])
            dni.setTextAlignment(5)
            self.usuarios_ui.tableWidget.setItem(tablerow,3,dni)
            unidad = QTableWidgetItem(row[4])
            unidad.setTextAlignment(5)
            self.usuarios_ui.tableWidget.setItem(tablerow,4,unidad)
            tablerow +=1
    
    def userUiShow(self):
        self.usuarios_ui.show()

    def textChanged(self):
        print("textChanged")


