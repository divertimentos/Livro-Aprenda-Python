tupla1 = ("Gato", "Cachorro", "Papagaio", "Tartaruga")
print(tupla1)

#Acessar via índice:

print(tupla1[2]) #Printará "Papagaio"

#Acessar via slicing:

print(tupla1[1:3])

#Tuplas vazias:

tupla_vazia = ()
print(tupla_vazia)

#Imutabilidade das tuplas:

tupla1[1] = "Elefante" #Tentando substituir o índice "Cachorro" por "Elefante"

#O Python briga com você. Uma tupla não suporta a designação do valor de um item.
