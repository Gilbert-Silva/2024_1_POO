class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
print(x)
print(x.calc_area())
x.b = float(input("Informe o valor da base: "))
x.h = float(input("Informe o valor da altura: "))
print(x.calc_area())

