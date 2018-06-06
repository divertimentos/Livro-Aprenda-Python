def owner(dona):
    print("Resposta correta, %s. Você é a garota mais bonita da cidade. \n" %dona)

while True:
    nome = input("Digite seu nome e descubra se você é a garota mais bonita da cidade: \n")
    if nome == "Luiza":
        owner("Luiza")
        break
    else:
        print("Resposta errada, %s. Tente novamente." %nome.capitalize())
