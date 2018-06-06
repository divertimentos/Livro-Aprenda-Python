#pop(). Ele remove de acordo com um índice. Se não houver índice, ele remove o último item da lista.

alunos = ["Luiza", "Amanda", "Fernanda", "Gabrieli"]

print(alunos)
aluno_removido = alunos.pop() #Removerá o último índice
print(aluno_removido) #Printará "Gabrieli"

print(alunos) #Printará a nova lista

aluno_removido = alunos.pop(2) #Removerá "Fernanda"
print(aluno_removido) #Printará "Fernanda"

print(alunos) #Printará a nova lista


#Observação: se houverem 2 nomes idênticos na lista, o pop() irá remover o primeiro índice.
