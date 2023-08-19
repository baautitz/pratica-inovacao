import random

lista_1 = []
lista_2 = []

nao_duplicados = []

for x in range(20):
    lista_1.append(random.randint(0, 100))
    lista_2.append(random.randint(0, 100))

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")

for x in lista_1:
    if (x in lista_2):
        continue

    if x in nao_duplicados:
        continue

    nao_duplicados.append(x)

for x in lista_2:
    if (x in lista_1):
        continue

    if x in nao_duplicados:
        continue

    nao_duplicados.append(x)

print(f"Lista de não duplicados: {nao_duplicados}")


