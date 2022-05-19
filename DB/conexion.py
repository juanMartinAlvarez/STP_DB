import sqlite3

from colorama import Cursor

class RegistroDatos():
    def __init__(self, consulta):
        self.consulta = consulta
        try:
            # make sqlite db file
            self.conexion = sqlite3.connect('DB/stpDB.sqlite')
            self.cursor = self.conexion.cursor()
            self.cursor.execute(self.consulta)
            self.cursor.fetchall()
        except sqlite3.Error as error:
            print('Se ha producido un error', error)

    def close(self):
        if self.conexion:
            print('close conexion')
            self.conexion.close()
            