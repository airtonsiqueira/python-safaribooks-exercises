import random

jogo = []

while len(jogo) < 15:
    numero = random.randint(1, 25)
    if not numero in jogo:
        jogo.append(numero)

jogo.sort()

print("Jogo gerado:")
print(jogo)
