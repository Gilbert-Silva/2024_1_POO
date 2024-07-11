class Disciplina:
    def __init__(self, nome, semestre, media, ch):
        self.__nome = nome
        self.__semestre = semestre
        self.__media = media
        self.__ch = ch
        self.__aprovado = media >= 60
    def get_semestre(self):
        return self.__semestre  
    def get_media(self):
        return self.__media        
    def __str__(self):
        if self.__aprovado:
            return f"{self.__nome}-{self.__semestre}-{self.__media}-{self.__ch} - aprovado"
        else:    
            return f"{self.__nome}-{self.__semestre}-{self.__media}-{self.__ch} - reprovado"

class Historico:
    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []
    def inserir(self, disc):
        self.__disciplinas.append(disc)
    def listar(self):
        return self.__disciplinas
    def listar_semestre(self, semestre):
        x = []
        for disc in self.__disciplinas:
            if disc.get_semestre() == semestre:
                x.append(disc)
        return x        
    def IRA(self):
        if len(self.__disciplinas) == 0: return 0
        soma = 0
        for disc in self.__disciplinas:
            soma += disc.get_media()
        return soma / len(self.__disciplinas)

h = Historico("aluno")
a = Disciplina("POO", "2024.1", 100, 90)
b = Disciplina("Assembly", "2024.1", 50, 60)
c = Disciplina("Inglês", "2023.2", 90, 60)
h.inserir(a)
h.inserir(b)
h.inserir(c)
print("Todas as disciplinas")
for disc in h.listar():
    print(disc)
print("Disciplinas do semestre 2024.1")
for disc in h.listar_semestre("2024.1"):
    print(disc)
print(f"IRA = {h.IRA()}")


