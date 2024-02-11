import os
#variables
DIRECTORIO = "dir/"
EXTENCION = ".txt"

def crear_carpeta():
    try:
        os.path.exists(DIRECTORIO)
        os.makedirs(DIRECTORIO)
    except OSError as error:
        print("carpeta creada")

def app():
    crear_carpeta()

app()