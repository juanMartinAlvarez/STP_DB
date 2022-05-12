import sqlite3

class RegistroDatos():
    def __init__(self, consulta):
        self.consulta = consulta
        try:
            # make sqlite db file
            self.conexion = sqlite3.connect('DB/stpDB.sqlite')
            cursor = self.conexion.cursor()
            cursor.execute(self.consulta)
            cursor.fetchall()
        except sqlite3.Error as error:
            print('Se ha producido un error', error)

    def close(self):
        if self.conexion:
            self.conexion.close()
            print('la conexion se ha cerrado correctamente')