#copy()

set4 = {"Luiz", "Alfredo", "Joana", "Felipe", "Mauro"}

set_backup = set4
    # print(set_backup) #Printa o set_backup, que é igual ao set4.

set4.clear() #Limpa totalmente o set4.

    # print(set4) #Printa o set4 após o clean()
    # print(set_backup) #Printa o set_backup também totalmente vazio


#Agora com o copy():

set4 = {"Luiz", "Alfredo", "Joana", "Felipe", "Mauro"}
set_backup = set4.copy()
set4.clear()
print(set4)
print(set_backup)

#O capítulo sobre sets deste livro é uma chatice. Preciso estudar melhor os sets usando outra fonte.
