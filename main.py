from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import socket
import json
import sys
from PySide2.QtWidgets import QStyleFactory

#Import ui y configuraciones
import MenuConfiguracionSistema.ConfiguracionGral as ConfiguracionGral
import MenuAlineacionArmas.FuncionalidadAlineacion as funcalineacion
import ConfigSituacion.FuncionalidadEjercitacion as funcejercitacion
import DB.DB as funcDB
import MenuCtrlVisualizacion.Reproduccion as Reproduccion
import RecursosSTPUI_rc
    
class MainWidget(QtWidgets.QWidget):
	
		
    def __init__(self, screen):
        super().__init__()
                   
        
        #Conexion con MADST
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 5557
        self.UDP_RECV = 5558
        
        self.disparos=[]

        self.socket_madst = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.sock_recv = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

        self.udp_madst = (self.UDP_IP, self.UDP_PORT)
        
        self.sock_recv.bind((self.UDP_IP,self.UDP_RECV))
        
        self.sock_recv.settimeout(0.01)
        self.timer = QtCore.QTimer()
        self.timer.start(1)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'),self.recibeMADST)
        
        #Inicio Display
        self.screen = screen
        # setup address widget
        self.main_widget = QtWidgets.QWidget()
        loader = QUiLoader()
        
        
        # Setup QVBox Main Layout
        self.VBox = QtWidgets.QVBoxLayout(self)
        self.VBox.addWidget(self.main_widget,1)
        self.VBox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.VBox)
        self.setFixedWidth(1360)
        self.setFixedHeight(100)
        self.setGeometry(0,0, self.frameGeometry().width(), self.frameGeometry().height())
        
        self.main_ui = loader.load('MainMenu/MainMenu.ui', self.main_widget)
        self.alineacion_widget = QtWidgets.QWidget()
        self.alineacion_ui = loader.load('MenuAlineacionArmas/AlineacionArmas.ui', self.alineacion_widget)        
        self.menutiradores_widget = QtWidgets.QWidget()
        self.menutiradores_ui = loader.load('MenuTiradores/MenuTiradores.ui', self.menutiradores_widget)
        self.configsituacion_widget = QtWidgets.QWidget()
        self.configsituacion_ui = loader.load('ConfigSituacion/ConfigSituacion.ui', self.configsituacion_widget)
        self.DB_widget = QtWidgets.QWidget()
        self.DB_ui = loader.load('DB/DB.ui', self.DB_widget)
                             
        self.button_connections()
        
    def button_connections(self):
        self.main_ui.AlineacionButton.clicked.connect(self.Alineacion)
        self.main_ui.EjerEvalButton.clicked.connect(self.Ejercitacion)
        self.main_ui.ReproducirButton.clicked.connect(self.Reproducir)
        self.main_ui.BaseDatosButton.clicked.connect(self.DB)
        self.main_ui.ConfiguracionButton.clicked.connect(self.clickConfig)
        self.main_ui.SalirGral.clicked.connect(self.salir)
        
    def clickConfig(self):
        self.config = ConfiguracionGral.ConfiguracionGral(self, self.screen, self.socket_madst, self.udp_madst)
        self.config.show()
        
    def Alineacion(self):
        self.funcAlineacion = funcalineacion.Alineacion(self)
        self.main_ui.EjerEvalButton.setEnabled(False)
        self.main_ui.ReproducirButton.setEnabled(False)
        self.main_ui.BaseDatosButton.setEnabled(False)
        self.main_ui.ConfiguracionButton.setEnabled(False)
        self.alineacion_ui.pushButtonSalir.clicked.connect(self.funcAlineacion.salirAlineacion)
        
    def Ejercitacion(self):
        self.main_ui.AlineacionButton.setEnabled(False)
        self.main_ui.ReproducirButton.setEnabled(False)
        self.main_ui.ConfiguracionButton.setEnabled(False)
        self.funcEjercitacion = funcejercitacion.Ejercitacion(self)
        self.main_ui.BaseDatosButton.setEnabled(False)
        self.configsituacion_ui.SalirEjercitacion.clicked.connect(self.funcEjercitacion.salirejercitacion)
        self.configsituacion_ui.QSituacionSelect.selectionModel().selectionChanged.connect(self.funcEjercitacion.on_selection_changed)
        self.configsituacion_ui.ButtonOK.clicked.connect(self.funcEjercitacion.iniciarEnsayo)
        
    def DB(self):
        self.main_ui.AlineacionButton.setEnabled(False)
        self.main_ui.EjerEvalButton.setEnabled(False)
        self.main_ui.ReproducirButton.setEnabled(False)
        self.funcDB = funcDB.DB(self)
        self.main_ui.ConfiguracionButton.setEnabled(False)
        self.DB_ui.salir.clicked.connect(self.funcDB.salir)
        self.DB_ui.aListaDeUsuarios.clicked.connect(self.funcDB.listaDeUsuarios)
        self.DB_ui.bBackUp.clicked.connect(self.funcDB.backUp)
        self.DB_ui.cEditarPerfil.clicked.connect(self.funcDB.editarPerfil)
        self.DB_ui.dRegistrarUsuario.clicked.connect(self.funcDB.registrarUsusario)
    
    def Reproducir(self):
        self.main_ui.AlineacionButton.setEnabled(False)
        self.main_ui.EjerEvalButton.setEnabled(False)
        self.main_ui.BaseDatosButton.setEnabled(False)
        self.main_ui.ConfiguracionButton.setEnabled(False)
        self.reproduccion = Reproduccion.reproduccionwindow(self)
        self.reproduccion.show()
        
    def recibeMADST(self):
        try:
             dato = self.sock_recv.recvfrom(1024)[0].decode('utf-8')
             dato = json.loads(dato)
             respuesta = dato['responseType']
             estado = dato['madstState']
             #self.labelEstado.setText("Estado MADST: " + estado)
             #self.labelRespuesta.setText("Respuesta MADST: " + respuesta)
             try:
                 if (len(dato['sensed_shots'])):
                    self.disparos.append(dato['sensed_shots'])
                    #print(self.disparos)
                        
             except Exception as e:
                 print (e)
        except Exception as e:
            pass
        
    def salir(self):
        
        self.close()
        
    def closeEvent(self, event):
        print("Close")
        try:
            self.config.close()
        except:
            pass
        try:
            self.reproduccion.close()
        except:
            pass
        try:
            self.funcEjercitacion.salirejercitacion()
        except:
            pass

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('fusion'))
    screenRect = app.desktop().screenGeometry(0)
    widget = MainWidget(screenRect)
    widget.show()
    app.exec_()

