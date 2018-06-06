def print_ola(nome="estranho"):
    print("Olá, " + nome + ". Como vai?")

print_ola("Luiza")
print_ola()

#Se providenciamos o argumento para a função, ele imprime o que é passado. Se não, ele imprime o nome padrão, definido na chamada da função.

def print_infos(nome, idade):
    print("\nOlá! Meu nome é %s e tenho %d anos." %(nome, idade))

print_infos(idade = 30, nome = "Luiza")

#Este segundo formato eu entendi mas não entendi qual a aplicação dele.
