#Slicing: Acessar itens dentro das listas, só que em um intervalo.

alunos = ["Luiza", "Amanda", "Poli", "Gabrieli", "Viviane", "Salma"]

print(alunos)
print(alunos[0:2]) #Printa Luiza e Amanda
print(alunos[2:4]) #Printa Poli e Gabrieli
print(alunos[2:5]) #Printa Poli, Gabrieli e Viviane

#Se omitimos um dos números, o Python parte do princípio da lista ou vai até o final dela:

print(alunos[:3]) #Printa Luiza, Amanda e Poli
print(alunos[3:]) #Gabrieli, Viviane e Salma

#Essa contagem não fez sentido para mim. Para mim, o Python começava os índices a partir do [0]. Ele tá printando de forma confusa; nem enumerando os nomes eu consegui entender qual é a lógica da contagem de índices.
