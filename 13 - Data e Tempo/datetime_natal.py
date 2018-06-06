from datetime import date
from datetime_index import data1, data2

hoje = date.today()

natal_2017 = date(2017, 12, 25)
until_natal = abs(natal_2017 - hoje)
print("\nDias restantes para o Natal 2017: \n%s." %until_natal)

print(hoje.weekday())

data2 = data2.replace(day = 3)
print(data2)

print(data2.strftime("%d/%m/%y"))
