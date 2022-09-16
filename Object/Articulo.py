from Object import Persona

class Articulo:
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
