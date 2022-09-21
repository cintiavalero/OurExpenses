from Object import Articulo


class FacturaDetalle:
    # Inicializo la clase FacturaDetalle
    def __init__(self, articulo: Articulo, cantidad: int, precio: float):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio

    
    def __str__(self) -> str:
        texto = "Cantidad: {0}    Precio: $ {1}    Articulo: {2}"
        return texto.format(self.cantidad, self.precio, self.articulo)
    def __repr__(self) -> str:
        texto = "Cantidad: {0}    Precio: $ {1}    Articulo: {2}\n"
        return texto.format(self.cantidad, self.precio, self.articulo)

    def getArticulo(self) -> Articulo:
        return self.articulo    
    def getCantidad(self) -> int:
        return self.cantidad
    def getPrecio(self) -> float:
        return self.precio
    def getPersonas(self):
        return self.articulo.getPersonas()
    def setArticulo(self, nArticulo: Articulo):
        self.articulo = nArticulo
    def setCantidad(self, nCantidad: int):
        self.cantidad = nCantidad
    def setPrecio(self, nPrecio: float):
        self.precio = nPrecio

    # funcion calcular para calcular el subtotal del detalle
    def calcularSubTotal(self) -> float:
        return self.cantidad * self.precio
 
    def calcularSubTotalxPersona(self) -> float:
        return round(self.calcularSubTotal()/len(self.articulo.getPersonas()), 2)