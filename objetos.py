from datetime import datetime

# cambiar lista e personas a obj detalle y precio a obj articulo

class Persona():
    # Inicializo la clase Persona
    def __init__(self, nombre: str, inversion: float, diferencia: float):
        self.nombre = nombre
        self.inversion = inversion
        self.diferencia = diferencia

    def __str__(self) -> str:
        texto = "{0}"
        return texto.format(self.nombre)
    def __repr__(self) -> str:
        texto = "{0}"
        return texto.format(self.nombre)

    def getNombre(self) -> str:
        return self.nombre
    def getInversion(self) -> float:
        return self.inversion
    def getDiferencia(self) -> float:
        return self.diferencia # si 'diferencia < 0', el valor es negativo, por lo tanto tiene el modulo de ese valor a favor
    def setNombre(self, nNombre: str):
        self.nombre = nNombre
    def setInversion(self, nInversion: float):
        self.inversion = nInversion
    def setDiferencia(self, nDiferencia: float):
        self.diferencia = nDiferencia

    # imprimirDatos()
    def getAll(self):
        print("Nombre:", self.getNombre())
        print("Inversion: $", self.getInversion())
        if self.getDiferencia() < 0:
            print("Debe: $", round(self.getDiferencia() * -1, 2))
        if self.getDiferencia() >= 0:
            print("Se le debe: $", round(self.getDiferencia(), 2))
 
class Articulo():
    # Inicializo la clase Articulo
    def __init__(self, nombre: str, personas: list[Persona]):
        self.nombre = nombre
        self.personas = personas
    def __str__(self) -> str:
        texto = "{0}    Divisores: {1}"
        return texto.format(self.nombre, self.personas)
    def __repr__(self) -> str:    # para debug
        texto = " {0} \tDivisores: {1}"
        return texto.format(self.nombre, self.personas)
    def getPersonas(self) -> list[Persona]:
        return self.personas
    def getNomPersonas(self):
        nombres=[]
        for persona in self.personas:
            nombres.append(persona.getNombre())
        return nombres
    def getNombre(self) -> str:
        return self.nombre
    def setNombre(self, nNombre: str):
        self.nombre = nNombre
    def setPersonas(self, nListaPersonas: list[Persona]): # con *args, admite varios argumentos
        self.personas = nListaPersonas
    def desasignar(self, nomPersona: str):
        for p in self.getPersonas():
            if nomPersona == p.getNombre():
                self.getPersonas().remove(p)

class FacturaDetalle():
    # Inicializo la clase FacturaDetalle
    def __init__(self, cantidad: int, precio: float, articulo: Articulo):
        self.cantidad = cantidad
        self.precio = precio
        self.articulo = articulo
    
    def __str__(self) -> str:
        texto = "Cantidad: {0}    Precio: $ {1}    Articulo: {2}"
        return texto.format(self.cantidad, self.precio, self.articulo)
    def __repr__(self) -> str:
        texto = "Cantidad: {0}    Precio: $ {1}    Articulo: {2}\n"
        return texto.format(self.cantidad, self.precio, self.articulo)
    
    def getCantidad(self) -> int:
        return self.cantidad
    def getPrecio(self) -> float:
        return self.precio
    def getArticulo(self) -> Articulo:
        return self.articulo
    def setCantidad(self, nCantidad: int):
        self.cantidad = nCantidad
    def setPrecio(self, nPrecio: float):
        self.precio = nPrecio

    # funcion calcular para calcular el subtotal del detalle
    def calcularSubTotal(self) -> float:
        return self.cantidad * self.precio
     
class Factura():
    # Inicializo la clase Factura
    def __init__(self, fecha: datetime, numero: int, importeTotal: float):
        self.fecha = fecha
        self.numero = numero
        self.importeTotal = importeTotal
        self.detalles = []

    def __str__(self) -> str:
        texto = "Factura nro: {0}    Fecha: {1}    Importe Total: {2}\nDetalle:\n    {3} "
        return texto.format(self.numero, self.fecha, self.importeTotal, self.getDetalles())

    def getFecha(self) -> datetime:
        return self.fecha
    def getNumero(self) -> int:
        return self.numero
    def getImporteTotal(self) -> float:
        return self.importeTotal
    def getDetalles(self) -> list[FacturaDetalle]:
        return self.detalles
    def setFecha(self, nFecha: datetime):
        self.fecha = nFecha
    def setNumero(self, nNumero: int):
        self.numero = nNumero
    def setImporteTotal(self, nImporteTotal: float):
        self.importeTotal = nImporteTotal
    def setDetalle(self, nDetalle: FacturaDetalle):
        self.detalles = nDetalle
    def addDetalle(self, nDetalle: FacturaDetalle):
        self.detalles.append(nDetalle)

