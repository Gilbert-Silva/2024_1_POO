class Aluno:
    # método especial usado para definir os atributos
    def __init__(self):
        self.nome = ""        # atributo
        self.matricula = ""   # atributo
    # método da classe aluno
    def ano_ingresso(self):
        ano_str = self.matricula[0:4]
        ano_int = int(ano_str)
        return ano_int

# Prog. Estruturada
# função - operação não está dentro de um tipo de variável
def func_ano_ingresso(aluno):
    ano_str = aluno.matricula[0:4]
    ano_int = int(ano_str)
    return ano_int


a = Aluno() # __init__ é chamado de forma invisível
b = Aluno()
c = a

a.nome = "aluno 1"
a.matricula = "20232014040001"
b.nome = "aluno 2"
b.matricula = "20232014040002"

#print(a.nome, a.matricula)
#print(b.nome, b.matricula)
turma = [a, b, c]
for aluno in turma:
    print(id(aluno), aluno.nome, aluno.matricula, aluno.ano_ingresso(), func_ano_ingresso(aluno))





