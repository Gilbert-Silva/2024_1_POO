import random

numeros = []
numBolas = 10
k = 0
s = 0
while k < numBolas:
    n = random.randint(1, numBolas)
    s += 1
    if n not in numeros:
        numeros.append(n)
        k += 1

print(numeros)
print(s)

