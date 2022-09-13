import utilities, TAD_LISTA, objetos
from utilities import *
from TAD_LISTA import *
from objetos import *
########## ATRIBUTOS GLOBALES ##########
FECHA=time.strftime("%d/%m/%Y", time.localtime())   # guardo la fecha actual
tituloConsola("Dividir Gastos")                     # establezco titulo consola
callHandler()                                       # handler: Ctrl+C
personas = createList()                             # creo coleccion de personas
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
        inversion = float(input("Inversion inicial: $"))
        diferencia = 0.00
        # Se crea un objeto 'Persona' con los datos anteriores
        persona = Persona(nombre, inversion, diferencia)
        # Se agrega el objeto en la coleccion de personas
        addToList(personas, persona)
        aux += 1

def desasignarPersona():
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    nombreArticulo = str(input("Ingrese el nombre del articulo: "))
    clear()
    setTittle(" >>> DESASIGNAR PERSONA >>> ", "=")
    for detalle in factura.getDetalles():       # itero la coleccion de detalles
        articulo = detalle.getArticulo()        # recupero un articulo
        if nombreArticulo == articulo.getNombre():
            print("Articulo encontrado:", articulo.getNombre())
            print("Que usuario se debe eliminar?:", articulo.getPersonas())
            personaAeliminar=str(input("---> "))
            for p in articulo.getPersonas():
                if personaAeliminar == p.getNombre():
                    articulo.getPersonas().remove(p)

            #articulo.desasignar(personaAeliminar)
            #print(articulo.getPersonas())

        #for persona in articulo.getPersonas():  # itero dentro de la coleccion de personas
        #    if nom == persona.getNombre():      # busco si 'nom' coincide con el nombre de la persona
        #        pass
    input()

def altaArticulos():
    clear()
    setTittle(" CARGA DE ARTICULOS ", "=")
    nombre = str(input("Nombre: "))
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad: "))
    # Creo un articulo con nombre y personas asociadas
    articulo = Articulo(nombre, personas)   # probar añadir uno por uno
    # Creo un detalle con un articulo asociado
    detalle = FacturaDetalle(cantidad, precio, articulo)
    factura.addDetalle(detalle)

def verFactura():
    clear()
    setTittle(" >>> GENERAR FACTURA >>> ", "=")
    print("Factura nro:", factura.getNumero(), "    Fecha:", factura.getFecha())
    print("Detalle:")
    
    for detalle in factura.getDetalles():           # itero la coleccion de detalles
        articulo = detalle.getArticulo()            # recupero un articulo
        print(" Articulo:", articulo.getNombre(),   
        "    Precio: $", detalle.getPrecio(), "    Cantidad:", detalle.getCantidad(),
        "    Divisores:", articulo.getPersonas())   # imprimo los datos del articulo y del detalle.
    
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



