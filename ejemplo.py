
class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, valor):
        self.resultado += valor
        return self.resultado

    def restar(self, valor):
        self.resultado -= valor
        return self.resultado
