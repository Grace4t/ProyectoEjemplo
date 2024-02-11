import os
#variables
DIRECTORIO = "dir/"
EXTENCION = ".txt"

def crear_platillo():
    print("Desde crear platillo")

def mostrar_menu():
    print("SELECCIONE UNA OPCIÓN DEL MENÚ")
    print("1. Crear platillo")
    print("2. Editar platillo")
    print("3. Mostrar platillo")
    print("4. Buscar platillo")
    print("5. Eliminar platillo")
    
def seleccionar_opcion():
    pregunta = True
    while pregunta == True:
        opcion = int(input("Selecciona una opción del Menú:"))
        if opcion == 1:
            crear_platillo()
            pregunta == False
        elif opcion == 2:
            print("Editar platillo")
            pregunta ==  False
        elif opcion == 3:
            print("Mostrar platillo")
            pregunta ==  False
        elif opcion == 4:
            print("Buscar platillo")
            pregunta ==  False
        elif opcion == 5:
            print("Eliminar platillo")
            pregunta ==  False
        else:
            print(f"Opción no valida")
def crear_carpeta():
    try:
        os.path.exists(DIRECTORIO)
        os.makedirs(DIRECTORIO)
    except OSError as error:
        print(f"La carpeta llamada {DIRECTORIO} fue creada exitosamente\r\n")

def app():
    crear_carpeta()
    mostrar_menu()
    seleccionar_opcion()
    #crear_platillo()

app()