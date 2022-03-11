#from PyQt5 import QtWidgets, uic
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import numpy as np
import cv2
import imutils
import qimage2ndarray
import socket
import json
import MenuConfiguracionSistema.resoluciones as resolucion
import MenuConfiguracionSistema.configuracionsistema as configuracionsistema
import MenuConfiguracionSistema.ui_calibracion as ui_calibracion

class ConfiguracionGral(QtWidgets.QWidget, configuracionsistema.Ui_Configuracion):
    #DEFAULT_CONFIG = ["3840x2160", "10000", "3840x2160", "6", "10"]
    #RESOLUCIONES_CAM = ["640x480", "800x600", "1280x720","1920x1080","3840x2160", "1280x1024"]
    #RESOLUCIONES_PROY = ["640x480", "800x600", "1280x720","1920x1080","3840x2160", "1280x1024"]
     
    DEFAULT_CONFIG =  resolucion.resDefault()
    RESOLUCIONES_CAM = resolucion.resCam()
    RESOLUCIONES_PROY = resolucion.resProy()
    CANTIDAD_TIRADORES = resolucion.cantTiradores()
    
    
    def __init__(self, parent, screen, socket_madst, udp_madst):
        super().__init__()
        self.setupUi(self)
        
        self.parent = parent
        self.screen = screen
        self.socket_madst = socket_madst
        self.udp_madst = udp_madst
        
        self.button_connections()
        
        # -------------------------------------------------------------------------------------------------
        self.comboResolucionCamara.addItems(self.RESOLUCIONES_CAM)
        self.comboResolucionProyector.addItems(self.RESOLUCIONES_PROY)
        self.comboCantidadTiradores.addItems(self.CANTIDAD_TIRADORES)
        try:  
            with open('ConfiguracionGral.json') as jsonfile:
                data = json.load(jsonfile)
                self.lineTiempoExposicion.setText(data['configuracion'][0][self.labelTiempoExposicion.text()])
                self.lineTiempoLaserOn.setText(data['configuracion'][0][self.labelTiempoLaserOn.text()])
                self.lineDisTiradorPantalla.setText(data['configuracion'][0][self.labelDistTiradorPantalla.text()])
                self.lineTiempoEntreDisparos.setText(data['configuracion'][0][self.labelTiempoEntreDisparos.text()])
                self.lineCantPulsosDisparoFalso.setText(data['configuracion'][0][self.labelCantPulsosDisparoFalso.text()])
                self.lineEscalaResultado.setText(data['configuracion'][0][self.labelEscalaResultado.text()])
                self.comboCantidadTiradores.setCurrentIndex(self.comboCantidadTiradores.findText(data['configuracion'][0][self.labelCantidadTiradores.text()]))
                self.lineAnchoPantalla.setText(data['configuracion'][0][self.labelAnchoPantalla.text()])
                self.comboResolucionCamara.setCurrentIndex(self.comboResolucionCamara.findText(data['configuracion'][0][self.labelResolucionCamara.text()]))
                                
                self.lineCuadrosPorSegundo.setText(data['configuracion'][0][self.labelCuadrosPorSegundo.text()])
                self.lineDistCamaraProyector.setText(data['configuracion'][0][self.labelDistCamaraProyector.text()])
                                
                self.comboResolucionProyector.setCurrentIndex(self.comboResolucionProyector.findText(data['configuracion'][0][self.labelResolucionProyector.text()]))
                         
                
        except Exception as e:
             print (e)
             self.comboResolucionCamara.setCurrentIndex(self.comboResolucionCamara.findText(self.DEFAULT_CONFIG[0]))
             self.comboResolucionProyector.setCurrentIndex(self.comboResolucionProyector.findText(self.DEFAULT_CONFIG[1]))
             self.lineTiempoExposicion.setText(self.DEFAULT_CONFIG[2])
             self.lineTiempoLaserOn.setText(self.DEFAULT_CONFIG[3])
             self.comboCantidadTiradores.setCurrentIndex(self.comboCantidadTiradores.findText(self.DEFAULT_CONFIG[4]))
             self.lineDisTiradorPantalla.setText(self.DEFAULT_CONFIG[5])
                       
        # --------------------------------------------------------------------------------------------------
        
    def button_connections(self):
        self.pushGuardarConfiguracion.clicked.connect(self.Guardar)
        self.pushCalibracionAutomatica.clicked.connect(self.Calibracion)
        
    
    def Guardar(self):
        fps = int(self.lineCuadrosPorSegundo.text())
        tiempo_laser = int(self.lineTiempoLaserOn.text())
        #self.parent.s.sendall(b"oper_fin")
        try:
            if self.parent.estado == "OPER":
                self.parent.oper_fin()
                time.sleep(0.1)
            self.parent.config_ini()
            self.parent.s.sendall(dumps((fps, 1, tiempo_laser)))
            self.parent.estado = "SELEC_MOD"
        except:
            pass
        data = {}
        data['configuracion'] = []
        data['configuracion'].append({
            self.labelTiempoExposicion.text():self.lineTiempoExposicion.text(),
            self.labelCuadrosPorSegundo.text():self.lineCuadrosPorSegundo.text(),
            self.labelTiempoLaserOn.text(): self.lineTiempoLaserOn.text(),
            self.labelDistTiradorPantalla.text(): self.lineDisTiradorPantalla.text(),
            self.labelTiempoEntreDisparos.text(): self.lineTiempoEntreDisparos.text(),
            self.labelResolucionProyector.text():self.comboResolucionProyector.currentText(),
            self.labelResolucionCamara.text():self.comboResolucionCamara.currentText(),
            self.labelCantidadTiradores.text():self.comboCantidadTiradores.currentText(),
            self.labelDistCamaraProyector.text(): self.lineDistCamaraProyector.text(),
            self.labelAnchoPantalla.text(): self.lineAnchoPantalla.text(),
            self.labelCantPulsosDisparoFalso.text(): self.lineCantPulsosDisparoFalso.text(),   
            self.labelEscalaResultado.text(): self.lineEscalaResultado.text(),
            
            #self.labelVisible.text():self.comboVisible.currentText(),
})
                                
        with open('ConfiguracionGral.json', 'w') as outfile:
            outfile.write(json.dumps(data, indent = 4))
        print ("Grabar")
        try:
            self.calib_win.close()
        except:
            pass
        self.close()
    
    def closeEvent(self, event):
        try:
            self.calib_win.close()
        except:
            pass
        event.accept()
    
    def Calibracion(self):
        #self.generaimg((int(self.screen.width()),int(self.screen.height())),int(self.linePuntos.text()),int(self.lineDiametro.text()),0,0, True)
        self.generaimg((int(self.screen.width()),int(self.screen.height())),10,5,0,0, True)
        #self.generaimg((int(self.screen.width()),int(self.screen.height())),int(self.linePuntos.text()),int(self.lineDiametro.text()),0,0, False)
        self.generaimg((int(self.screen.width()),int(self.screen.height())),10,5,0,0, False)
        self.calib_win = calibWindow(self, self.screen, self.socket_madst, self.udp_madst)
        #self.calib_win = calibWindow(self, self.screen)
        self.calib_win.show()
        print ("Calibracion")
        
    def generaimg(self,resolucion, puntosx, diametro, posx, posy, blanco): 
        
        blanck_image = np.zeros((resolucion[1],resolucion[0],3),np.uint8)
        relacion = float(resolucion[1])/resolucion[0]
        if blanco:
            blanck_image[:] = 255
            cv2.imwrite("blanco.jpg",blanck_image)
            cv2.imwrite("blanco.png",blanck_image)
        else:       
            puntosy = int(relacion*puntosx)
            distx = resolucion[0]/float(puntosx)
            disty = resolucion[1]/float(puntosy)
            puntosx = int(puntosx) 
            puntosy = int(puntosy)
            puntos = []
            for j in range(0,puntosy):
                for i in range(0,puntosx):
                    puntos.append((int(i*distx + distx/2),int(j*disty + disty/2)))    
            for p in puntos:
                cv2.circle(blanck_image,p,diametro,(255,255,255), -1)
            cv2.imwrite("puntos.jpg",blanck_image)
            cv2.imwrite("puntos.png",blanck_image)
            blanck_image = imutils.resize(blanck_image, width=3840)
            cv2.imwrite("/home/simulacion/Proyectos/MADST4/patternCalibrationImage.png",blanck_image)
        

class calibWindow(QtWidgets.QWidget, ui_calibracion.Ui_Calibracion):
    
    def __init__(self, parent, screen, socket_madst, udp_madst):
    #def __init__(self, parent, screen):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        qimage2ndarray
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(screen.x(),screen.y(),screen.width(),screen.height())
        
        self.label.setGeometry(0,0,screen.width(),screen.height())
        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'),self.mostrar)
        self.label.setPixmap(QtGui.QPixmap("blanco.jpg"))
        self.socket_madst = socket_madst
        self.udp_madst = udp_madst
        jsonDatagram = {
                            "messageType":"AUTOCALIBRATE_SCREEN_BORDER"
                       }
        self.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'),  self.udp_madst)
        
    def mostrar(self):
        imagen = "puntos.jpg"         
        self.label.setPixmap(QtGui.QPixmap(imagen))
        self.timer.stop()
        jsonDatagram = {
                            "messageType":"AUTOCALIBRATE_SCREEN_DOTS"
                       }
        self.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'), self.udp_madst)

