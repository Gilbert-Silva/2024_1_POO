x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife", 0 : "Teste"}
y = ["Natal", "João Pessoa", "Recife"]
z = {}

print(x)
print(type(x))
print(x["RN"])
print(x[0])  # apenas chaves para indexar o dicionário

print(y)
print(type(y))
print(y[0])

print(type(z))

y[0] = "Manaus"
print(y)

#y[4] = "Manaus"

x["AM"] = "Manaus"
print(x)
print(*x)
#print(**x)

for item in x.items(): 
    print(item, type(item))

z = ("AM", "Manaus")
print(z)
print(z[0])
print(z[1])
print(type(z))

#z[0] = "RN"  # as tuplas são imutáveis






