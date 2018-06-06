while True:
    nome = input("Digite seu nome ou sair para terminar o programa: ")
    if nome == "sair":
        print("Mensagem automática: O programa foi encerrado. \n")
        break
    else:
        print ("Olá, %s!" %nome)

        #A continuação é minha:

        if input != "sair":
            print("\nO que você deseja?")
            break
