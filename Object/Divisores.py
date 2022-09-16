class Divisores:
    # Inicializo la clase Persona
    def __init__(self, montoDividido: float):
        self.montoDividido = montoDividido

    def __str__(self) -> str:
        texto = "MontoDividido: {0}"
        return texto.format(self.montoDividido)
    def __repr__(self) -> str:
        texto = "MontoDividido: {0}"
        return texto.format(self.montoDividido)

    def getMontoDividido(self) -> float:
        return self.montoDividido
    def setMontoDividido(self, nMontoDividido: float):
        self.montoDividido = nMontoDividido
