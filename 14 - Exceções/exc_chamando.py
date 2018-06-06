nome = input("Qual o seu nome? ")
try:
    if nome == "Guilherme":
        raise NameError("Não gostei do seu nome.")
    print("Olá, %s." %nome)
except NameError:
    print("O programa não gostou do seu nome.")
