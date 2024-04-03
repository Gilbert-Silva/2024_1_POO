class Item:
    def __init__(self, prod, qtd, preco):
        self.__produto = prod
        self.__qtd = qtd
        self.__preco_unit = preco
        if prod == "": raise ValueError()
        if qtd <= 0: raise ValueError()
        if preco <= 0: raise ValueError()
    def set_produto(self, prod):
        self.__produto = prod
        if prod == "": raise ValueError()
    def set_qtd(self, qtd):
        self.__qtd = qtd
        if qtd <= 0: raise ValueError()
    def set_preco(self, preco):
        self.__preco_unit = preco
        if preco <= 0: raise ValueError()
    def get_produto(self):
        return self.__produto
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        return self.__preco_unit
    def total(self):
        return self.__qtd * self.__preco_unit
    def __str__(self):
        return f"{self.__produto} {self.__qtd} {self.__preco_unit}"

class Carrinho:
    def __init__(self, c, d):
        self.__cliente = c
        self.__data = d
        self.__itens = []
        if c == "": raise ValueError()
    def inserir(self, item):
        self.__itens.append(item)
    def remover(self, item):
        self.__itens.remove(item)
    def listar(self):
        return self.__itens
    def total(self):
        t = 0
        for item in self.__itens:
            t += item.total()    
        return t
    def __str__(self):
        return f"{self.__cliente} {self.__data} {len(self.__itens)} item(s)"

a = Item("Biscoito", 5, 2.5)
b = Item("Maça", 10, 2)
c = Item("Laranja", 5, 1)
print(a, a.total())
print(b, b.total())
print(c, c.total())

carrinho = Carrinho("Jorgiano", "03/04/2024")
carrinho.inserir(a)
carrinho.inserir(b)
carrinho.inserir(c)
carrinho.remover(a)
print(carrinho)
for item in carrinho.listar(): print(item)
print(carrinho.total())


    
