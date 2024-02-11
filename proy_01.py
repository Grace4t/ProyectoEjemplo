import os
#variables
DIRECTORIO = "dir/"
EXTENCION = ".txt"

def mostrar_menu():
    print("SELECCIONE UNA OPCIÓN DEL MENÚ")
    print("1. Crear platillo")
    print("2. Editar platillo")
    print("3. Mostrar platillo")
    print("4. Buscar platillo")
    print("5. Eliminar platillo")
    

def crear_carpeta():
    try:
        os.path.exists(DIRECTORIO)
        os.makedirs(DIRECTORIO)
    except OSError as error:
        print(f"La carpeta llamada {DIRECTORIO} fue creada exitosamente")

def app():
    crear_carpeta()
    mostrar_menu()

app()