import MenuAlineacionArmas.RecursosSTPUI

class Alineacion():
    def __init__(self, parent):
        self.parent = parent
        self = parent
        self.VBox.addWidget(self.alineacion_widget,3)
        #self.VBox.addWidget(self.menutiradores_widget,2)
        self.VBox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.VBox)
        self.setFixedWidth(1360)
        self.setFixedHeight(500)
        
        
    def saliralineacion(self):
        print("Salir Alineacion")
        self.parent.main_ui.EjerEvalButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.alineacion_widget.setParent(None)
        self.parent.setFixedHeight(100)
