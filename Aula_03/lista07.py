def iniciais(nome):
    excecoes = ["da", "do", "das", "dos", "de", "e"]
    palavras = nome.split() # lista de palavras do nome
    r = "" # string com iniciais começa vazia
    for palavra in palavras: # recupera cada palavra do nome
        if palavra not in excecoes:
            r += palavra[0]
    return(r)

def formatar_nome(nome):
    excecoes = ["da", "do", "das", "dos", "de", "e"]
    nome = nome.lower()
    palavras = nome.split() # lista de palavras do nome
    r = "" # string com nome formatado
    for palavra in palavras: # recupera cada palavra do nome
        if palavra in excecoes:
            r += palavra + " "
        else:
            r += palavra.capitalize() + " "
    return(r)

nome = input("Digite seu nome: ")
print(iniciais(nome))
print(formatar_nome(nome))




