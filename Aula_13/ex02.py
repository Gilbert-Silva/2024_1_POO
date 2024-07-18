from enum import Enum, IntFlag

class Estacao(Enum):
  OUTONO = 1
  INVERNO = 2
  PRIMAVERA = 3
  VERAO = 4

a = Estacao.INVERNO
b = Estacao["VERAO"]
c = Estacao(3)
print(a) # Estacao.INVERNO
print(b) # Estacao.VERAO
print(c) # Estacao.PRIMAVERA
print(type(a))

class Dia(IntFlag):
  Domingo = 1          # 0000.0001
  Segunda = 2          # 0000.0010
  Terca = 4            # 0000.0100
  Quarta = 8           # 0000.1000
  Quinta = 16          # 0001.0000
  Sexta = 32           # 0010.0000
  Sabado = 64          # 0100.0000

a = Dia(0)
b = Dia.Sexta
c = Dia.Segunda | Dia.Sexta    # ou binário  0010.0010
d = Dia.Sabado | Dia.Domingo
print(a) # Dia.0
print(b) # Dia.Sexta
print(c) # Dia.Sexta|Segunda
print(d) # Dia.Sabado|Domingo

