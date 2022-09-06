import utilities, TAD_LISTA, objetos
from utilities import *
from TAD_LISTA import *
from objetos import *

FECHA=time.strftime("%d/%m/%Y", time.localtime())
tituloConsola("Dividir Gastos")
callHandler()
clear()
personas = createList() # creo coleccion de personas
#tickets = createList() # creo coleccion de tickets
factura = Factura(FECHA,1,0) # creo la factura principal

def altaPersona(cant):
    clear()
    setTittle(" >>> CARGA DE PERSONAS >>> ", "=")
    aux = 0
    while aux < cant:
        # Se establecen los datos del objeto
        nombre = input("Nombre: ")
        inversion = float(input("Inversion inicial: $"))
        diferencia = 0.00
        # Se crea un objeto 'Persona'
        persona = Persona(nombre, inversion, diferencia)
        # Se agrega el objeto en la coleccion de personas
        addToList(personas, persona)
        aux += 1

def altaArticulos():
    clear()
    setTittle(" CARGA DE ARTICULOS ", "=")
    nombre = str(input("Nombre: "))
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad: "))
    # Creo un articulo con nombre y personas asociadas
    for persona in personas:
        articulo = Articulo(nombre, persona)
    # Creo un detalle con un articulo asociado
    detalle = FacturaDetalle(cantidad, precio, articulo)
    factura.addDetalle(detalle)

def calcularImporteTotal():
    for detalle in 10:
        importe = detalle

def verFactura():
    clear()
    print("Factura: ", factura.getNumero())
    print("Fecha: ", factura.getFecha())
    print("Importe Total: ", factura.getImporteTotal())
    print("Detalle: ")
    #facturaDetalle= factura.getDetalle()
    #for detalle in facturaDetalle: # itero en la coleccion de Detalles
    #    print("="*10)
    #    print(detalle)
        #suma de los precio*cantidad de cada detalle
    #print(factura)   
    
    for detalle in factura.getDetalle():
        for persona in detalle.articulo.getPersonas(): # detalle.articulo.getPersonas(), devuelve una lista? o devuelve una persona por iteracion?
            if persona.getNombre() = detalle.articulo.getPersonas():
                pass
        total = detalle.getPrecio() * detalle.getCantidad()
        factura.setImporteTotal(total)

        
    input()



def resto():    

    # Pregunto el total y cant personas a añadir
    setTittle("  CARGA DE DATOS  ", "=")
    compra = float(input("Monto total pagado: $"))
    cantPersonas = int(input("A dividir entre: "))
    altaPersona(cantPersonas)

    altaArticulos()

    # calculo el monto total que debe pagar cada uno
    cantIguales = round(compra/size(personas), 2)

    # defino la cantidad inicial antes de la suma
    cantInicial = 0.00

    for i in range(0, size(personas)):
        # sumo la cantidad de dinero acumulada
        cantInicial += float(Persona.getInversion(personas[i]))

    clear() # limpio pantalla

    vuelto = round(cantInicial - compra, 2)
    if vuelto < 0:
        print("\nError --> vuelto < 0\n La cantidad de dinero acumulado debe ser igual o mayor al gasto.\n") # si vuelto < 0, el dinero acumulado no es suficiente para pagar.
        input()
        exit(1)

    # genero un ticket
    setTittle("            TICKET           ", "=")
    print("Cant. dinero acumulado: $", cantInicial)
    print("Gasto total: $", compra)
    print("Gasto dividido entre: ", cantInicial)
    print("Cada uno paga: $", cantIguales)
    print("Vuelto: $", vuelto)


    for i in range(0, size(personas)):
        diferencia = 0.00
        # calculo la diferencia inversion - cantIguales para ver si se le debe dinero o debe dinero
        diferencia = round(float(Persona.getInversion(personas[i])) - cantIguales, 2)
        Persona.modDiferencia(personas[i], diferencia)
        print("="*29)
    Persona.getAll(personas[i])
    print("="*29)

def menu():
    clear()
    setTittle(" >>> MENU DE OPCIONES >>> ", "=")
    print("1) Cargar Articulo.")
    print("2) Modificar Articulo.")
    print("3) Ver factura.")
    print("5) Cargar Persona.")
    print("0) Salir")
    res = int(input("---> "))
    return res

def main():
    op = 1
    while op!=0:
        op = menu()
        if op == 1:
            if size(personas) > 0: 
                altaArticulos()
            else:
                print("\nAtencion! No hay personas para asignar a los articulos.")
                input()
        elif op == 5:
            clear()
            c = int(input("Cuantas personas va a ingresar?: "))
            altaPersona(c)
        elif op == 3:
            verFactura()
        elif op == 4:
            pass



main()
