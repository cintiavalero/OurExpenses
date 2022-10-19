from Object import FacturaDetalle, Articulo
from datetime import datetime

class Factura:
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
    def getArticulos(self) -> list[Articulo]: # Retorna una lista de Articulos
        listaArticulos = []
        for detalle in self.getDetalles():
            articulo = detalle.getArticulo()
            listaArticulos.append(articulo)
        return listaArticulos
    def getNomArticulos(self) -> list[str]: # Retorna una lista con los nombres de los Articulos
        listaArticulos = []
        for detalle in self.getDetalles():
            articulo = detalle.getArticulo().getNombre()
            listaArticulos.append(articulo)
        return listaArticulos
    def setFecha(self, nFecha: datetime):
        self.fecha = nFecha
    def setNumero(self, nNumero: int):
        self.numero = nNumero
    def setImporteTotal(self, nImporteTotal: float):
        self.importeTotal = nImporteTotal
    def setDetalles(self, nDetalles: FacturaDetalle):
        self.detalles = nDetalles
    def addDetalle(self, nDetalle: FacturaDetalle):
        self.detalles.append(nDetalle)
    def delDetalle(self, rDetalle: FacturaDetalle):
        self.detalles.remove(rDetalle)
    def delDetalles(self):
        self.detalles.clear()
