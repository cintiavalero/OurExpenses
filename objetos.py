import time, utilities
class Persona:
    # Inicializo la clase padre con __init__
    def __init__(self, nombre, inversion, diferencia):
        self.nombre = nombre
        self.inversion = inversion
        self.diferencia = diferencia

    def __str__(self) -> str:
        texto = "Nombre: {0}\nInversion: ${1}"
        return texto.format(self.nombre, self.inversion)
    # get()
    def getNombre(self):
        return self.nombre
    def getInversion(self):
        return self.inversion
    def getDiferencia(self):
        return self.diferencia # si 'diferencia < 0', el valor es negativo, por lo tanto tiene el modulo de ese valor a favor


    # imprimirDatos()
    def getAll(self):
        print("Nombre:", self.getNombre())
        print("Inversion: $", self.getInversion())
        if self.getDiferencia() < 0:
            print("Debe: $", round(self.getDiferencia() * -1, 2))
        if self.getDiferencia() >= 0:
            print("Se le debe: $", round(self.getDiferencia(), 2))

    def getAllVar(self):
        reg = [self.getNombre(), self.getInversion(), self.getDiferencia()]
        return reg
        
    # modDato()
    def modNombre(self, nNombre):
        self.nombre = nNombre
    def modInversion(self, nInversion):
        self.inversion = nInversion
    def modDiferencia(self, nDiferencia):
        self.diferencia = nDiferencia

class Factura:
    # Inicializo la clase padre con __init__
    def __init__(self, fecha, numero, importeTotal):
        self.fecha = fecha
        self.numero = numero
        self.importeTotal = importeTotal
        self.detalles = []

    def __str__(self) -> str:
        texto = "Factura nro: {0}\nFecha: {1}\nImporte Total: {2}\nFactura Detalle: [{3}]"
        return texto.format(self.numero, self.fecha, self.importeTotal, self.det())

    def getFecha(self):
        return self.fecha
    def getNumero(self):
        return self.numero
    def getImporteTotal(self):
        return self.importeTotal
    def getDetalle(self):
        return self.detalles
    def det(self):
        for detalle in self.detalles:
            return detalle
    def setFecha(self, nFecha):
        self.fecha = nFecha
    def setNumero(self, nNumero):
        self.numero = nNumero
    def setImporteTotal(self, nImporteTotal):
        self.importeTotal = nImporteTotal
    def setDetalle(self, nDetalle):
        self.detalles = nDetalle
    def addDetalle(self, nDetalle):
        self.detalles.append(nDetalle)


class FacturaDetalle():
    def __init__(self, cantidad, precio, articulo):
        self.cantidad = cantidad
        self.precio = precio
        self.articulo = articulo
    
    def __str__(self) -> str:
        texto = "Cantidad: {0}\n Precio: $ {1}\nArticulo: [{2}]"
        return texto.format(self.cantidad, self.precio, self.articulo)
    

    def getCantidad(self):
        return self.cantidad
    def getPrecio(self):
        return self.precio
    def getArticulo(self):
        return self.articulo
    def setCantidad(self, nCantidad):
        self.cantidad = nCantidad
    def setPrecio(self, nPrecio):
        self.precio = nPrecio
    
    # funcion calcular precio pra la suma
    def calcularPrecio(self):
        return self.cantidad * self.precio
        
class Articulo():
    def __init__(self, nombre, personas):
        self.nombre = nombre
        self.personas = personas
    def __str__(self) -> str:
        texto = "Nombre: {0}\nPersonas: {1}"
        return texto.format(self.nombre, self.det())
    def getPersonas(self):
        for persona in self.personas:
            return persona
    def getNombre(self):
        return self.nombre
    #def getPrecio(self):
        #return self.precioA

    def setNombre(self, nNombre):
        self.nombre = nNombre
    #def setPrecio(self, nPrecioA):
        #self.precioA = nPrecioA

utilities.clear()
FECHA=time.strftime("%d/%m/%Y", time.localtime())
factura = Factura(FECHA,1,0)# creo la factura
p1=Persona("Mateo", 100, 0) # persona
p2=Persona("Juan", 130, 0) # persona
personas=[p1, p2] # lista de personas
art1=Articulo("Leche", personas) # articulo
art2=Articulo("Azucar", personas) # articulo
art3=Articulo("Pan", personas) # articulo
articulos=[art1, art2, art3] # lista de articulos
c1=2
c2=2
c3=1
p1=35
p2=20
p3=50
detalle1 = FacturaDetalle(c1, p1, art1)
detalle2 = FacturaDetalle(c2, p2, art2)
detalle3 = FacturaDetalle(c3, p3, art3)
factura.addDetalle(detalle1)
factura.addDetalle(detalle2)
factura.addDetalle(detalle3)

for detalle in factura:
    print(detalle)

#print(factura)