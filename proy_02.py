import os

class Carpetas:
    def __init__(self,nombre):
        self.nombre = nombre

def crear_carpeta():
    #necesito directorio
    #crear un directorio con with y despues checar si ya existe ese direcionro
    carpeta = input("ingresa el nombre de la carpeta: ")
    car_prin = carpeta+"/"
    print(car_prin)
    if not os.path.exists(car_prin):
        os.makedirs(car_prin)

    
def app():
    #print("App principal!")
    crear_carpeta()
app()