from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileSystemModel
from PySide2.QtCore import QDir
import ConfigSituacion.ui_ejercitacion as ui_ejercitacion
import json
import cv2
import numpy as np
import imutils
import qimage2ndarray
from threading import Thread
import time
import subprocess
import csv

file_path = [None, None, None]
situacion = None
path = None
condicion = None
cont = 0
        
class Ejercitacion():
    def __init__(self, parent):
        self.parent = parent
        #self = parent
                
        self.parent.VBox.addWidget(self.parent.configsituacion_widget,6)  ##RT 5
        self.parent.VBox.addWidget(self.parent.menutiradores_widget,2)
        #self.VBox.addWidget(self.menutiradores_widget,2)
        self.parent.VBox.setContentsMargins(0, 0, 0, 0)
        self.parent.setLayout(self.parent.VBox)
        
        self.parent.setFixedWidth(1360)  ##RT
        self.parent.setFixedHeight(1024)
        
        loader = QUiLoader()
        self.parent.configsituacion_ui.situacion_ui = loader.load('SetSituaciones1/SetSituaciones1.ui', self.parent.configsituacion_ui.dConfiguracion)
        
        model = QFileSystemModel()
        model.setRootPath("./Situaciones")
        
        
        self.parent.configsituacion_ui.QSituacionSelect.setModel(model)
        self.parent.configsituacion_ui.QSituacionSelect.setColumnWidths((207,207,207))
        self.parent.configsituacion_ui.QSituacionSelect.setRootIndex(model.index("./Situaciones"))
        self.parent.configsituacion_ui.ButtonOK.setEnabled(False)
        
        
    def salirejercitacion(self):
        print("Salir Ejercitacion")
        try:
            self.ejercitacion_proy.close()
            
        except:
            pass 
        jsonDatagram = {
                            "messageType":"STOP_SENSING_SHOTS"
                       }
        self.parent.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'), self.parent.udp_madst)
        cv2.destroyAllWindows()
        self.parent.main_ui.AlineacionButton.setEnabled(True)
        self.parent.main_ui.ReproducirButton.setEnabled(True)
        self.parent.main_ui.ConfiguracionButton.setEnabled(True)
        self.parent.main_ui.BaseDatosButton.setEnabled(True)
        self.parent.configsituacion_widget.setParent(None)
        self.parent.menutiradores_widget.setParent(None)
        self.parent.setFixedHeight(100)

    def on_selection_changed(self):
        global file_path
        global situacion
        global path
        global condicion
        indexes = self.parent.configsituacion_ui.QSituacionSelect.selectedIndexes()
        for index in indexes:
            try:
                file_path[int(index.data(0)[0])] = index.data(0)
                if (int(index.data(0)[0]) < 2):
                    self.parent.configsituacion_ui.textBrowser.setText('')
                else:
                    try:  
                        print(file_path)
                        condicion = file_path[1]
                        path = "./Situaciones/"+file_path[0]+'/'+file_path[1]+'/'
                        situacion = "./Situaciones/"+file_path[0]+'/'+file_path[1]+'/'+file_path[2]
                        with open("./Situaciones/"+file_path[0]+'/'+file_path[1]+'/'+file_path[2]) as jsonfile:
                            data = json.load(jsonfile)
                            print(data)
                            self.parent.configsituacion_ui.textBrowser.setText(data['configuracion'][0]['Descripcion'])
                            self.parent.configsituacion_ui.ButtonOK.setEnabled(True)
                    except:
                        print("Error en Archivo de Configuracion")
            except:
                print("Mal nombre carpeta/archivo")
                
        
    def iniciarEnsayo(self):
        global situacion
        global path
        global condicion
        print("Inicia Ensayo")
        data = 0
        with open('ConfiguracionGral.json', 'r') as json_file:
            data = json.load(json_file)
        #dist = int(EditDist.get())
        cv2.destroyAllWindows()
        blanck_image = np.zeros((self.parent.screen.height(),self.parent.screen.width(),3),np.uint8)

        with open(situacion, 'r') as json_file:
            dato = json.load(json_file)
        self.offset_x = int(dato['configuracion'][0]['Offset X'])
        self.offset_y = int(dato['configuracion'][0]['Offset Y'])

        self.widthHoja = float(dato['configuracion'][0]['Width Hoja'])
        self.DistanciaBlanco = float(dato['configuracion'][0]['Distancia Blanco'])
        self.CuadradoMote = float(dato['configuracion'][0]['Cuadrado Mote'])
        self.archivo_imagen = dato['configuracion'][0]['Imagen']

        puntosVisibles = self.parent.configsituacion_ui.situacion_ui.VerImpactos.isChecked()
        
        mote = cv2.imread("Imagenes_Mote/" + self.archivo_imagen)
        width_A4 = self.widthHoja
        width = mote.shape[1]
        dist_tirador = float(data['configuracion'][0]['Distancia Tirador Pantalla'])
        #Asi lo tenia antes?
        #width = width*(dist_tirador/9.5)
        Res_X = int(data['configuracion'][0]['Resolución Proyector'].split('x')[0])
        #width_A4 = 0.210
        Tamano_Pantalla = float(data['configuracion'][0]['Ancho Pantalla [m]'])
        TAMANO_ESCALA = int(data['configuracion'][0]['Escala Resultado'])   
        dist_blanco = self.DistanciaBlanco
        width = (width_A4 * Res_X)/Tamano_Pantalla
        cuadrado_mote = self.CuadradoMote*TAMANO_ESCALA

        
        tam_cuadrado = (cuadrado_mote*Res_X*TAMANO_ESCALA) / Tamano_Pantalla 
        mote = imutils.resize(mote, width=int(width*TAMANO_ESCALA))
           

        width_new = width*(dist_tirador/dist_blanco)
        mote_ini = imutils.resize(mote, width=int(width_new))
            
        #centro_x = self.screen.height()/2 + self.offset_x
        #centro_y = self.screen.width()/2 + self.offset_y
        print (mote.shape[1], mote.shape[0])
        
        #Mote en blanco a distancia de 25 mts
        cv2.imwrite("ejercitacion.jpg", mote_ini)
        cv2.imwrite("ejercitacion.png", mote_ini)

        #Esto es para los disparos

        #blanck_image = np.zeros((self.screen.height(),self.screen.width(),3),np.uint8)

        #blanck_image[int(self.screen.height()/2-mote.shape[0]/2):int(self.screen.height()/2+mote.shape[0]/2),int(self.screen.width()/2-mote.shape[1]/2):int(self.screen.width()/2+mote.shape[1]/2)] = mote

        blanck_image = cv2.cvtColor(mote, cv2.COLOR_BGR2RGBA)
        cv2.imwrite("ejercitacion_fin.jpg", blanck_image)
        cv2.imwrite("ejercitacion_fin.png", blanck_image)
            
        #Esto sirve para la proyeccion cambio a clase ejercitacioProyectorWindow
        try:
            self.ejercitacion_proy.close()
        except:
            pass 
        self.ejercitacion_proy = ejercitacionProyectorWindow(self, self.parent.screen, self.parent.socket_madst, self.parent.udp_madst, situacion, puntosVisibles, self.parent.disparos, condicion)#, self.disparos, self.pulso, self.situacion, self.test)

        self.ejercitacion_proy.show()

class ejercitacionProyectorWindow(QtWidgets.QWidget, ui_ejercitacion.Ui_Ejercitacion):
    
    def __init__(self, parent, screen, socket_madst, udp_madst, situacion, puntosVisibles, disparos, condicion):#, disparos, pulso, situacion, test):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.situacion = situacion
        self.condicion = condicion
        self.setStyleSheet("background-color: black;")
        self.socket_madst = socket_madst
        self.udp_madst = udp_madst
        self.disparos = disparos
        # ~ self.pulso = pulso
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(screen.x(),screen.y(),screen.width(),screen.height())
        #self.test = test
                
        img = cv2.imread("ejercitacion.jpg")
        tamano = img.shape
        self.label.setGeometry(0,0,screen.width(),screen.height())
        #self.label2.setGeometry(0,0,screen.width(),screen.height())
        self.label2.setHidden(True)
        #self.x = 0
        #self.y = screen.width()/2- tamano[1]/2
        #self.label.move(self.y, self.x)
        self.screen = screen
        
        data = 0
        with open('ConfiguracionGral.json', 'r') as json_file:
            data = json.load(json_file)
        tiempo = float(data['configuracion'][0]['Tiempo entre disparos [ms]'])
        Res_CAM = int(data['configuracion'][0]['Resoluci\u00f3n Camara'].split('x')[0])
        self.escala_proyeccion = Res_CAM/screen.width()    
        #self.PuntosVisibles = eval(data['configuracion'][0]['Disparo Visibles'])
        self.PuntosVisibles = puntosVisibles
        self.CantPulsos = int(data['configuracion'][0]['Cant. Pulsos disparo falso'])
        self.CantidadTiradores = int(data['configuracion'][0]['Cantidad de Tiradores'])
        self.TiradorAnalizar = 1 #Por ahora lo dejo fijo
        
        # ~ #Agregue un archivo de configuracion para cada video
        with open(self.situacion, 'r') as json_file:
            data = json.load(json_file)
        self.offset_x = int(data['configuracion'][0]['Offset X'])
        self.offset_y = int(data['configuracion'][0]['Offset Y'])
        
        self.widthHoja = float(data['configuracion'][0]['Width Hoja'])
        self.DistanciaBlanco = float(data['configuracion'][0]['Distancia Blanco'])
        self.CuadradoMote = float(data['configuracion'][0]['Cuadrado Mote'])
        self.CantidadDisparos = int(data['configuracion'][0]['Cantidad Disparos'])
        self.Velocidad = float(data['configuracion'][0]['Velocidad'])
        self.archivo_video = data['configuracion'][0]['Video']
        
        mote_ini = cv2.imread("ejercitacion.jpg")
        #back = cv2.imread("background.jpeg")
        
        # ~ #self.video = cv2.VideoCapture("Condiciones/" + str(self.condicion) +"/" + str(self.condicion) + ".mp4")
        self.video = cv2.VideoCapture("Videos_ejercitacion/" + self.archivo_video)
        
        # ~ #self.player = MediaPlayer("Condiciones/" + str(self.condicion) +"/" + str(self.condicion) + ".mp4")
        back = self.video.read()[1]
        back = cv2.cvtColor(back, cv2.COLOR_BGR2RGB)
        back = cv2.resize(back, (int(self.screen.width()), int(self.screen.height())))
        
        # ~ #dst = cv2.addWeighted(front, 1, back, 0.5, 0.0)
        
        
        #saco el offset
        self.offset_x = 0
        self.offset_y = 0
        centro_x = self.screen.height()/2 + self.offset_y
        centro_y = self.screen.width()/(1 + self.CantidadTiradores) + self.offset_x
        self.labelResultado = []
        self.labelImage = []
        
        self.frame = []
        
        for i in range(self.CantidadTiradores):
            i = i
            back[int(centro_x - mote_ini.shape[0]/2):int(centro_x + mote_ini.shape[0]/2),int(centro_y*(i+1) - mote_ini.shape[1]/2):int(centro_y*(i+1) + mote_ini.shape[1]/2)] = mote_ini
            #Texto de resultados
                        
            self.frame.append(QtWidgets.QFrame(self))
            #Color para el recuadro de los tiradores
            self.frame[i].setStyleSheet("background: rgba(0, 255, 0, 40);");
            
            self.frame[i].setFrameStyle(QtWidgets.QFrame.Panel)
            self.frame[i].setLineWidth(3)
            
            ancho_texto = 350
            alto_texto = 150
            
            
            self.frame[i].setGeometry(QtCore.QRect(centro_y*(i+1)- ancho_texto/2, 0, ancho_texto, alto_texto))
            
            hbox = QtWidgets.QHBoxLayout()
            self.labelResultado.append(QtWidgets.QLabel(self.frame[i]))
            
            self.labelResultado[i].setStyleSheet("background: rgba(0, 0, 0, 0);color:rgba(255,255,255,255); font-size: 20px;");
            escribe = "Situacion\nDisparo: 0/"+str(self.CantidadDisparos)+"\nDisparos en Blanco: 0/"+str(self.CantidadDisparos)
            #texto = "<html><head/><body><p><span style=\"font-size:20pt; color:#ffffff;\"\>" + escribe + "</span></p></body></html>"
            self.labelResultado[i].setWordWrap(True);
            self.labelResultado[i].setText(escribe)
            
            self.labelImage.append(QtWidgets.QLabel(self.frame[i]))
            self.labelImage[i].setStyleSheet("background: rgba(0, 0, 0, 0);");
            #self.labelImage[i].setScaledContents(True)

            self.labelImage[i].setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored )
            #self.labelImage[i].setPixmap(QtGui.QPixmap("img/Mote_Basico.jpg"))
            self.labelImage[i].resize = (60,50)
            self.labelImage[i].setPixmap(QtGui.QPixmap("imagen_muestra.jpg").scaled(60, 50, QtCore.Qt.KeepAspectRatio))
            
            hbox.addWidget(self.labelResultado[i])
            hbox.addWidget(self.labelImage[i])
            self.frame[i].setLayout(hbox)
        
        image = qimage2ndarray.array2qimage(back)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        
        # ~ #self.label.setPixmap(QtGui.QPixmap("ejercitacion.jpg"))
        # ~ #self.PuntosVisibles = False

        self.tiempo = tiempo/1000
        self.hilo_disparo = []

        self.resultado_disparo = [[],[],[],[]]
        self.thread_stop = False
        
        self.test=True
        self.disparos_thread = Thread(target=self.thread_disparos)
        self.disparos_thread.start()
        
        self.timer = QtCore.QTimer()
        self.timer.start(33)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'),self.resultados)

        jsonDatagram = {
                            "messageType":"START_SENSING_SHOTS"
                       }
        
        self.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'), self.udp_madst)
        if self.test == 1:
            self.pid = subprocess.Popen(['python3.6', 'sensed_shots_report_example.py'])
        
        #Habilito Audio
        self.audio = subprocess.Popen(['python3.6', 'audio.py'])        
        
        self.disparos.clear()
        # ~ #self.first = True
        # ~ #self.second = True
        self.cont = 5
        self.contDisparos=[0,0,0,0]
        
        
        #Grabacion de Archivos CSV
        with open("Resultados.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Situacion:", self.condicion,"Cantidad de Tiradores", self.CantidadTiradores])
            writer.writerow(["Tirador:", "Posicion","Posicion Blanco"])
        

    def thread_disparos(self):
        while len(self.resultado_disparo[self.TiradorAnalizar-1]) < self.CantidadDisparos:
            time.sleep(0.005)
            
            if (self.thread_stop):
                break
            if self.test == 1:
                if (len(self.disparos)>0):
                    self.resultado_disparo[self.TiradorAnalizar-1].append(self.disparos[-1])
                    
                    self.disparos.clear()
            else:
                if self.tiempo == 0:
                    if self.pulso[-1][1] == True:     
                        print ("Thread Pulsador: " + str(self.pulso[-1][0]))
                        
                        #print(self.disparos)
                        #print(len(self.disparos))
                        if len(self.disparos):
                            print("analisis")
                            print(self.disparos[-1])
                            print ("Disparo")
                            if (len (self.resultado_disparo[self.pulso[-1][0]]) < self.CantidadDisparos):
                                self.resultado_disparo[self.pulso[-1][0]].append(self.disparos[-1])
                                
                            self.disparos.clear()
                else:
                    time.sleep(0.1)
                    if len(self.disparos):
                        print("analisis")
                        print(self.disparos)
                        time.sleep(self.tiempo)                
                        if len(self.disparos) > self.CantPulsos:
                            print ("No es Disparo")
                            self.disparos.clear()
                        else:
                            print ("Disparo")
                            self.resultado_disparo[0].append(self.disparos[0])
                            self.disparos.clear()
                                    
            
    
    def resultados(self):
        global cont
        paso = self.Velocidad
        mote_ini = cv2.imread("ejercitacion.jpg")
        ret, back = self.video.read()
        if ret == 0:
            #self.player.close_player()
            self.video = cv2.VideoCapture("Videos_ejercitacion/" + self.archivo_video)
            #self.player = MediaPlayer("Condiciones/" + str(self.condicion) +"/" + str(self.condicion) + ".mp4")
            ret, back = self.video.read()
            print ("Empieza el video")
            
        back = cv2.cvtColor(back, cv2.COLOR_BGR2RGB)
        back = cv2.resize(back, (int(self.screen.width()), int(self.screen.height())))
        
        
        centro_x = self.screen.height()/2 + self.offset_y
        #centro_y = self.screen.width()/2 + self.offset_x
        centro_y = self.screen.width()/(1 + self.CantidadTiradores) + self.offset_x
        
        
        
        for i in range(self.CantidadTiradores):
            back[int(centro_x - mote_ini.shape[0]/2):int(centro_x + mote_ini.shape[0]/2),int(centro_y*(i+1) + cont*paso - mote_ini.shape[1]/2):int(centro_y*(i+1) + cont*paso + mote_ini.shape[1]/2)] = mote_ini
            cont = cont + 1
            #Texto de resultados
            
            escribe = "Situacion "+ str(self.condicion) + "\nDisparo: "+str(len(self.resultado_disparo[i]))+"/"+str(self.CantidadDisparos)+"\nDisparos en Blanco: "+ str(len(self.resultado_disparo[i])) +"/"+str(self.CantidadDisparos)
            if (len(self.resultado_disparo[i]) == self.CantidadDisparos):
                self.frame[i].setStyleSheet("background: rgba(255, 0, 0, 40);")
            #texto = "<html><head/><body><p><span style=\"font-size:20pt; color:#ffffff;\"\>" + escribe + "</span></p></body></html>"
            self.labelResultado[i].setWordWrap(True);
            self.labelResultado[i].setText(escribe)
            self.labelImage[i].setScaledContents(False)

            #self.labelImage[i].setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored )
            self.labelImage[i].resize = (60,50)    
            self.labelImage[i].setPixmap(QtGui.QPixmap("imagen_muestra.jpg").scaled(60, 50, QtCore.Qt.KeepAspectRatio))
            
        #PATAS DEL CARTEL
        #largo_pata = 10
        #cv2.line(back, (int(centro_y + mote_ini.shape[1]/2 - 4), int(centro_x + mote_ini.shape[1]/2)), (int(centro_y + mote_ini.shape[1]/2 - 4), int(centro_x + mote_ini.shape[0]/2 + largo_pata)), (255, 255, 0), 1)
        #cv2.line(back, (int(centro_y - mote_ini.shape[1]/2 + 4), int(centro_x + mote_ini.shape[1]/2)), (int(centro_y - mote_ini.shape[1]/2 + 4), int(centro_x + mote_ini.shape[0]/2 + largo_pata)), (255, 255, 0), 1)
            colores_tirador=[(255,255,0),(255,0,255),(0,255,255),(255,255,255)]
            if len(self.resultado_disparo[i]):                
                #self.resultado_disparo.append(self.hilo_disparo[-1])
                #self.hilo_disparo.clear()
                if (len(self.resultado_disparo[i]) > self.contDisparos[i]):
                        with open("Resultados.csv", 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([i + 1, (self.resultado_disparo[i][-1][-1]['screenCoordinates'][1]//self.escala_proyeccion, self.resultado_disparo[i][-1][-1]['screenCoordinates'][0]//self.escala_proyeccion), (centro_x, centro_y*(i+1) + (cont-1)*paso)])
                        self.contDisparos[i] = len(self.resultado_disparo[i])
                
                for disparos in self.resultado_disparo[i]:
                    for shot in disparos:
                        point = shot['screenCoordinates']
                        #print (point)
                        if self.PuntosVisibles:
                            back = cv2.circle(back,(int(point[0]/self.escala_proyeccion),int(point[1]/self.escala_proyeccion)),5,colores_tirador[i], -1)
            #back = cv2.imread("background.jpeg")
        
        image = qimage2ndarray.array2qimage(back)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        
        
        if len(self.resultado_disparo[self.TiradorAnalizar-1]) >= self.CantidadDisparos:            
            self.cont = self.cont - 1         
            if self.cont:
                print ("********************************SLEEP******************************************")
                    
            else:
                time.sleep(2)
                print ("********************************Disparos completos**************************************")
                if self.test == 1:
                    self.pid.terminate()
                self.audio.terminate()                
                self.thread_stop = True
                jsonDatagram = {
                                "messageType":"STOP_SENSING_SHOTS"
                           }
                self.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'), self.udp_madst)
                
                mote = cv2.imread("ejercitacion_fin.jpg")
                
                
                ret, back = self.video.read()
                if ret == 0:
                    #self.player.close_player()
                    self.video = cv2.VideoCapture("Videos_ejercitacion/" + self.archivo_video)
                    #self.player = MediaPlayer("Condiciones/" + str(self.condicion) +"/" + str(self.condicion) + ".mp4")
                    ret, back = self.video.read()
                    
                back = cv2.cvtColor(back, cv2.COLOR_BGR2RGB)
                blanck_image = cv2.resize(back, (int(self.screen.width()), int(self.screen.height())))
                
                #blanck_image[int(self.screen.height()/2-mote.shape[0]/2):int(self.screen.height()/2+mote.shape[0]/2),int(self.screen.width()/2-mote.shape[1]/2):int(self.screen.width()/2+mote.shape[1]/2)] = mote
                if (mote.shape[0] > self.screen.height()):
                    if (mote.shape[1] > self.screen.width()):
                        blanck_image[:,:] = mote[int(mote.shape[0]/2-self.screen.height()/2):int(mote.shape[0]/2+self.screen.height()/2),int(mote.shape[1]/2-self.screen.width()/2):int(mote.shape[1]/2+self.screen.width()/2)]
                    else:
                        blanck_image[:,int(self.screen.width()/2-mote.shape[1]/2):int(self.screen.width()/2+mote.shape[1]/2)] = mote[int(mote.shape[0]/2-self.screen.height()/2):int(mote.shape[0]/2+self.screen.height()/2),:]
                else:
                    blanck_image[int(self.screen.height()/2-mote.shape[0]/2):int(self.screen.height()/2+mote.shape[0]/2),int(self.screen.width()/2-mote.shape[1]/2):int(self.screen.width()/2+mote.shape[1]/2)] = mote
                        
                #disparo = []
                #for disparos in self.disparos:           
                #    for shot in disparos:
                #        disparo.append((float(shot['screenCoordinates'][0]),float(shot['screenCoordinates'][1])))
                #disparo.append(disparo1)
                #disparo.append(disparo2)
                #disparo.append(disparo3)

                #Evaluacion de distancias
                data = 0
                with open('ConfiguracionGral.json', 'r') as json_file:
                    data = json.load(json_file)
                Res_X = int(data['configuracion'][0]['Resoluci\u00f3n Proyector'].split('x')[0])
                Res_Y = int(data['configuracion'][0]['Resoluci\u00f3n Proyector'].split('x')[1])
                Res_X_CAM = int(data['configuracion'][0]['Resoluci\u00f3n Camara'].split('x')[0])
                Res_Y_CAM = int(data['configuracion'][0]['Resoluci\u00f3n Camara'].split('x')[1])
                
                
                width_A4 = self.widthHoja
                Tamano_Pantalla = float(data['configuracion'][0]['Ancho Pantalla [m]'])
                dist_tirador = float(data['configuracion'][0]['Distancia Tirador Pantalla'])
                dist_blanco = self.DistanciaBlanco
                TAMANO_ESCALA = float(data['configuracion'][0]['Escala Resultado'])
                
                escala = (TAMANO_ESCALA*dist_blanco)/dist_tirador
                width = (width_A4 * Res_X*TAMANO_ESCALA)/Tamano_Pantalla
                cuadrado_mote = self.CuadradoMote*TAMANO_ESCALA
                
                self.tam_cuadrado = (cuadrado_mote*Res_X) / Tamano_Pantalla
                #escala = dist_blanco/dist_tirador
                #escala = 1
                
                
                escala_proyeccion = float(Res_X_CAM/Res_X)

                self.tam_cuadrado = (cuadrado_mote*Res_X) / Tamano_Pantalla
                
                centro_y = self.screen.width()/(1 + self.CantidadTiradores) + self.offset_x
                
                self.offset_x = self.TiradorAnalizar*centro_y - self.screen.width()/2 
                
                
                disparo = []
                disparo_original = []
                for disparos in self.resultado_disparo[self.TiradorAnalizar-1]:           
                    for shot in disparos:
                        disparo_original.append((float(shot['screenCoordinates'][0]),float(shot['screenCoordinates'][1])))
                        disparo.append((((float(shot['screenCoordinates'][0]/escala_proyeccion)-Res_X/2 - self.offset_x)*escala)+Res_X/2,((float(shot['screenCoordinates'][1]/escala_proyeccion) - Res_Y/2 - self.offset_y)*escala)+Res_Y/2))
                        print ("Disparo con Escala y Offset: " + str(disparo))
                        print ("Disparo Original: " + str(disparo_original))

                print (disparo)
                
                #Esto lo tengo que mejorar es como dibuja los 6 disparos
                
                if self.CantidadDisparos == 6:
                    cv2.circle(blanck_image, (int(disparo[0][0]), int(disparo[0][1])), int(TAMANO_ESCALA*4), (255,0,0), -1 )
                    cv2.circle(blanck_image, (int(disparo[1][0]), int(disparo[1][1])), int(TAMANO_ESCALA*4), (255,0,0), -1 )
                    cv2.circle(blanck_image, (int(disparo[2][0]), int(disparo[2][1])), int(TAMANO_ESCALA*4), (255,0,0), -1 )

                    
                    cv2.circle(blanck_image, (int(disparo[3][0]), int(disparo[3][1])), int(TAMANO_ESCALA*4), (0,0,255), -1 )
                    cv2.circle(blanck_image, (int(disparo[4][0]), int(disparo[4][1])), int(TAMANO_ESCALA*4), (0,0,255), -1 )
                    cv2.circle(blanck_image, (int(disparo[5][0]), int(disparo[5][1])), int(TAMANO_ESCALA*4), (0,0,255), -1 )

                    cv2.line(blanck_image, (int(disparo[0][0]), int(disparo[0][1])), (int(disparo[1][0]), int(disparo[1][1])), (255,0,0), int(TAMANO_ESCALA*2))
                    cv2.line(blanck_image, (int(disparo[1][0]), int(disparo[1][1])), (int(disparo[2][0]), int(disparo[2][1])), (255,0,0), int(TAMANO_ESCALA*2))
                    cv2.line(blanck_image, (int(disparo[2][0]), int(disparo[2][1])), (int(disparo[0][0]), int(disparo[0][1])), (255,0,0), int(TAMANO_ESCALA*2))

                    cv2.line(blanck_image, (int(disparo[3][0]), int(disparo[3][1])), (int(disparo[4][0]), int(disparo[4][1])), (0,0,255), int(TAMANO_ESCALA*2))
                    cv2.line(blanck_image, (int(disparo[4][0]), int(disparo[4][1])), (int(disparo[5][0]), int(disparo[5][1])), (0,0,255), int(TAMANO_ESCALA*2))
                    cv2.line(blanck_image, (int(disparo[5][0]), int(disparo[5][1])), (int(disparo[3][0]), int(disparo[3][1])), (0,0,255), int(TAMANO_ESCALA*2))
                
                else:
                    for i in range(self.CantidadDisparos):
                        cv2.circle(blanck_image, (int(disparo[0][0]), int(disparo[i][1])), int(TAMANO_ESCALA*4), (255,0,0), -1 )
                #centro_rec = ((disparo1[0] + disparo2[0] + disparo3[0])/3), ((disparo1[1] + disparo2[1] + disparo3[1])/3) 
                self.centro_rec =  int(centro_x), int(centro_y)
                
                self.centro_rec =  int(self.screen.width()/2), int(self.screen.height()/2)
                self.blanck_image = blanck_image.copy()
                
                
                blanck_image = cv2.rectangle(blanck_image, (int(self.centro_rec[0] - self.tam_cuadrado/2.0),int(self.centro_rec[1] - self.tam_cuadrado/2.0)), (int(self.centro_rec[0] + self.tam_cuadrado/2.0),int(self.centro_rec[1] + self.tam_cuadrado/2.0)), (0,255,0),2)
                #blanck_image = cv2.rectangle(blanck_image, (int(self.screen.width()/2.0 - self.tam_cuadrado/2.0),int(self.screen.height()/2.0 - self.tam_cuadrado/2.0)), (int(self.screen.width()/2.0 + self.tam_cuadrado/2.0),int(self.screen.height()/2.0 + self.tam_cuadrado/2.0)), (0,255,0),2)
                
                dst2 = imutils.resize(blanck_image, width=1920)
                dst2 = cv2.cvtColor(dst2, cv2.COLOR_RGB2BGR)                        
                cv2.imshow("Resultado", dst2)
                cv2.waitKey(1)
                image = qimage2ndarray.array2qimage(blanck_image)
                self.label.setPixmap(QtGui.QPixmap.fromImage(image))
                self.timer.stop()
                jsonDatagram = {
                                "messageType":"STOP_SENSING_SHOTS"
                           }
                self.socket_madst.sendto(json.dumps(jsonDatagram).encode('utf-8'), self.udp_madst)
                self.disparos.clear()
                #self.pid.terminate()
                #self.audio.terminate()
    

    def keyPressEvent(self, event):
        #print (event.key())
        try:
            blanck_image = self.blanck_image.copy()
        
            if event.key() == QtCore.Qt.Key_Up:
                print ("Up")
                self.centro_rec= (self.centro_rec[0], self.centro_rec[1] - 1)
                
            elif event.key() == QtCore.Qt.Key_Down:
                print ("Down")
                self.centro_rec= (self.centro_rec[0], self.centro_rec[1] + 1)
                
            elif event.key() == QtCore.Qt.Key_Left:
                print("Left")
                self.centro_rec= (self.centro_rec[0] - 1, self.centro_rec[1])

            elif event.key() == QtCore.Qt.Key_Right:
                print("Right") 
                self.centro_rec= (self.centro_rec[0] + 1, self.centro_rec[1])
            
            blanck_image = cv2.rectangle(blanck_image, (int(self.centro_rec[0] - self.tam_cuadrado/2.0),int(self.centro_rec[1] - self.tam_cuadrado/2.0)), (int(self.centro_rec[0] + self.tam_cuadrado/2.0),int(self.centro_rec[1] + self.tam_cuadrado/2.0)), (0,255,0),2)
            
            dst2 = imutils.resize(blanck_image, width=1920)
            dst2 = cv2.cvtColor(dst2, cv2.COLOR_RGB2BGR) 
            cv2.imshow("Resultado", dst2)
            cv2.waitKey(1)
            image = qimage2ndarray.array2qimage(blanck_image)            
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        except:
            if event.key() == QtCore.Qt.Key_V:
                if self.PuntosVisibles:
                    self.PuntosVisibles = False
                else:
                    self.PuntosVisibles = True            
        event.accept()

    def closeEvent(self, event):
        if self.test == 1:
            self.pid.terminate()
        self.audio.terminate()
        #self.player.close_player()
        self.thread_stop = True

