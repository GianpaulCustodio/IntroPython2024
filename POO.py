import os
import time

class Ordenador:
    #Método Constructor
    def __init__(self, nombre_carpeta):
        self.nombre_carpeta = nombre_carpeta

    #Acciones
    def crear_carpeta(self):
        os.mkdir(self.nombre_carpeta)

    def eliminar_carpeta(self):
        os.rmdir(self.nombre_carpeta)

usuario1 = Ordenador("carpetita")
usuario1.crear_carpeta()
time.sleep(3)
usuario1.eliminar_carpeta()