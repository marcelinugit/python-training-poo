class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor


# Teste
p1 = Produto("Teclado", 100)

print(p1.preco)

p1.preco = 200
print(p1.preco)

p1.preco = -10  # erro