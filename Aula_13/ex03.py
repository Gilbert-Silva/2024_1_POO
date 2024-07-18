from datetime import datetime

hoje = datetime.now()
nasc = datetime.strptime("07/09/2004", "%d/%m/%Y")
idade = hoje - nasc
dias = idade.days
anos = idade.days // 365
dias_sobrando = idade.days % 365
meses = dias_sobrando // 30
print(dias)
print(anos)
print(meses)

print(hoje.year, hoje.month)
print(nasc.year, nasc.month)
anos = hoje.year - nasc.year
meses = hoje.month - nasc.month
if meses < 0: 
    anos -= 1
    meses += 12
print(anos)
print(meses)





