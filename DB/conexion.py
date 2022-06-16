import sqlite3
from colorama import Cursor

class RegistroDatos():
    def __init__(self, consulta):
        self.consulta = consulta
        try:
            # make sqlite db file
            self.conexion = sqlite3.connect('DB/stpDB.sqlite')
            self.cursor = self.conexion.cursor()
            print("registro datos consulta: " + self.consulta)
            self.cursor.execute(self.consulta)
            self.datos = self.cursor.fetchall()
            self.conexion.commit()
            
        except sqlite3.Error as error:
            self.datos= None
            print('Se ha producido un error', error)

    def listado(self):
        return (self.datos)

    def close(self):
        if self.conexion:
            print('close conexion')
            self.conexion.close()



