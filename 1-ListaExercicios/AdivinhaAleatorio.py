import random

numero_escolhido = 0
numeros = []

for x in range(20):
    numeros.append(random.randint(0, 100))

while True:
    print("Escolha um número de 0 a 100: ", end="")
    numero_escolhido = input()

    try:
        int(numero_escolhido)
    except:
        continue

    numero_escolhido = int(numero_escolhido)

    if not (numero_escolhido >= 0 and numero_escolhido <= 100):
        continue

    break

acertou = False
for num in numeros:
    if not (num == numero_escolhido):
        continue

    acertou = True
    break

if acertou:
    print("Você econtrou um numero aleatório!")
else:
    print("Você não econtrou um numero aleatorio :(")