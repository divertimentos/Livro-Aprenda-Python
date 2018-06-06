string12 = "Olá, meu nome é Geraldão de Rívia."
substring1 = "meu"

print(string12.find(substring1)) #Retornará 5, pois "m" é o 5o índice.

substring2 = "José"
print(string12.find(substring2)) #Retornará "-1" porque "José" não é uma substring de string12.

print(string12.find(substring1, 2)) #Essa parte eu sinceramente não entendi.
