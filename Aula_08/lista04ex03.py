class Cliente:
    def __init__(self, nome, cpf, limite):  # x = Cliente("nome", "cpf", 1000)
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
    def set_socio(self, c):  # x.set_socio(y)
        eu = self
        voce = c
        if eu.__socio != None: # eu já tenho sócio -> meu sócio vai deixar de ter sócio
            meu_socio = eu.__socio
            meu_socio.__socio = None
        if voce.__socio != None:
            voce_socio = voce.__socio
            voce_socio.__socio = None    
        eu.__socio = voce    # self.__socio = c
        voce.__socio = eu    # c.__socio = self
    def get_limite(self):
        if self.__socio == None:
            return self.__limite
        else:
            meu_socio = self.__socio
            return self.__limite + meu_socio.__limite  # self.__socio.__limite 
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome} - limite pessoal: {self.__limite}" 
        else:
            a = f"{self.__nome} - limite pessoal: {self.__limite} "
            b = f"- sócio: {self.__socio.__nome} - limite sociedade: {self.get_limite()}" 
            return a + b

x = Cliente("Eduardo", "123456789", 1000)
y = Cliente("Marília", "987654321", 2000)
z = Cliente("Jorgiano", "98769876", 3000)
t = Cliente("Gilbert", "98989898", 1500)
x.set_socio(y)
z.set_socio(t)
print(x)
print(y)
print(z)
print(t)
z.set_socio(x)
print()
print(x)
print(y)
print(z)
print(t)



