class Triangulo:
    def __init__(self, b, h):
        #self.__b = b
        #self.__h = h
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    def __str__(self):
        return f"Triangulo com base = {self.__b} e altura = {self.__h}"

class UI:
    @staticmethod
    def main():
        x = Triangulo(10, 20)
        print(x)
        print(f"Um triângulo de base {x.get_base()} e altura {x.get_altura()}")
        print(f"tem área = {x.calc_area()}")

        print("Digite o valor da base: ")
        x.set_base(float(input()))
        print("Digite o valor da altura: ")
        x.set_altura(float(input()))
        print(f"Um triângulo de base {x.get_base()} e altura {x.get_altura()}")
        print(f"tem área = {x.calc_area()}")

UI.main()