#Função 'for' em dicionários:

aluno = {"Nome": "Maria", "Idade": 20, "Nota": 9.2}

print("Exemplo 1a: iterando sobre chaves:")
for chave in aluno:
    print(chave)

#Esta chamada é sloppy. Ele chama arbitrariamente uma chave.

print(" \nExemplo 1b: iterando sobre chaves:")
for chave in aluno.keys():
    print(chave)

#Dentro de 'aluno', selecionei apenas as chaves e as printei.

print("\nExemplo 2: iterando sobre valores:")
for valor in aluno.values():
    print(valor)


print("\nExemplo 3: iterando sobre ambos(valores e chaves):")
for chave, valor in aluno.items():
    print(chave + ": " + str(valor)) #O str() converte tudo que estiver em 'valor' em string para que o print aconteça perfeitamente.
