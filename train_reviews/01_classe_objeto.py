class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


c1 = Carro("Porsche", "911", 2022)
c2 = Carro("BMW", "X6", 2024)

print(c1.descricao())
print(c2.descricao())