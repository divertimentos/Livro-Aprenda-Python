#Concatenação de strings:

nome = 'Geralt de Rívia'
idade = 30

print("Olá, meu nome é " + nome)

#Convertendo um número em string para que ele caiba dentro da concatenação:

print("Olá, meu nome é " + nome + "e tenho " + str(idade) + " anos.")

#Chamando números decimais usando o str():

valor = 503.78987
print("O valor é " + str(valor))

print("O valor é " + format(valor, '.2f')) #Note que a função format já retorna uma string, não havendo aqui a necessidade de converter o resultado em string usando a funçao str.
