import utilities, TAD_LISTA, objetos
from utilities import *
from TAD_LISTA import *
from objetos import *
########## ATRIBUTOS GLOBALES ##########
FECHA=time.strftime("%d/%m/%Y", time.localtime())   # guardo la fecha actual
tituloConsola("Dividir Gastos")                     # establezco titulo consola
callHandler()                                       # handler: Ctrl+C
personas = createList()                             # creo coleccion de personas
divisores = createList()
#tickets = createList()                             # creo coleccion de tickets
factura = Factura(FECHA,1,0)                        # creo la factura principal
clear()                                             # limpio pantalla
########################################
def altaPersona(cant: int):
    clear()
    setTittle(" >>> CARGA DE PERSONAS >>> ", "=")
    aux = 0
    while aux < cant:
        # Se establecen los datos del objeto
        nombre = str(input("Nombre: "))
        #inversion = float(input("Inversion inicial: $"))
        inversion = float(codNumRand(3))
        diferencia = 0.00
        # Se crea un objeto 'Persona' con los datos anteriores
        persona = Persona(nombre, inversion, diferencia)
        # Se agrega el objeto en la coleccion de personas
        addToList(personas, persona)
        aux += 1

def desasignarPersona():
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    nombres = []
    for persona in personas:
        nombres.append(persona.getNombre())
    print("Articulos:", nombres)
    nombreArticulo = str(input("Ingrese el nombre del articulo: "))
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    for detalle in factura.getDetalles():       # itero la coleccion de detalles
        articulo = detalle.getArticulo()        # recupero un articulo
        if nombreArticulo == articulo.getNombre(): # si nomArticulo = a algun nombre de articulo:
            print("Articulo encontrado:", articulo.getNombre())
            print("Que usuario se debe eliminar?:", articulo.getPersonas())
            personaAeliminar=str(input("---> "))

            for divisor in articulo.getPersonas():
                if divisor.getNombre() == personaAeliminar:
                    articulo.getPersonas().remove(divisor)

            

            #articulo.desasignar(personaAeliminar)
            #print(articulo.getPersonas())

        #for persona in articulo.getPersonas():  # itero dentro de la coleccion de personas
        #    if nom == persona.getNombre():      # busco si 'nom' coincide con el nombre de la persona
        #        pass
    input()

def altaArticulos():
    clear()
    setTittle(" CARGA DE ARTICULOS ", "=")
    nombreArticulo = str(input("Nombre: "))
    #precio = float(input("Precio: $"))
    precio = float(codNumRand(3))
    #cantidad = int(input("Cantidad: "))
    cantidad = int(codNumRand(1))

    print("Que personas dividiran el gasto?")
    nombres = []
    clearList(divisores)
    for persona in personas:
        nombres.append(persona.getNombre())
    print("Opciones:", nombres)
    nom = input("--->")
    vec = nom.split(",")
    for persona in personas:    # itero lista personas
        for i in vec:        # itero los nombres del vector
            if i == persona.getNombre():
                addToList(divisores, persona)
    
    # Creo un articulo con nombre y divisores asociados
    articulo = Articulo(nombreArticulo, divisores)
    # Creo un detalle con un articulo asociado
    detalle = FacturaDetalle(cantidad, precio, articulo)
    factura.addDetalle(detalle)
    clearList(divisores)

def verFactura():
    clear()
    setTittle(" >>> GENERAR FACTURA >>> ", "=")
    print("Factura nro:", factura.getNumero(), "    Fecha:", factura.getFecha())
    print("Detalle:")
    
    for detalle in factura.getDetalles():           # itero la coleccion de detalles
        articulo = detalle.getArticulo()            # recupero un articulo
        nombres=[]
        for i in articulo.getPersonas():
            nombres.append(i.getNombre())
        print(" Articulo:", articulo.getNombre(),   
        "    Precio: $", detalle.getPrecio(), "    Cantidad:", detalle.getCantidad(),
        "    Divisores:", nombres)   # imprimo los datos del articulo y del detalle.
    
    input()



def menu():
    clear()
    setTittle(" >>> MENU DE OPCIONES >>> ", "=")
    print("1) Cargar Articulo.")
    print("2) Desasignar persona de Articulo.")
    print("3) Ver factura.")
    print("5) Cargar Persona.")
    print("0) Salir")
    res = int(input("---> "))
    return res

if __name__ == '__main__':
    op = 1
    while op!=0:
        op = menu()
        if op == 1:
            if isEmpty(personas):   # si la lista de personas esta vacia:
                print("\nAtencion! No hay personas para asignarle a los articulos.")
                input()
            else:                   # si la lista de personas no esta vacia:
                altaArticulos()     # permito ingresar los articulos
        elif op == 2:
            desasignarPersona()
        elif op == 3:
            verFactura()
        elif op == 5:
            clear()
            c = int(input("Cuantas personas va a ingresar?: "))
            altaPersona(c)
        elif op == 4:
            pass



