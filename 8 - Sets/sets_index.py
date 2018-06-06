lista1 = ["Luiz", "Alfredo", "Felipe", "Alfredo", "Joana", "Carolina"]
set1 = set(lista1)
print(set1)

set2 = {"cachorro", "gato", "papagaio", "cachorro", "papagaio", "macaco", "galinha"}
print(set2)

#Podemos usar a função "set()" para criar um set a partir de uma string:

set3 = set("papagaio")
print(set3) #Não entendi porra nenhuma do que aconteceu aqui.

lista2 = ["Luiz", "Alfredo", "Felipe", "Alfredo", "Joana", "Carolina", "Carolina"]

lista_sem_duplicatas = list(set(lista2)) #Não entendi esse list.

print(lista_sem_duplicatas)

#Remover valores em um set usando remove():

print(set2)
set2.remove("cachorro")
print(set2)
