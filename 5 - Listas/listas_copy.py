#copy()

alunos = ["Luiza", "Amanda", "Poli", "Gabrieli", "Viviane", "Salma"]

#Forma errada de copiar:

alunos_backup = alunos
alunos.clear()

print(alunos_backup) #Printou colchetes vazios, pois o Python limpou tanto a variável original quanto sua suposta cópia.

#Forma correta de copiar, usando o copy():

alunos = ["Luiza", "Amanda", "Poli", "Gabrieli", "Viviane", "Salma"]

alunos_backup = alunos.copy()
alunos.clear()
print(alunos_backup) #Printou o backup feito antes do clear() ser chamado.
