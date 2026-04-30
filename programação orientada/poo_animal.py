# SuperClasse
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som Genérico")


# herança é quando uma classe “herda” atributos e métodos de outra.

# SubClasse
class Cachorro(Animal):
    def falar(self):
        print("Au-Au")
        # override é quando a classe filha redefine um metodo da classe pai.


class Gato(Animal):
    def falar(self):
        print("Miau-Miau")
        # override é quando a classe filha redefine um metodo da classe pai.

dog = Cachorro("Orion")
print(dog.nome)
dog.falar()

cat = Gato("Apollo")
print(cat.nome)
cat.falar()

class Vaca(Animal):
    def falar(self):
        print("Muu")

cow = Vaca("Muh")
print(cow.nome)
cow.falar()

# super() serve para acessar a classe pai dentro da classe filha.
