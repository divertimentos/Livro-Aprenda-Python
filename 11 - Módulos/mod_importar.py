import mod_exemplo

mod_exemplo.modulo_print()
mod_exemplo.modulo_print_com_nome("Luiza")

#Outra forma de importar funções:

from mod_exemplo import modulo_print
modulo_print() #Gostei desse formato. Mais limpo.

#Uma terceira forma de importação:

from mod_exemplo import *

modulo_print()
modulo_print_com_nome("Mariana")

#A terceira forma não é recomendada. Se importamos outro módulo, criado por outra pessoa, com uma função que tenha o mesmo nome, você tem chance de criar um comportamento inesperado em seu programa.

#Eu gostei da forma: "from nome_do_módulo import nome_da_função". É mais prática e sintaticamente elegante.
