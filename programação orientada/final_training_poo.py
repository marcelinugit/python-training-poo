class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo.")
        self._salario = valor

    def mostrar_dados(self):
        return f"Funcionário: {self.nome} | Salário: {self.salario}"

    def bonus(self):
        return 0


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_dados(self):
        return f"Gerente: {self.nome} | Departamento: {self.departamento} | Salário: {self.salario}"

    def bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def bonus(self):
        return self.salario * 0.05


# Working..
g1 = Gerente("Ana", 5000, "TI")
e1 = Estagiario("Marcelinuu", 2000)

print(g1.mostrar_dados())
print("Bônus:", g1.bonus())

print(e1.mostrar_dados())
print("Bônus:", e1.bonus())