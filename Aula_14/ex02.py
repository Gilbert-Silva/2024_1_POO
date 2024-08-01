import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

def salvar_arquivo():    
    a = Cliente(1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")  
    #print(a.__dict__)
    #print(vars(b))
    clientes = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(clientes, arquivo, default = vars)

def abrir_arquivo():
    clientes = []
    with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
            c = Cliente(obj["id"], obj["nome"])
            clientes.append(c)
    for c in clientes: 
        print(c)        
    
#salvar_arquivo()
abrir_arquivo()



