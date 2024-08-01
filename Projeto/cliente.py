import json
# Modelo
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

# Persistência: Modelo -> Arquivo Json    
class Clientes:
    objetos = []               # atributo da classe e não de uma instância da classe
    @classmethod
    def inserir(cls, obj):     # create - C
        cls.abrir()
        cls.objetos.append(obj) 
        cls.salvar()
    @classmethod
    def listar(cls):           # read - R
        cls.abrir()
        return cls.objetos       
    @classmethod
    def salvar(cls):    
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("clientes.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)       

class UI:
    @staticmethod
    def menu():
        print("Clientes")
        print("  1-Inserir, 2-Listar, 9-Fim")
        return int(input())
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        a = Cliente(id, nome, email, fone)
        #p = Clientes()
        #p.inserir(a)
        Clientes.inserir(a)
    @staticmethod
    def cliente_listar():
        #p = Clientes()
        #for cliente in p.listar(): print(cliente)
        for cliente in Clientes.listar(): print(cliente)

UI.main()




      

    
