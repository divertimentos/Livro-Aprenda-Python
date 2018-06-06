def owner(dona):
    print("Seja bem-vinda, %s. Parabéns por ser a garota mais bonita de Sanca." %dona)


name = input("Responda: Quem é a garota mais bonita de Sanca? \n")
if name != "Luiza":
    print("Seja bem-vindo(a), visitante %s." %name.capitalize())

if name == "Luiza":
    owner("Luiza")
