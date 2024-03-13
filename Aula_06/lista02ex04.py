class Ingresso:
    def __init__(self):
       self.__dia = "dom"
       self.__horario = 0
    def set_dia(self, dia):
       dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
       if dia in dias: self.__dia = dia
       else: raise ValueError() 
    def set_horario(self, horario):   
       if 0 <= horario <= 23: self.__horario = horario
       else: raise ValueError()
    def get_dia(self):
       return self.__dia
    def get_horario(self):
       return self.__horario
    def inteira(self):
       if self.__horario <= 17: return 10
       else: return 20
    def meia(self):
       return self.inteira() / 2   

x = Ingresso()
x.set_dia("seg")
x.set_horario(22)
print(x.get_dia())
print(x.get_horario())
print(x.inteira())
print(x.meia())
y = x
y.set_horario(10)
print(x.inteira())

