import math

class Equacao:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
    def set_a(self, a):
        if a != 0: self.__a = a
        else: raise ValueError("Coeficiente a não pode ser zero")
    def set_b(self, b):
        self.__b = b
    def set_c(self, c):
        self.__c = c
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def tem_raizes_reais(self):
        return self.delta() >= 0
    def raiz1(self):
        if self.tem_raizes_reais():
            return (-self.__b + math.sqrt(self.delta())) / (2 * self.__a)
        return "Não tem raiz real"
    def raiz2(self):
        if self.tem_raizes_reais():
            return (-self.__b - math.sqrt(self.delta())) / (2 * self.__a)
        return "Não tem raiz real"
    def __str__(self):
        s = f"{self.__a}*x^2"
        if self.__b >= 0: s += f" +{self.__b}*x"
        else: s += f" {self.__b}*x"
        if self.__c >= 0: s += f" +{self.__c}"
        else: s += f" {self.__c}"
        return s
    
class UI:
    @staticmethod
    def main():
        op = 10
        while op != 2:
            op = UI.menu()
            if op == 1: UI.nova_equacao()
    @staticmethod
    def menu():
        print("1 - Nova equação, 2 - Fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def nova_equacao():
        print("Programa para calcular as raízes de uma equação do 2º grau")
        a = float(input("Informe o valor de a: "))
        b = float(input("Informe o valor de b: "))
        c = float(input("Informe o valor de c: "))
        eq = Equacao(a, b, c)
        print(eq)
        print(eq.tem_raizes_reais())
        print(eq.delta())
        print(eq.raiz1())
        print(eq.raiz2())

UI.main()        




                 
