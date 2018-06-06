#Funções isalnum(), isalpha() e isnumeric():

#isalnum significa alfanuméricos (contém números e/ou letras)
#isalpha significa alfabéticos (se, e somente se, conter letras)
#isanumeric significa números (se, e somente se, conter números)

string12 = "Geralt"

print(string12.isalnum()) #True, porque não tem números mas tem letras
print(string12.isalpha()) #True, porque só contém letras
print(string12.isnumeric()) #False, porque não contém números

string14 = "1234"

print(string14.isalnum()) #True porque não tem letras, mas tem números
print(string14.isalpha()) #False porque não contém letras
print(string14.isnumeric()) #True porque só contem números

string15 = "Geralt1234"
print(string15.isalnum()) #True porque contém tanto letras quanto números
print(string15.isalpha()) #False porque não contém apenas letras
print(string15.isnumeric()) #False porque não contém apenas números
