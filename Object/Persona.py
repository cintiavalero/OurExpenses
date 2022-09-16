class Persona:
    # Inicializo la clase Persona
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self) -> str:
        texto = "{0}"
        return texto.format(self.nombre)
    def __repr__(self) -> str:
        texto = "Nombre: {0}"
        return texto.format(self.nombre)

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nNombre: str):
        self.nombre = nNombre


