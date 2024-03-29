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
def eliminar_platillo():
    eliminar = input("Escribe el platillo que deseas eliminar: \r\n") 
    try:
        os.remove(DIRECTORIO +eliminar+ EXTENSION)
        print(f"PLATILLO ' {eliminar} ' FUE ELIMINADO CORRECTAMENTE")
    except:
        print(f"ERROR, EL CONTACTO NO EXISTE {IOError}")
    app()
def buscar_platillo():
    nombre_buscar = input("Escribe el nombre del platillo que deseas buscar: \r\n") 
    try:
        with open(DIRECTORIO+nombre_buscar+EXTENSION) as archivo:
            print("platillo encontrado!")
            for linea in archivo:
                print(linea.rstrip())
    except IOError:
        print(f"ERROR, EL CONTACTO NO EXISTE {IOError}")
    app()
        
def mostrar_platillo():
    # 1.-ASEGURARNOS DE QUE EXISTA EL PLATILLO
    nombre_anterior = input("Escribe el nombre que desea editar: \r\n") #Nombre del archivo/platillo
    existe = existe_platillo(nombre_anterior)
    if existe:
        #LEER EL ARCHIVO SE LECCIONADO
        with open (DIRECTORIO + nombre_anterior + EXTENSION) as archivo:
            print(archivo.read())
    else:
        print("No existe")
def editar_menu():
    #Que platillo se desea editar
    nombre_anterior = input("Escribe el nombre que desea editar: \r\n") #Nombre del archivo/platillo
    existe = existe_platillo(nombre_anterior)
    #crear el archivo con el nombre del archivo
    if existe:
        #print("Si existe el archivo, usted puede agregar comentarios al platillo")
        with open(DIRECTORIO + nombre_anterior + EXTENSION, "a+") as archivo:
            nombre_platillo= input("\r\Agregar un nombre: \r\n")
            ingredientes_platillo= input("\r\Agregar un Ingrediente: \r\n")
            termino_platillo= input("\r\Agregar un termino: \r\n")
            categoria_platillo= input("\r\Agregar una categoria: \r\n")
            #Instanciar el construcor de la clase 
            platillo = Platillo(nombre_platillo, ingredientes_platillo, termino_platillo, categoria_platillo)
            archivo.write("Area modificada: " + platillo.nombre + "\r") 
            archivo.write("Area modificada: " + platillo.ingredientes + "\r") 
            archivo.write("Area modificada: " + platillo.termino + "\r") 
            archivo.write("Area modificada: " + platillo.categoria + "\r") 
            print("\r\n Comentarios agregados exitosamente")                  
    else:
        print("Ese platillo no existe, no puede ser modificado")
    app()
def crear_platillo():
    nombre_platillo = input("Escribe el nombre: \r\n") #Nombre del archivo/platillo
    existe = existe_platillo(nombre_platillo)
    #crear el archivo con el nombre del archivo
    if not existe:
        with open(DIRECTORIO + nombre_platillo + EXTENSION, "w") as archivo:
            #Escribir los otros campos en el archivo creado
            nombre_platillo = input("Escribe el nombre del platillo: \r\n")
            ingredientes_platillo = input("Escribe los ingredientes del platillo: \r\n")
            termino_platillo = input("Escribe el termino del platillo: \r\n")
            categoria_platillo = input("Escribe la categoria del platillo: \r\n")
            #Instanciar el construcor de la clase 
            platillo = Platillo(nombre_platillo, ingredientes_platillo, termino_platillo, categoria_platillo)

            #Todavia no escribe porque no le hemos mandado los  datos al método para guardalos
            #referencia a la Class Contacto NombredelObjeto.Nombredelatributo
            archivo.write("El nombre del platillo es: "+ platillo.nombre + "\r")
            archivo.write("Los ingredientes son: " + platillo.ingredientes + "\r")
            archivo.write("El termino del platillo es: " + platillo.termino + "\r")
            archivo.write("La categoria de comida es: " + platillo.categoria + "\r")
    else:
        print("El platilla ya esta creado")
    app()

def mostrar_menu():
    print("**********BIENVENIDO AL MENÚ**********")
    print("1. Crear platillo")
    print("2. Editar platillo")
    print("3. Mostrar platillo")
    print("4. Buscar platillo")
    print("5. Eliminar platillo \n")
    
def seleccionar_opcion():
    pregunta = True
    while pregunta == True:
        opcion = int(input("Selecciona una opción del Menú:\r\n"))
        if opcion == 1:
            crear_platillo()
            pregunta == False
        elif opcion == 2:
            editar_menu()
            pregunta ==  False
        elif opcion == 3:
            mostrar_platillo()
            pregunta ==  False
        elif opcion == 4:
            buscar_platillo()
            pregunta ==  False
        elif opcion == 5:
            eliminar_platillo()
            pregunta ==  False
        else:
            print(f"Opción no valida")
def crear_carpeta():
    try:
        os.path.exists(DIRECTORIO)
        os.makedirs(DIRECTORIO)
    except OSError as error:
        #print(f"La carpeta llamada {DIRECTORIO} fue creada exitosamente\r\n")
        print("\r")

def existe_platillo(nombre):
   return os.path.isfile(DIRECTORIO + nombre + EXTENSION)

def app():
    crear_carpeta()
    mostrar_menu()
    seleccionar_opcion()
    editar_menu()
    
app()