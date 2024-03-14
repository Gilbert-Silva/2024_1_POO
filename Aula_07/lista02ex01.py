import math
# modelo
class Circulo:  
    def __init__(self):     # construtor
        self.__raio = 0
    def set_raio(self, r):  # métodos de acesso
        if r < 0: raise ValueError()
        self.__raio = r
    def get_raio(self):
        return self.__raio   
    def calc_area(self):
        return math.pi * self.__raio ** 2 
    def calc_circ(self):
        return 2 * math.pi * self.__raio 

# UI    
class UI: # html, xml 
    def menu():
        print("Figuras Geométricas")
        print("1 - Novo círculo")
        print("9 - Fim")
        op = int(input("Escolha uma opção: "))
        return op
    def novo_circulo():
        print("Você escolheu Círculo")
        r = float(input("Informe o raio do círculo: "))
        x = Circulo()
        x.set_raio(r)
        print(f"Raio = {x.get_raio()}")
        print(f"Área = {x.calc_area()}")
        print(f"Circ = {x.calc_area()}")
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.novo_circulo()
        print("Volte sempre!")

        """    
        x = Circulo()  # __init__
        y = Circulo()
        print(id(x))
        print(id(y))
        x.set_raio(10)          #set
        y.set_raio(5)
        print(x.get_raio())      #get
        print(y.get_raio())
        print(x.calc_area())
        print(x.calc_circ())
        """   

UI.main()
