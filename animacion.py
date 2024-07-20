import time
import os

# Ancho del área de la consola
ancho = 40

# Símbolo de la flecha
flecha = "→"

# Mensaje
mensaje = "Liz, te quiero muchísimo!"

# Limpiar la pantalla de la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mover la flecha de izquierda a derecha con el mensaje
def animar_flecha():
    for i in range(ancho):
        limpiar_pantalla()
        print(" " * i + flecha + " " + mensaje)
        time.sleep(0.1)

# Ejecutar la animación
animar_flecha()
