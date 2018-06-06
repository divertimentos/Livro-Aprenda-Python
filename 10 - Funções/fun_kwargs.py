def print_info(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro + ": " + str(valor) + ".")

print_info(nome = "Felipe", idade = 30, nacionalidade = "Brasileiro")

#Ainda não estou 100% com as propriedades do for.
