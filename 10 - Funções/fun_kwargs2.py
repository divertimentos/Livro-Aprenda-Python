def print_info(nome, idade, **kwargs):
    print("Informações básicas: \n")
    print("nome:" + nome)
    print("idade:" + str(idade))
    print("\nInformações adicionais:\n")
    for parametro, valor in kwargs.items():
        print(parametro + ": " + str(valor) + ".")

print_info(nome = "Luiza", idade = 20, nacionalidade = "Brasileira", time = "Ponte Preta")

#A chave "time = Ponte Preta" fui eu quem adicionei. Entendi que o "**kwargs" me possibilita isso. Preciso entender melhor esse conceito.
