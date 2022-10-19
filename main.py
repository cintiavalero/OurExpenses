
import json
from tabulate import tabulate
from utilities import *
from TAD_LISTA import *
from Object import *
#import pickel
########## ATRIBUTOS GLOBALES ##########
FECHA=time.strftime("%d/%m/%Y", time.localtime())   # guardo la fecha actual
tituloConsola("Dividir Gastos")                     # establezco titulo consola
callHandler()                                       # handler: Ctrl+C
personas = createList()                             # creo coleccion de personas
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
    #listaNombres=[persona.getNombre() for persona in personas]
    #[persona.getNombre() for persona in personas if (persona.getNombre() != 'Pedro')]
    for persona in personas: #itero lista personas
        facturaPersonal = persona.getFacturaPersonal()
        facturaPersonal.delDetalles()
        for detalle in factura.getDetalles(): # itero los detalles de la factura general
            listaNombres=[persona.getNombre() for persona in detalle.getArticulo().getPersonas()]
            for nomPersona in listaNombres:        #itero los nombres de los detalles
                if nomPersona == persona.getNombre():   # si uno coincide con nomPersona, añado el detalle
                    facturaPersonal.addDetalle(detalle)

def verTodasFacturas():
    for persona in personas:
        factura = persona.getFacturaPersonal()
        verFactura(factura, persona.getNombre())
  
################ Articulo ################
def altaArticulo():
    clear()
    setTittle(" CARGA DE ARTICULOS ", "=")
    nombreArticulo = str(input("Nombre: "))
    precio = float(input("Precio: $"))
    #precio = float(codNumRand(3))
    cantidad = int(input("Cantidad: "))
    #cantidad = int(codNumRand(1))

    print("Que personas dividiran el gasto?")
    divisores = createList()
    print("Opciones:", verNomPersonas(personas))
    nom = input("---> ")
    if nom == '':
        for persona in personas:
            addToList(divisores, persona)
    else:
        vec = nom.split(",")
        for persona in personas:    # itero lista personas
            for nomb in vec:        # itero los nombres del vector
                if nomb == persona.getNombre():
                    addToList(divisores, persona)
    if isEmpty(divisores):
        print("algo salio mal, intenta otra vez")
    else:
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
def verFactura(factura: Factura, propietario: str):
    """Imprime en pantalla los datos de una factura"""
    clear()
    totalFactura = 0
    sumaMontoDividido = 0
    setTittle(" >>> GENERAR FACTURA >>> ", "=")
    cabecera = ["Nro Factura","Propietario","Fecha"]
    nro=int(factura.getNumero())
    fecha=str(factura.getFecha())
    fila=[nro,propietario,fecha]
    contenido = [fila]
    print(tabulate(contenido, headers=cabecera, tablefmt='psql'))
    if isEmpty(factura.getDetalles()):
        print("Atencion! Todavia no hay detalles cargados en la factura")
    else:
        contenido = []

        for detalle in factura.getDetalles():           # itero la coleccion de detalles
            fila = []
            articulo = detalle.getArticulo()            # recupero un articulo
            subtotal = detalle.calcularSubTotal()       # subtotal del detalle
            montoDividido = detalle.calcularSubTotalxPersona()
            nombreArticulo = articulo.getNombre()
            precio = detalle.getPrecio()
            cantidad = detalle.getCantidad()
            divisores = verNomPersonas(articulo.getPersonas()) # retorna los nombres de las personas
            
            fila = {"nombre":nombreArticulo, "precio":precio, "cantidad":cantidad, "subtotal":subtotal, "divisores":divisores, "subtotal/div":montoDividido}
            contenido.append(fila)

           

            totalFactura += subtotal
            sumaMontoDividido += montoDividido
            
        print(tabulate(contenido, headers="keys", tablefmt='psql'))
        #print(tabulate(contenido, headers=cabecera, tablefmt='psql'))
        if propietario == "General":
            print(">> Total: $", totalFactura)
        else:
            print(">> Total individual: $", sumaMontoDividido)
        
        
        datosFacturaCompleta = {
            "nro": nro,
            "Propietario": propietario,
            "fecha": fecha,
            "Detalles": contenido,
            "Total": totalFactura,
            "Total individual": sumaMontoDividido
        }   
        #print(datosFacturaCompleta)
        
    input()


########################################
def menu():
    """Menu principal"""
    clear()
    setTittle(" >>> MENU DE OPCIONES >>> ", "=")
    print("1) Alta Articulo.")
    print("2) Baja Articulo.")
    print("3) Desasignar persona de Articulo.")
    print("4) Ver factura.")
    print("5) Ver facturas individuales.")
    print("6) Alta Persona.")
    print("7) Baja Persona.")
    print("0) Salir.")
    try:
        res = int(input("---> "))
    except Exception as ex:
        res = 999
    return res

def verNomPersonas(listaPersonas: list[Persona]) -> list[str]:
    """Retorna una lista de nombres basada en la lista de objetos Persona"""
    listaNombres = []
    for persona in listaPersonas:
        nombre = persona.getNombre()
        listaNombres.append(nombre)
    return listaNombres


if __name__ == '__main__':
    op = 999
    while op!=0:
        try:
            op =  menu()
        except Exception as ex:
            print("\n>>>>> ERROR >>>>>", ex)
            input()
        if op == 1:
            if isEmpty(personas):   # si la lista de personas esta vacia:
                print("\nAtencion! No hay personas para asignarle a los articulos.")
                input()
            else:                   # si la lista de personas no esta vacia:
                altaArticulo()      # permito ingresar los articulos
        elif op == 2:
            if isEmpty(factura.getArticulos()):
                print("\nAtencion! No hay articulos cargados para dar de baja.")
                input()
            else:
                bajaArticulo()
        elif op == 3:
            if isEmpty(personas):
                print("\nAtencion! No hay personas cargadas para desasignar.")
                input()
            elif isEmpty(factura.getArticulos()):
                print("\nAtencion! No hay articulos cargados para desasignar una persona.")
                input()
            else:
                desasignarPersona()
        elif op == 4:
            verFactura(factura, 'General')
        elif op == 5:
            permutacion()
            verTodasFacturas()
        elif op == 6:
            clear()
            c = int(input("Cuantas personas va a ingresar?: "))
            altaPersona(c)
        elif op == 7:
            if isEmpty(personas):
                print("\nAtencion! No hay personas cargadas para dar de baja.")
                input()
            else:
                bajaPersona()

        



