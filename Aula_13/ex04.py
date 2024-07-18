from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, nascimento):
        if nome == "": raise ValueError("Nome informado é inválido")
        # if nascimento > datetime.now() - timedelta(days = 365): raise ValueError("Data deve ter pelo menos 1 ano")
        if nascimento > datetime.now() : raise ValueError("Data de nascimento não pode ser no futuro")
        self.__nome = nome
        self.__nascimento = nascimento
    def idade(self):
        hoje = datetime.now()
        idade = hoje - self.__nascimento
        anos = idade.days // 365
        meses = (idade.days % 365) // 30
        return f"{anos} ano(s) e {meses} mes(es)"
    def __str__(self):
        return f"{self.__nome} - Nascimento {self.__nascimento.strftime('%d/%m/%Y')}"

#data1 = datetime.strptime("10/07/2023", "%d/%m/%Y")  # mais de um ano
#data2 = datetime.strptime("10/08/2023", "%d/%m/%Y")  # menos de um ano
#data3 = datetime.strptime("10/08/2024", "%d/%m/%Y")  # nascimento no futuro
data = datetime.strptime("10/07/1970", "%d/%m/%Y")  # mais de um ano
p1 = Paciente("Eduardo", data)
print(p1)
print(p1.idade())



