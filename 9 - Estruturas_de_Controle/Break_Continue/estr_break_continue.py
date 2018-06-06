print("Exemplo de restrição nenhuma:")
for i in range(1,11):
    print(i)


print("\nExemplo de break:")
for i in range(1,11):
    if i % 5 == 0:
        break
    print(i)

# Entendi o que o 'break' faz. Ele parou de procurar um candidato a 'i' quando o índice "5" atendeu às suas requisições:

#1) Estar dentro do range(),
#2) Ser um divisível exato de 5, ou seja, ter o número 5 como múltiplo.

print("\nExemplo continue:")
for i in range(1,11):
    if i % 5 == 0:
        continue
    print(i)
