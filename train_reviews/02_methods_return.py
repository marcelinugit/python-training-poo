class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):

        if b == 0:
            return ValueError("Erro: Divisão por zero!")
        return a / b

calc = Calculadora()
print(calc.somar(0, 10))
print("A divisão: {:2f}".format(calc.divisao(7, 2)))
print(calc.divisao(10, 0))