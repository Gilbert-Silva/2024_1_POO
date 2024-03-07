import math
# Model
class Circulo:
    def __init__(self, raio): # encapsulamento
        #self.__raio = raio    # atributos ficam escondidos
        #if raio < 0: raise ValueError()
        self.set_raio(raio)
    def set_raio(self, raio):
        self.__raio = raio    # atributos ficam escondidos
        if raio < 0: raise ValueError()
    def get_raio(self):
        return self.__raio    
    def area(self):
        return math.pi * self.__raio ** 2
    def circunferencia(self):
        return 2 * math.pi * self.__raio

# UI
print("Digite o raio de um círculo")
r = int(input())
c = Circulo(r)  # c = Circulo.__init__(c)
#c.raio = r
print("Raio =", c.get_raio())
print("Área =", c.area())
print("Circunferência =", c.circunferencia())
print("Digite um valor novo para o raio")
r = int(input())
#c = Circulo(r) - cria outro objeto círculo
c.set_raio(r) # alterando um objeto círculo existente
print("Raio =", c.get_raio())
print("Área =", c.area())
print("Circunferência =", c.circunferencia())

#print(math.sqrt(10))


#Eduarda
#Pedro Henrique
#Wesley


