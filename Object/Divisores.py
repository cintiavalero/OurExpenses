from Object import Persona
class Divisores:
    # Inicializo la clase Persona
    def __init__(self, montoDividido: float, grupo: list[Persona]):
        self.montoDividido = montoDividido
        self.grupo = grupo

    def __str__(self) -> str:
        texto = "MontoDividido: {0} ; Grupo: {1}"
        return texto.format(self.getMontoDividido(), self.getGrupo())
    def __repr__(self) -> str:
        texto = "MontoDividido: {0} ; Grupo: {1}"
        return texto.format(self.getMontoDividido(), self.getGrupo())

    def getMontoDividido(self) -> float:
        return self.montoDividido
    def getGrupo(self) -> list[Persona]:
        return self.grupo

    def setGrupo(self, nGrupo: list[Persona]):
        self.grupo = nGrupo    
    def setMontoDividido(self, nMontoDividido: float):
        self.montoDividido = nMontoDividido
