import os
#variables
DIRECTORIO = "dir/"
EXTENSION = ".txt"

class Platillo:
    def __init__(self,nombre,ingredientes, termino, categoria):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.termino = termino
        self.categoria = categoria
        
def crear_platillo():
    nombre_platillo = input("Escribe el nombre del platillo:")
    existe = existe_platillo(nombre_platillo)
    #crear el archivo con el nombre del archivo
    if not existe:
        with open(DIRECTORIO + nombre_platillo + EXTENSION, "w") as archivo:
            archivo.write()#Aqui no le estoy mandado nada para que escriba, por lo que hay que llamar a la clase con sus atributos
            #Escribir los otros campos en el archivo creado
            ingredientes_platillo = input("Escribe los ingredientes del platillo: \r\n")
            termino_platillo = input("Escribe el termino del platillo: \r\n")
            categoria_platillo = input("Escribe la categoria del platillo: \r\n")
            #Instanciar el construcor de la clase 
            platillo = Platillo(nombre_platillo, ingredientes_platillo, termino_platillo, categoria_platillo)

            #Todavia no escribe porque no le hemos mandado los  datos al método para guardalos
            #referencia a la Class Contacto NombredelObjeto.Nombredelatributo
            archivo.write(platillo.ingredientes)
            archivo.write(platillo.termino)
            archivo.write(platillo.categoria)
            #Mostrar mensaje  
            print("\r\nContacto Agregado Exitosamente\r\n")               
    else:
        print("El contacto ya existe.")

    
        print("El platilla ya esta creado")


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

def existe_platillo(nombre):
   return os.path.isfile(DIRECTORIO + nombre + EXTENSION)

def app():
    crear_carpeta()
    mostrar_menu()
    seleccionar_opcion()
    
app()