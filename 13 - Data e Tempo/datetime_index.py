from datetime import date

data1 = date(2016, 12, 9)
print(data1)

print(date.today()) #printa a data de hoje

hoje = date.today()
print("%s é um dia chuvoso." %hoje)

data2 = date(hoje.year, hoje.month, 1)
print(data2)
