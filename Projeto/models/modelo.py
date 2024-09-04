# Persistência: Modelo -> Arquivo Json  
from abc import ABC, abstractmethod 

class Modelo(ABC):

    objetos = []                # atributo da classe e não de uma instância da classe

    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de clientes do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id             # novo objeto recebe o id calculado
        cls.objetos.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo

    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.objetos  

    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.objetos:   # percorre a lista procurando o objeto com o id informado
            if x.id == id: return x
        return None      

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass    

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

