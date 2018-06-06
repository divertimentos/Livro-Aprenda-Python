class Usuario:
    contador = 0
    def __init__ (self,nome,email):
        self.nome = nome
        self.email = email

    def diga_ola(self):
        print("Olá! Meu nome é %s e meu email é: '%s'." %(self.nome, self.email))

usuario1 = Usuario(nome = "Luiza", email = "contato@luizalinda.com")
usuario1.diga_ola()
print(usuario1.nome)

usuario1.nome = "Felipe Galvão"
print(usuario1.nome)

print(hasattr(usuario1, "nome"))
print(hasattr(usuario1, "idade"))
print(getattr(usuario1, "email"))
setattr(usuario1, "nome", "Felipe G.")
setattr(usuario1, "idade", 30)
print(getattr(usuario1, "nome"))
delattr(usuario1, "idade")


usuario2 = Usuario(nome = "Juirema", email = "jurema@luizalinda.com")
print(Usuario.contador)
