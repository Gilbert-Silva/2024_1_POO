import random

class Bingo:
    def __init__(self, numBolas):
        if numBolas >= 2: self.__numBolas = numBolas
        else: raise ValueError("Número mínimo de bolas é dois")
        self.__bolas = []
    def proximo(self):
        # testa se todos os números já foram sorteados
        if len(self.__bolas) == self.__numBolas: return -1
        # sortear um número entre 1 e o numBolas
        n = random.randint(1, self.__numBolas)
        # testa se n já tinha sido sorteado
        while n in self.__bolas:
            n = random.randint(1, self.__numBolas)
        self.__bolas.append(n)
        return n
    def sorteados(self):
        self.__bolas.sort()
        return self.__bolas

class UI:
    @staticmethod
    def menu():
        print("1 - novo jogo, 2 - sortear, 3 - sorteados, 4 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: jogo = UI.novo_jogo()
            if op == 2: UI.sortear(jogo)
            if op == 3: UI.sorteados(jogo)
    @staticmethod
    def novo_jogo():
        n = int(input("Informe o número de bolas: "))
        jogo = Bingo(n)
        return jogo 
    @staticmethod
    def sortear(jogo):
        print(jogo.proximo())
    @staticmethod
    def sorteados(jogo):
        print(jogo.sorteados())

UI.main()

"""
b = Bingo(10)
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())

print(b.sorteados())

print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())

print(b.proximo())
print(b.proximo())

"""

        

