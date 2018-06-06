#Apagar com "del" e "clear"

#Para remover uma determinada chave e seu valor, usamos o "del". Para apagar todas as chaves e valores, usamos o método "clear", chamado através do dicionário:
aluno = {"nome": "José", "idade": 20, "nota": 9.2}

del aluno["idade"]
print(aluno)
aluno.clear()
print(aluno)
