class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old"

p1 = Person("Marcelinuu", 20)
print(p1.introduce())

p2 = Person("Mary", 22)
print(p2.introduce())