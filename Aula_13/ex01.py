#import math
#print(math.sqrt(16))
#from math import sqrt
#print(sqrt(16))

#import datetime
#a = datetime.datetime(2024, 7, 18)
#print(a)

from datetime import datetime, timedelta
a = datetime(2024, 7, 18)
print(a)
b = datetime(2023, 6, 1, 9, 30, 15)
print(b)

# método estáticos da classe datetime
c = datetime.today()
d = datetime.now()
print(c)
print(d)

# Conversão de texto para data usando strptime
#s = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
s = "18/07/2024"
f = datetime.strptime(s, "%d/%m/%Y")
print(f)

# atributos - acesso com uma instância da classe
print(f.day)
print(f.month)
print(f.year)
print(f.hour)
print(f.minute)
print(f.second)

# métodos de instância
g = datetime.now()
print(g)
print(g.day)      # atributo
print(g.month)
print(g.year)
print(g.hour)
print(g.minute)
print(g.second)
print(g.date())   # método
print(g.time())
print(g.weekday())

# conversão de data para texto usando strftime
print(g.strftime("%d/%m/%Y %H:%M"))
print(g.strftime("%A, %d/%B/%y"))

t1 = timedelta(days=1, hours=10)
t2 = timedelta(hours=3, minutes=30, seconds=10)
t3 = timedelta(1, 3600)
print(t1) 
print(t2) 
print(t3)

h = datetime.now()
i = timedelta(days = 30)

for k in range(9):
    print(h)
    h = h + i

intervalo = "10:30"
x = intervalo.split(":")
print(x)
print(type(int))
h = int(x[0])
m = int(x[1])
h, m = map(int, x)
print(h, m)

t1 = timedelta(hours=1, minutes=35)
t2 = timedelta(minutes=30)
t3 = t1 + t2
print(t1)
print(t2)
print(t3)

hoje = datetime.now()
nasc = datetime.strptime("27/04/2004", "%d/%m/%Y")
vida = hoje - nasc
print(vida)






















