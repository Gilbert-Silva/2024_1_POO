import math

class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def __str__(self):
        bstr = f"+{self.__b}"
        if self.__b < 0: bstr = f"{self.__b}"
        cstr = f"+{self.__c}"
        if self.__c < 0: cstr = f"{self.__c}"
        return f"{self.__a}*x² {bstr}*x {cstr}"
    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def tem_raizes_reais(self):
        return self.delta() >= 0
    def x1(self):
        if self.tem_raizes_reais():
            return (-self.__b + math.sqrt(self.delta())) / (2 * self.__a)
    def x2(self):
        if self.tem_raizes_reais():
            return (-self.__b - math.sqrt(self.delta())) / (2 * self.__a)
    def y(self, x):
        return self.__a * x**2 + self.__b * x + self.__c    
        
        