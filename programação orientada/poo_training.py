# ANOTA ISSO: todo método dentro da classe tem self como primeiro parâmetro.
class Car:
    def __init__(self, modelo, ano, marca):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def description(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")



c1 = Car("X7", 2024, "Bmw")
c2 = Car("911", 2022, "Porsche")
c1.description()
c2.description()