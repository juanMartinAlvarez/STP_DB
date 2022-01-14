from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileSystemModel
from PySide2.QtCore import QDir
import json

file_path = [None, None, None]
        
class Ejercitacion():
    def __init__(self, parent):
        self.parent = parent
        self = parent
                
        self.VBox.addWidget(self.configsituacion_widget,6)  ##RT 5
        self.VBox.addWidget(self.menutiradores_widget,2)
        #self.VBox.addWidget(self.menutiradores_widget,2)
        self.VBox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.VBox)
        
        self.setFixedWidth(1360)  ##RT
        self.setFixedHeight(1024)
        
        loader = QUiLoader()
        self.situacion_ui = loader.load('SetSituaciones1/SetSituaciones1.ui', self.configsituacion_ui.dConfiguracion)
        
        model = QFileSystemModel()
        model.setRootPath("./Situaciones")
        
        
        self.configsituacion_ui.QSituacionSelect.setModel(model)
        self.configsituacion_ui.QSituacionSelect.setColumnWidths((207,207,207))
        self.configsituacion_ui.QSituacionSelect.setRootIndex(model.index("./Situaciones"))
        
        
    def salirejercitacion(self):
        print("Salir Ejercitacion")
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.configsituacion_widget.setParent(None)
        self.parent.menutiradores_widget.setParent(None)
        self.parent.setFixedHeight(100)

    def on_selection_changed(self):
        global file_path
        indexes = self.parent.configsituacion_ui.QSituacionSelect.selectedIndexes()
        for index in indexes:
            try:
                file_path[int(index.data(0)[0])] = index.data(0)
                if (int(index.data(0)[0]) < 2):
                    self.parent.configsituacion_ui.textBrowser.setText('')
                else:
                    try:  
                        print(file_path)
                        with open("./Situaciones/"+file_path[0]+'/'+file_path[1]+'/'+file_path[2]) as jsonfile:
                            data = json.load(jsonfile)
                            print(data)
                            self.parent.configsituacion_ui.textBrowser.setText(data['configuracion'][0]['Descripcion'])
                    except:
                        print("Error en Archivo de Configuracion")
            except:
                print("Mal nombre carpeta/archivo")
