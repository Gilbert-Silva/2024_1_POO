def tautograma(s):
    s = s.upper() # passa a string para maiúsculo
    palavras = s.split() # divide a string em uma lista de palavras
    letra = palavras[0][0] # recupera a inicial da primeira palavra
    iguais = True # supõe que as iniciais são iguais
    for palavra in palavras: # recupera cada palavra da lista
        inicial = palavra[0] # recupera a inicial de cada palavra
        if inicial != letra: iguais = False # testa a inicial de cada palavra
        if not iguais: break
    return iguais

s = input()
while s != "*":
    print("Y" if tautograma(s) else "N")
    s = input()
