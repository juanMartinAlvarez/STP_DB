def resDefault():
	#ResolucionCamara
	#ResolucionProyector 
	#TiempoExposicion [us]
	#TeimpoLaserOn [us]
	#CantidadTiradores
	#DistanciaTiradorPantalla 
	DEFAULT_CONFIG = ["3840x2160","3840x2160", "10000", "3000", "4", "10"]
	return DEFAULT_CONFIG

def resCam():
	RESOLUCIONES_CAM = ["640x480", "800x600", "1280x720","1920x1080","3840x2160", "1280x1024"]
	return RESOLUCIONES_CAM

def resProy():
    RESOLUCIONES_PROY = ["640x480", "800x600", "1280x720","1920x1080","3840x2160", "1280x1024"]
    return RESOLUCIONES_PROY

	
def cantTiradores():
	CANTIDAD_TIRADORES =["1","2","3","4","5","6","7","8","9","10"]
	return CANTIDAD_TIRADORES
