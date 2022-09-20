from Object import Persona, Factura, FacturaDetalle
class Persona:
    # Inicializo la clase Persona
    def __init__(self, nombre: str, facturaPersonal: Factura):
        self.nombre = nombre
        self.facturaPersonal = facturaPersonal

    def __str__(self) -> str:
        texto = "{0}"
        return texto.format(self.nombre)
    def __repr__(self) -> str:
        texto = "Nombre: {0}"
        return texto.format(self.nombre)

    def getNombre(self) -> str:
        return self.nombre
    def getFacturaPersonal(self) -> Factura:
        return self.facturaPersonal
    def getNomPersonas(self, personas: list[Persona]) -> list[str]:
        listaNombres = []
        for persona in personas:
            nombre = persona.getNombre()
            listaNombres.append(nombre)
        return listaNombres
    
    def addDetalle(self, nDetalle: FacturaDetalle):
        self.facturaPersonal.addDetalle(nDetalle)
    def setNombre(self, nNombre: str):
        self.nombre = nNombre
    def setFacturaPersonal(self, nFacturaPersonal: Factura):
        self.facturaPersonal = nFacturaPersonal

    



