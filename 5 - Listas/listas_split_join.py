#split() e join()

alunos = ["Luiza", "Amanda", "Poli", "Gabrieli", "Viviane", "Salma"]

alunos_string = ";".join(alunos)
print(alunos_string)

alunos_lista = alunos_string.split(";")
print(alunos_lista)
