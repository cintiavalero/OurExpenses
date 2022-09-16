class GastoPersonal:
    def __init__(self, inversion: float, gastoAPagar: float):
        self.inversion = inversion
        self.gastoAPagar = gastoAPagar

    def __str__(self) -> str:
        texto = "Inversion: {0}    GastoFinal: {1}"
        return texto.format(self.inversion, self.gastoAPagar)
    def __repr__(self) -> str:
        texto = "Inversion: {0}    GastoFinal: {1}"
        return texto.format(self.inversion, self.gastoAPagar)