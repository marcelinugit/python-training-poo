class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            return False

        if self.saldo < valor:
            return False

        self.saldo -= valor
        return True

    def mostrar_saldo(self):
        return self.saldo


conta1 = ContaBancaria("Gustavo Marcelino", 2000)

ok = conta1.depositar(500)
print(ok)  # True

ok = conta1.sacar(3000)
print(ok)  # False

print(conta1.mostrar_saldo())  # 2500

# Note: mostrar_saldo() retornando valor é melhor que printar,
# porque você pode usar em qualquer lugar (print, relatório, interface, etc).

