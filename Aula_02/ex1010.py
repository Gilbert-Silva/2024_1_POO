linha1 = input()
linha2 = input()
peca1 = linha1.split()
peca2 = linha2.split()
n1 = int(peca1[1])
v1 = float(peca1[2])
n2 = int(peca2[1])
v2 = float(peca2[2])
t = n1*v1 + n2*v2
print(f"VALOR A PAGAR: R$ {t:.2f}")



