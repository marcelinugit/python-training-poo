class Produto:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

p1 = Produto("Keyboard", 100)

print(p1.price)

p1.price = 250
print(p1.price)

p1.price = -10  # should raise error