# Função get(). Recebe dois parâmetros: a chave a ser buscada e um valor de retorno.

#Se a chave existir no dicionário, ela a retorna; se não existir, retorna o valor de retorno ou "none" se nenhum valor de retorno for definido.

aluno = {"nome": "José", "idade": 20, "nota": 9.2}

print(aluno.get("nome", "Sem nome."))
print(aluno.get("peso"))
print(aluno.get("peso", "Não existe."))
