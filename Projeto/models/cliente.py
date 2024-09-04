import json
from models.modelo import Modelo

# Modelo - POJO POCO
class Cliente:
    def __init__(self, id, nome, email, fone):
        if nome == "": raise ValueError("Nome inválido")
        if email == "": raise ValueError("E-mail inválido")
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone
    #def get_senha(self): return self.senha

    def set_id(self, id): self.id = id
    def set_nome(self, nome): self.nome = nome
    def set_email(self, email): self.email = email
    def set_fone(self, fone): self.fone = fone
    #def set_senha(self, senha): self.senha = senha    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

# Persistência: Herdar da classe Modelo     
class Clientes(Modelo):

    @classmethod
    def salvar(cls):    
        with open("../clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("../clientes.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                  cls.objetos.append(c)
        except FileNotFoundError:
          pass                   
