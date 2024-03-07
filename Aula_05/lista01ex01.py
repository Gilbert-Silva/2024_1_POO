import math
# Model
class Circulo:
    def __init__(self):
        self.raio = 0    # atributos ficam escondidos
    def area(self):
        return math.pi * self.raio ** 2
    def circunferencia(self):
        return 2 * math.pi * self.raio

# UI
print("Digite o raio de um círculo")
r = int(input())
c = Circulo()
c.raio = r
print("Raio =", c.raio)
print("Área =", c.area())
print("Circunferência =", c.circunferencia())
#print(math.sqrt(10))



