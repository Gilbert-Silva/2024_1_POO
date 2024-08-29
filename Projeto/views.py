from models.cliente import Cliente, Clientes

class View:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        if nome == "": raise ValueError("Nome inválido")
        if email == "": raise ValueError("E-mail inválido")
        a = Cliente(0, nome, email, fone)
        Clientes.inserir(a)
    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)
    @staticmethod
    def cliente_excluir(id):
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)


    
    