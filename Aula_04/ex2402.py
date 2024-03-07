n = int(input())

k = 0 # divisores de n, excetuando 1 e n
rn = int(n**0.5)
for d in range(2, rn + 1):
    if n % d == 0: k += 1

if k == 0: print("N") # n é primo, não tem como dividir em linhas e colunas
else: print("S")

