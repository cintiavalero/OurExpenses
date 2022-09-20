from utilities import *
from TAD_LISTA import *
from Object import *

########## ATRIBUTOS GLOBALES ##########
FECHA=time.strftime("%d/%m/%Y", time.localtime())   # guardo la fecha actual
tituloConsola("Dividir Gastos")                     # establezco titulo consola
callHandler()                                       # handler: Ctrl+C
personas = createList()                             # creo coleccion de personas
burbujas = []                             # creo una 'burnuja' que contiene listas de divisores.
#tickets = createList()                             # creo coleccion de tickets
factura = Factura(FECHA,1,0)                        # creo la factura principal
clear()                                             # limpio pantalla
########################################
################ Persona ################
def altaPersona(cant: int):
    clear()
    setTittle(" >>> CARGA DE PERSONAS >>> ", "=")
    aux = 0
    while aux < cant:
        # Se establecen los datos del objeto
        nombre = str(input("Nombre: "))
        facturaPersonal = Factura(FECHA, codNumRand(2), 0)
        # Se crea un objeto 'Persona' con los datos anteriores
        persona = Persona(nombre, facturaPersonal)
        # Se agrega el objeto en la coleccion de personas
        addToList(personas, persona)
        aux += 1
def bajaPersona():
    clear()
    setTittle(" >>> BAJA DE PERSONAS >>> ", "=")
    print("Personas actuales:", personas)
    nombre = str(input("Ingrese el nombre de la persona a dar de baja: "))
    for persona in personas:
        if nombre == persona.getNombre():
                removeElemList(personas, persona)
                print("Persona eliminada correctamente")
    input()

################ Divisores ################

def permutacion():
    for persona in personas: #itero lista personas
        facturaPersonal = persona.getFacturaPersonal()
        for detalle in factura.getDetalles(): # itero los detalles de la factura general
            for nomPersona in detalle.getNomPersonas():        #itero los nombres de los detalles
                if nomPersona == persona.getNombre():   # si uno coincide con nomPersona, añado el detalle
                    facturaPersonal.addDetalle(detalle)
                    
        print(persona.getFacturaPersonal())

def verTodasFacturas():
    for persona in personas:
        factura = persona.getFacturaPersonal()
        verFactura(factura)
    
################ Articulo ################
def altaArticulo():
    clear()
    setTittle(" CARGA DE ARTICULOS ", "=")
    nombreArticulo = str(input("Nombre: "))
    #precio = float(input("Precio: $"))
    precio = float(codNumRand(3))
    #cantidad = int(input("Cantidad: "))
    cantidad = int(codNumRand(1))

    print("Que personas dividiran el gasto?")
    divisores = createList()
    nombre = Persona.getNomPersonas(personas)
    print("Opciones:", nombre)
    nom = input("---> ")
    vec = nom.split(",")
    for persona in personas:    # itero lista personas
        for nomb in vec:        # itero los nombres del vector
            if nomb == persona.getNombre():
                addToList(divisores, persona)
    
    # Creo un articulo con nombre y personas asociadas
    articulo = Articulo(nombreArticulo, divisores)
    
    # Creo un detalle con un articulo asociado
    detalle = FacturaDetalle(articulo, cantidad, precio)
    factura.addDetalle(detalle)

def bajaArticulo():
    clear()
    aux = 0
    setTittle(" >>> BAJA DE ARTICULO >>> ", "=")
    print("Articulos actuales:", factura.getNomArticulos())
    nombreArticulo = str(input("Articulo a eliminar: "))
    for detalle in factura.getDetalles():
        if nombreArticulo == detalle.getArticulo().getNombre():
            factura.delDetalle(detalle)
            print("Articulo eliminado correctamente!"); aux = 1
    if aux == 0: print("Atencion! No se ha encontrado el articulo ingresado.") 
    input()

def desasignarPersona():
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    print("Articulos:", factura.getNomArticulos())
    nombreArticulo = str(input("Ingrese el nombre del articulo: "))
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    for detalle in factura.getDetalles():       # itero la coleccion de detalles
        articulo = detalle.getArticulo()        # recupero un articulo
        if nombreArticulo == articulo.getNombre():
            print("Articulo encontrado:", articulo.getNombre())
            print("Que usuario se debe eliminar?:", articulo.getPersonas())
            personaAeliminar=str(input("---> "))
            for persona in articulo.getPersonas():
                if personaAeliminar == persona.getNombre():
                    articulo.getPersonas().remove(persona)
                    print("Persona/s desasignada/s correctamente")
                    # tambien se puede negar la condicion del if y cargar una lista nueva que luego se carga al objeto.
    input()
################ Factura ################
def verFactura(factura: Factura):
    clear()
    setTittle(" >>> GENERAR FACTURA >>> ", "=")
    print("Factura nro:", factura.getNumero(), "    Fecha:", factura.getFecha())
    print("Detalle:")
    if isEmpty(factura.getDetalles()):
        print("Atencion! Todavia no hay detalles cargados en la factura")
    else:
        for detalle in factura.getDetalles():           # itero la coleccion de detalles
            articulo = detalle.getArticulo()            # recupero un articulo
            subtotal = detalle.calcularSubTotal()       # subtotal del detalle
            print(" Articulo:", articulo.getNombre(),   
            "    Precio: $", detalle.getPrecio(), "    Cantidad:", detalle.getCantidad(),
            "    Divisores:", articulo.getPersonas(),
            "    Subtotal: $", subtotal,
            "    Cada uno paga: $", detalle.calcularSubTotalxPersona())   # imprimo los datos del articulo y del detalle.
    input()



########################################
def menu():
    clear()
    setTittle(" >>> MENU DE OPCIONES >>> ", "=")
    print("1) Alta Articulo.")
    print("2) Baja Articulo.")
    print("3) Desasignar persona de Articulo.")
    print("4) Ver factura.")
    print("5) Alta Persona.")
    print("6) Baja Persona.")
    print("0) Salir.")
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
                altaArticulo()      # permito ingresar los articulos
        elif op == 2:
            bajaArticulo()
        elif op == 3:
            desasignarPersona()
        elif op == 4:
            verFactura(factura)
        elif op == 5:
            clear()
            c = int(input("Cuantas personas va a ingresar?: "))
            altaPersona(c)
        elif op == 6:
            bajaPersona()
        elif op == 7:
            verTodasFacturas()
        



