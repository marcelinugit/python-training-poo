class Carro: # cria classe
    def __init__(self, marca, modelo, ano):
        # inicializa construtor!
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # this em java : pyhton self

carro1 = Carro("Porsche", "911", 2021)
# instancia a classe!
print(f"Descrição rápida: {carro1.modelo}, {carro1.ano}, {carro1.marca}")

carro2 = Carro("BMW", "X6", 2022)
# instancia a classe!
print(f"Descrição rápida: {carro2.modelo}, {carro2.ano}, {carro2.marca}")

